import re

SKILLS = {
    "python": ["python", "py"],
    "aws": ["aws", "ec2", "s3"],
    "docker": ["docker"],
    "kubernetes": ["k8s", "kubernetes"],
    "fastapi": ["fastapi"],
    "sql": ["sql", "mysql", "postgres"],
    "git": ["git", "github"],
    "ci/cd": ["ci", "cd", "jenkins", "github actions"]
}

def extract_skills(text: str):
    text = text.lower()
    found = set()

    for skill, aliases in SKILLS.items():
        for a in aliases:
            if a in text:
                found.add(skill)

    return sorted(found)