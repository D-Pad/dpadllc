from flask import Flask, Response, request, stream_with_context
from flask_cors import CORS
import requests

from os import environ
from json import loads, JSONDecodeError


app = Flask(__name__)
CORS(app)


class ChatStateManager:

    def __init__(self) -> None:
        self.clients = {}
        self.urls = {
            "prompt": "http://llama:7000/completion",
            "chat": "http://llama:7000/v1/chat/completions"
        }

    def add_new_client(self, ip: str):
        if ip not in self.clients:
            messages = [ 
                {
                    "role": "system", 
                    "content": "You are an AI version of D-Pad Something..."
                },
            ]
            self.clients[ip] = messages 

    def add_user_message(self, ip: str, prompt: str):
        self.clients[ip].append({
            "role": "user",
            "content": prompt 
        })
    
    def client_exists(self, ip: str) -> bool:
        return ip in self.clients


chat_bot = ChatStateManager()


@app.route("/")
def home():
    return {"Hello": "world"}


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    
    if "prompt" not in data:
        return "Invalid request format"

    CLIENT_IP = request.remote_addr

    if not chat_bot.client_exists(CLIENT_IP):
        chat_bot.add_new_client(CLIENT_IP)

    chat_bot.add_user_message(CLIENT_IP, data['prompt'])

    payload = {
        "model": "local-llama",
        "messages": chat_bot.clients[CLIENT_IP],
        "n_predict": 256,
        "temperature": 0.7,
        "stream": True,
        "stop": ["</s>"]
    }

    resp = requests.post(chat_bot.urls['chat'], 
                         json=payload,
                         stream=True)

    def generate():
        for line in resp.iter_lines():
            if line:
                try:
                    raw_json_data = loads(line.decode().replace("data: ", ""))
                    decoded = raw_json_data['choices'][0]['delta']
                    
                    if "content" in decoded: 
                        ret_data = decoded['content']
                        if ret_data is None:
                            continue
                    else:
                        last_frame = raw_json_data['choices'][0]
                        if "finish_reason" in last_frame:
                            ret_data = "" 
                        else:
                            ret_data = f"UNEXPECTED RESPONSE: {raw_json_data}"
                 
                except JSONDecodeError:
                    ret_data = "" 

                yield bytes(str(ret_data), "utf-8")


    return Response(
        stream_with_context(generate()),
        content_type="text/event-stream"
    )


def start_server():
    API_PORT = int(environ.get("WEBPAGE_API_PORT", 8082))
    app.run(host="0.0.0.0", 
            port=API_PORT, 
            debug=True) 

