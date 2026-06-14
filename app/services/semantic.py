from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_score(resume: str, job: str) -> float:
    r = model.encode([resume])[0]
    j = model.encode([job])[0]

    score = np.dot(r, j) / (np.linalg.norm(r) * np.linalg.norm(j))
    return round(score * 100, 2)