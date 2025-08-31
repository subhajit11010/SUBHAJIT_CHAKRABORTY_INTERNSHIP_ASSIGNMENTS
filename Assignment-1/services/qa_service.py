from services.llm_client import LLMClient
from utils.document_store import InMemoryDocumentStore

class QAService:
    def __init__(self, llm: LLMClient):
        self.llm = llm
        self.store = InMemoryDocumentStore()
    
    async def answer(self, doc_text: str, question: str):
        if doc_text is None or doc_text.strip() == "":
            print("Document text is empty.")
        paras = [p.strip() for p in doc_text.split('\n\n') if p.strip()]
        self.store.add_documents(paras)
        relevant = self.store.query(question, k=4)
        context = '\n\n'.join(relevant)
        prompt = f"You are an expert answerer. Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer concisely. If not enough info, say 'Insufficient information.'"
        return await self.llm.generate_prompt(prompt)