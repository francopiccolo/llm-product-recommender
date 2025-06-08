import os

class Settings:
    ELASTIC_URL: str = os.getenv("ELASTIC_URL", "http://localhost:9000")

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = "gpt-4o"

settings = Settings()