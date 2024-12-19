from fastapi import FastAPI
from app.routers import users, items

app = FastAPI()

@app.get("/ping")
def read_root():
    return {"message": "pong"}