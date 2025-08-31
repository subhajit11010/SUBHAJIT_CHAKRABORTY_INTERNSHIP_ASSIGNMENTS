from services.llm_client import LLMClient

class LearningPathService:
    def __init__(self, llm: LLMClient):
        self.llm = llm


    async def suggest_path(self, background: str, goal: str, months: int = 3):
        prompt = (
            f"Create a {months}-month personalized, weekly learning plan for someone with this background: {background}.\n"
            f"The learning goal is: {goal}. The plan should include weekly topics, suggested hands-on projects, and checkpoints. Keep it practical and measurable. Use bullet format."
        )
        return await self.llm.generate_prompt(prompt)