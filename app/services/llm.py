import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_review(resume, job):
    prompt = f"""
Return JSON only:

{{
  "summary": "",
  "missing_skills": [],
  "strong_skills": [],
  "recommendation": ""
}}

Resume:
{resume}

Job:
{job}
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return res.choices[0].message.content