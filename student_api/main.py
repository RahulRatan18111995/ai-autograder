import os
from fastapi import FastAPI, HTTPException
from starlette.requests import Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Autograder API is running!"}

@app.post("/generate")
async def generate(request: Request):
    payload = await request.json()
    expected_secret = os.getenv("EXPECTED_SECRET")
    if payload.get("secret") != expected_secret:
        raise HTTPException(status_code=400, detail="Invalid secret")
    repo_url = f"https://github.com/{payload['email']}/{payload['task']}"
    return {"status": "success", "repo_url": repo_url}
