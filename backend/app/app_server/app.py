from fastapi import FastAPI
from os import environ
import uvicorn
import requests


app = FastAPI()


LLM_URL = "http://localhost:7000/completion"


@app.get("/")
def home():
    return {"Hello": "world"}


@app.post("/chat")
async def chat(prompt: str):
    payload = {
        "prompt": prompt,
        "n_predict": 256,
        "temperature": 0.7,
        "stop": ["</s>"]
    }
    resp = requests.post(LLM_URL, json=payload)
    return resp.json()


def start_server():
    API_PORT = environ.get("WEBPAGE_API_PORT", 8082)
    uvicorn.run("main:app", host="0.0.0.0", port=API_PORT, reload=True) 

