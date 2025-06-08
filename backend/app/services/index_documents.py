from typing import Callable

from backend.app.interfaces.docs_store import DocsStoreInterface

DocsFetcher = Callable[[], list[dict]]

def index_docs(
    fetch_docs: DocsFetcher,
    docs_store: DocsStoreInterface,
):
    docs = fetch_docs()
    docs_store.index_docs(docs)