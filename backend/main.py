from fastapi import FastAPI
from pydantic import BaseModel

from matcher import compare

app = FastAPI()

class JobData(BaseModel):
    text: str

@app.get("/")
def health():
    return {
        "status": "running"
    }

@app.post("/analyze")
def analyze(job: JobData):
    return compare(job.text)