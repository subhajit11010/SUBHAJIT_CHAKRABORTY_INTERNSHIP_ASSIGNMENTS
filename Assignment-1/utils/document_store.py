import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class InMemoryDocumentStore:
    def __init__(self, embedding_model_name='Qwen/Qwen3-Embedding-0.6B'):
        self.embedder = SentenceTransformer(embedding_model_name)
        self.embeddings = None
        self.texts = []
        self.index = None


    def add_documents(self, texts: list[str]):
        embs = self.embedder.encode(texts, convert_to_numpy=True)
        if self.embeddings is None:
            self.embeddings = embs
        else:
            self.embeddings = np.vstack([self.embeddings, embs])

        self.texts.extend(texts)
        d = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(self.embeddings)


    def query(self, text: str, k: int = 3):
        q_emb = self.embedder.encode([text], convert_to_numpy=True)
        D, I = self.index.search(q_emb, k)
        results = [self.texts[i] for i in I[0] if i < len(self.texts)]
        return results