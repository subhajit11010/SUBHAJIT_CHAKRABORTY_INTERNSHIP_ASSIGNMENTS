from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from pydantic import BaseModel
import uvicorn
import pypdf
import io
from services.llm_client import LLMClient
from services.summarizer import summarize_text
from services.qa_service import QAService
from services.learning_path import LearningPathService

app = FastAPI(title="LangChain Agents")
llm = LLMClient()
qa_service = QAService(llm)
learning_path_service = LearningPathService(llm)

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 200

@app.post("/summarize")
async def summarize(req: SummarizeRequest):
    if not req.text:
        raise HTTPException(status_code=400, detail="Text is required")
    result = await summarize_text(llm, req.text, req.max_length)
    return {"summary": result}

@app.post("/qa")
async def qa(file: UploadFile = File(...), question : str = Form(...)):
    if not question:
        raise HTTPException(status_code=400, detail="Question is required")
    content = await file.read()
    content_stream = io.BytesIO(content)

    if file.content_type == "application/pdf":
        try:
            reader = pypdf.PdfReader(content_stream)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to read PDF file: {e}")
        
    else:
        # for text files,  .md files etc
        text = content.decode('utf-8', errors='ignore') # that means just ignore the errors if occur

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="The uploaded document contains no readable text. This can happen with image-based PDFs."
        )

    answer = await qa_service.answer(text, question)
    return {"answer": answer}

class LearningPathRequest(BaseModel):
    background: str
    goal: str
    months: int = 3

@app.post("/get_suggestions")
async def learning_path_suggestions(req: LearningPathRequest):
    suggestions = await learning_path_service.suggest_path(req.background, req.goal, req.months)
    return {"learning_path": suggestions}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
