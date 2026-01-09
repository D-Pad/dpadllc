from flask import Flask, request
from flask_cors import CORS
import requests

from os import environ


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {"Hello": "world"}


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    payload = {
        "prompt": data["prompt"],
        "n_predict": 256,
        "temperature": 0.7,
        "stop": ["</s>"]
    }

    resp = requests.post("http://llama:7000/completion", json=payload)
    return resp.json() 


def start_server():
    API_PORT = int(environ.get("WEBPAGE_API_PORT", 8082))
    app.run(host="0.0.0.0", 
            port=API_PORT, 
            debug=True) 

