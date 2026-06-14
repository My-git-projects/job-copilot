from skills_db import COMMON_SKILLS


def extract_skills(text: str):

    text = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:

        if skill.lower() in text:

            if skill not in found_skills:
                found_skills.append(skill)

    return found_skills