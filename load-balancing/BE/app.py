from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
FILE = "/data/data.txt"

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Item(BaseModel):
    message: str

@app.post("/add")
def add_item(item: Item):
    with open(FILE, "a") as f:
        f.write(item.message + "\n")
    return {"status": "saved"}

@app.get("/list")
def list_items():
    if not os.path.exists(FILE):
        return {"items": []}
    with open(FILE, "r") as f:
        items = f.read().splitlines()
    return {"items": items}
