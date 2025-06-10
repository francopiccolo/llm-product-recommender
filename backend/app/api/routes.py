from fastapi import APIRouter, Depends, Query

from backend.app.interfaces.docs_fetcher import DocsToIndexFetcher
from backend.app.interfaces.docs_store import DocsStoreInterface
from backend.app.interfaces.llm import LLMInterface
from backend.app.dependencies import (
    get_docs_to_index_fetcher,
    get_docs_store,
    get_llm,
)
from backend.app.models import RAGResponse
from backend.app.services.rag import query
from backend.app.services.index_documents import index_docs

router = APIRouter()

@router.get("/rag", response_model=RAGResponse)
def rag(
    q: str = Query(..., description="Search query string"),
    store: DocsStoreInterface = Depends(get_docs_store),
    llm: LLMInterface = Depends(get_llm),
):
    """
    Uses LLM to answer query using stored documents as context
    """

    return query(q, store, llm)

@router.post("/index-documents")
def index_documents(
    docs_store: DocsStoreInterface = Depends(get_docs_store),
    docs_to_index_fetcher: DocsToIndexFetcher = Depends(get_docs_to_index_fetcher),
):
    """Indexes products into the documents store"""
    index_docs(docs_to_index_fetcher, docs_store)
    return {"status": "indexed"}