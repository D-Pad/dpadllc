from flask import Flask, Response, request, stream_with_context, jsonify
from flask_cors import CORS
import requests

from os import environ
from json import loads, JSONDecodeError
from threading import Thread
from time import sleep
from datetime import datetime
from db_connection import DatabaseConnector


app = Flask(__name__)
CORS(app)


INITIAL_CONTENT = """
You are D-Bot, the official AI representative for D-Pad LLC. The owner of 
the company is a Full Stack Developer with 4+ years of professional 
experience designing, building, and deploying containerized web applications. 
He specializes in frontend SPA development, database design, Linux server 
provisioning , and Docker-based deployments. Strong background in Python, 
Flask, Vue.js, Linux, and real-time event-driven systems.

As a company, we have experience working with automated trading systems, have 
lots of knowledge on trading concepts, and familiararity with trading 
instruments such as futures and options. Vast knowledge of block chain 
technology and Web3 concepts as well as computer hardware and 
I.T. in general

The owners favorite retro video game series is Donkey Kong for the SNES. His 
favorite modern game is Overwatch. The name D-Pad comes from the owners love 
of chiptune music and modifying Gameboy hardware, as well as working with small 
electronics.

The interface that is being used to communicate to you with, is the home page
of our company website, which serves only as a portfolio/resume. Contact
information is found on the resume page
"""

MAX_MSG_COUNT = 5


DAILY_LIMIT_MSG = """Daily message limit reached. This LLM runs on a server 
without a GPU, and is not intended to be used as a puublic chatbot. It's only 
purpose is to show the technical abilities of the website creator. We only 
have 1 server for now, and it's self-hosted. Each chat message maxes out the 
CPU while the response is generating, and we need this CPU for development
purposes.
"""


WELCOME_MSG = f"""Welcome to the home page of D-Pad LLC! This is the owner speaking. You can ask our chat bot questions about the company if you'd like, but 
you're limited to only {MAX_MSG_COUNT} prompts per day. This app runs on my 
home server, and is more of a technical ability demonstration than a public 
service. Feel free to read our "About Us" page, or download my resume from the
navigation bar above.
"""


API_PORT = int(environ.get("WEBPAGE_API_PORT", 8082))


class ChatStateManager:

    def __init__(self) -> None:
        self.clients = {}
        self.urls = {
            "prompt": "http://llama:7000/completion",
            "chat": "http://llama:7000/v1/chat/completions"
        }

        def client_manager():
            timeout = 86440  # 1 day 
            while True:
                
                ts = datetime.now().timestamp()
                for client_ip in [i for i in self.clients.keys()]:
                    seconds = ts - self.clients[client_ip]['time']
                    if seconds >= timeout:
                        del self.clients[client_ip]

                sleep(1)

        self.client_management_thread = Thread(target=client_manager)
        self.client_management_thread.start()

    def add_new_client(self, ip: str):
        if ip not in self.clients:
            messages = [ 
                {
                    "role": "system", 
                    "content": INITIAL_CONTENT
                },
            ]
            self.clients[ip] = {
                "messages": messages,
                "time": datetime.now().timestamp(), 
                "msg_count": 0
            }

    def add_message(self, ip: str, prompt: str, role: str):
        self.clients[ip]['messages'].append({
            "role": role,
            "content": prompt 
        })
        if role == "user": 
            self.clients[ip]["msg_count"] += 1
    
    def client_exists(self, ip: str) -> bool:
        return ip in self.clients


chat_bot = ChatStateManager()


@app.route("/welcome", methods=["POST"])
def welcome():

    DatabaseConnector().update_visitor_count(request.remote_addr)

    def welcome_msg_stream():
       for word in WELCOME_MSG.replace("\n", " ").split(" "):
           sleep(0.1) 
           yield bytes(f"{word} ", "utf-8")

    return Response(
        stream_with_context(welcome_msg_stream()),
        content_type="text/event-stream"
    )


@app.route("/data", methods=["POST"])
def data_fetch():
    params = request.json
    
    if "dataId" not in params:
        return "Invalid input parameters"
    data_id = params["dataId"]

    if data_id == "visitorCount":
        db = DatabaseConnector()
        visitors = db.get_visitors()
        return jsonify({
            "visitorCount": len(visitors)
        })

    return ""


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    
    if "prompt" not in data:
        return "Invalid request format"

    CLIENT_IP = request.remote_addr

    if not chat_bot.client_exists(CLIENT_IP):
        chat_bot.add_new_client(CLIENT_IP)
    else:

        if chat_bot.clients[CLIENT_IP]["msg_count"] >= MAX_MSG_COUNT:
            
            def max_count_reached_msg():
                for word in DAILY_LIMIT_MSG.replace("\n", " ").split(" "):
                    sleep(0.2) 
                    yield bytes(f"{word} ", "utf-8")
            
            return Response(
                stream_with_context(max_count_reached_msg()),
                content_type="text/event-stream"
            )

    chat_bot.add_message(CLIENT_IP, data['prompt'], "user")

    payload = {
        "model": "local-llama",
        "messages": chat_bot.clients[CLIENT_IP]['messages'],
        "n_predict": 1536,
        "temperature": 0.7,
        "stream": True
    }

    resp = requests.post(chat_bot.urls['chat'], 
                         json=payload,
                         stream=True)

    def generate():

        chat_bot.add_message(CLIENT_IP, "", "system")
        
        for line in resp.iter_lines():
            if line:
                try:
                    raw_json_data = loads(line.decode().replace("data: ", ""))
                    decoded = raw_json_data['choices'][0]['delta']

                    if "content" in decoded: 
                        ret_data = decoded['content']
                        if ret_data is None:
                            continue
                        last = chat_bot.clients[CLIENT_IP]["messages"][-1]
                        last['content'] += ret_data
                    
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


@app.route("/health")
def health_check():
    return "Server is up"


def start_server():
    app.run(host="0.0.0.0", 
            port=API_PORT, 
            debug=True) 

