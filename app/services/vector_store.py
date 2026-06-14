import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.meta = []

    def add(self, text, meta):
        vec = self.model.encode([text])[0].astype("float32")
        self.index.add(np.array([vec]))
        self.meta.append(meta)

    def search(self, query, k=3):
        vec = self.model.encode([query])[0].astype("float32")
        _, I = self.index.search(np.array([vec]).reshape(1, -1), k)
        return [self.meta[i] for i in I[0] if i < len(self.meta)]