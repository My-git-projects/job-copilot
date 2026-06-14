from pydantic import BaseModel

class ATSRequest(BaseModel):
    resume: str
    job: str