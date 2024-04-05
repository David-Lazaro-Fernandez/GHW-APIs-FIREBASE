from typing import Union
from fastapi import FastAPI
from firebase import create_document
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/add_hacker")
def add_hacker(name: str, ghw: str, status: str):
    data = {
        "name": name,
        "ghw": ghw,
        "status": status
    }
    create_document("hackers", data)
    return {"status": "success"}