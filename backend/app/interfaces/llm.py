from typing import Protocol

class LLMInterface(Protocol):
    def query(self, prompt: str) -> str:
        """Generate a response to the given prompt."""
        ...