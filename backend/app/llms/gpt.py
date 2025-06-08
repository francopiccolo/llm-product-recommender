import openai
from backend.app.config import settings
from backend.app.interfaces.llm import LLMInterface

class GPT(LLMInterface):
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.model = settings.OPENAI_MODEL

    def query(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message["content"].strip()