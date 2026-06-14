from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class JobData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/analyze")
def analyze(job: JobData):

    return {
        "score": 75,
        "matched": [
            "linux",
            "aws"
        ],
        "missing": [
            "terraform"
        ]
    }