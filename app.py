from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from decouple import config


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World", "App": "Test", "Version": config("APP_VERSION", default="1.0.0")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}