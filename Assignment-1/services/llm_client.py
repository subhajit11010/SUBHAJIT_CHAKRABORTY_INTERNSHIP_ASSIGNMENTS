import langchain
import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
load_dotenv()

class LLMClient:
    def __init__(self):
        self.client = ChatOpenAI(model='deepseek/deepseek-r1-0528:free', temperature=0.2, api_key=os.getenv('OPENROUTER_API_KEY'), base_url=os.getenv('OPENROUTER_BASE_URL'))

    async def chat(self, messages, max_tokens=512):
        resp = await self.client.agenerate([messages])
        return resp.generations[0][0].text

    async def generate_prompt(self, prompt: str):
        messages = [HumanMessage(content=prompt)]
        return await self.chat(messages)