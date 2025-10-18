from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

class GenerateRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    nonce: str
    brief: str
    evaluation_url: str

@app.get("/")
def root():
    return {"message": "AI Autograder API is running!"}

@app.post("/generate")
def generate(payload: GenerateRequest):
    expected_secret = os.getenv("EXPECTED_SECRET")
    if payload.secret != expected_secret:
        raise HTTPException(status_code=400, detail="Invalid secret")
    return {"status": "success", "message": "Valid secret!"}
