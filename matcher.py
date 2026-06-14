import json
from skills_db import COMMON_SKILLS

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found.append(skill)

    return found

def compare(job_text):

    job_skills = extract_skills(job_text)

    with open(
        "resumes/resume_skills.json",
        "r"
    ) as file:

        resume_skills = json.load(file)["skills"]

    matched = []
    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = 0

    if len(job_skills) > 0:
        score = round(
            len(matched) /
            len(job_skills) * 100,
            2
        )

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }