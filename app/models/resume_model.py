from pydantic import BaseModel


class Resume(BaseModel):
    resume_name: str
    skills: list[str]