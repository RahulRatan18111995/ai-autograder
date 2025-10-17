from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from .github_utils import create_repo_and_push

load_dotenv()

app = FastAPI()

class GenerateRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    nonce: str
    brief: str
    evaluation_url: str

@app.post("/generate")
def generate_repo(req: GenerateRequest):
    expected_secret = os.getenv("EXPECTED_SECRET")

    if req.secret != expected_secret:
        raise HTTPException(status_code=400, detail="Invalid secret")

    try:
        repo_url = create_repo_and_push(
            req.email, req.task, req.round, req.nonce, req.brief
        )
        return {"status": "success", "repo_url": repo_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
