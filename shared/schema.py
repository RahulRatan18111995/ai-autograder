from pydantic import BaseModel
from typing import Optional

class StudentSubmission(BaseModel):
    secret: str
    brief: str
    email: str
    task: str
    round: int
    nonce: str
    evaluation_url: str


class EvaluationResult(BaseModel):
    email: str
    task: str
    round: int
    repo_url: str
    commit_sha: str
    pages_url: Optional[str] = None
    score: Optional[float] = None
    feedback: Optional[str] = None
