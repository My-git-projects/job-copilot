import json
from app.services.skills import extract_skills
from app.services.semantic import semantic_score
from app.services.llm import llm_review

def analyze_candidate(resume_text, job_text):

    skills = extract_skills(resume_text)
    sem = semantic_score(resume_text, job_text)

    llm = llm_review(resume_text, job_text)

    try:
        llm_json = json.loads(llm)
    except:
        llm_json = {"raw": llm}

    score = min(100, int(sem + len(skills)*2))

    return {
        "match_score": score,
        "semantic_score": sem,
        "skills": skills,
        "llm_analysis": llm_json
    }