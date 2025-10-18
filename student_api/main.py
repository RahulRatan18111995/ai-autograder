from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import logging

# --- Setup ---
app = FastAPI()
logging.basicConfig(level=logging.INFO)


# --- Request Model ---
class GenerateRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    nonce: str
    brief: str
    evaluation_url: str


# --- Test Route ---
@app.get("/")
def root():
    return {"message": "AI Autograder API is running!"}


# --- Generate Route ---
@app.post("/generate")
def generate(payload: GenerateRequest):
    logging.info(f"Received request: {payload.dict()}")

    expected_secret = os.getenv("EXPECTED_SECRET")
    if payload.secret != expected_secret:
        logging.error("Invalid secret key provided!")
        raise HTTPException(status_code=400, detail="Invalid secret")

    # ✅ Replace this with your GitHub repo creation logic
    repo_url = f"https://github.com/example/{payload.task}-repo"
    return {"status": "success", "repo_url": repo_url}

