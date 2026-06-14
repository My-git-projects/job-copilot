from pathlib import Path

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from pydantic import BaseModel

from matcher import compare

from app.services.pdf_parser import (
    extract_text_from_pdf
)

from app.services.skill_extractor import (
    extract_skills
)

from app.services.resume_service import (
    save_resume,
    get_resumes
)

app = FastAPI()

UPLOAD_FOLDER = "uploads"

Path(UPLOAD_FOLDER).mkdir(
    exist_ok=True
)


class JobData(BaseModel):
    text: str


@app.get("/")
def home():

    return {
        "status": "running"
    }


@app.post("/analyze")
def analyze(job: JobData):

    return compare(job.text)


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = (
        f"{UPLOAD_FOLDER}/{file.filename}"
    )

    contents = await file.read()

    with open(
        file_path,
        "wb"
    ) as uploaded_file:

        uploaded_file.write(contents)

    pdf_text = extract_text_from_pdf(
        file_path
    )

    skills = extract_skills(
        pdf_text
    )

    save_resume(
        {
            "resume_name":
                file.filename,

            "skills":
                skills
        }
    )

    return {
        "status":
            "uploaded",

        "filename":
            file.filename,

        "skills":
            skills
    }


@app.get("/resumes")
def resumes():

    return get_resumes()