from fastapi import APIRouter
from app.models.ats_schema import ATSRequest
from app.services.ats_engine import analyze_candidate

router = APIRouter()

@router.post("/analyze")
def analyze(req: ATSRequest):
    return analyze_candidate(req.resume, req.job)