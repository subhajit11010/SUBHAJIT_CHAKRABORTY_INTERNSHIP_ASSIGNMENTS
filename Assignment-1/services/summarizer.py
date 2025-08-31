from services.llm_client import LLMClient

async def summarize_text(llm: LLMClient, text: str, max_length: int = 200):
    prompt = f"Summarize the following text in <= {max_length} words, keep it concise:\n\n{text}"
    return await llm.generate_prompt(prompt)