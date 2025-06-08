from fastapi import FastAPI
from backend.app.api.routes import router as api_router

app = FastAPI(title="Product RAG API")
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Product RAG API"}