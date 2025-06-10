from typing import Protocol

class DocsStoreInterface(Protocol):
    def index_docs(self, documents: list[dict]) -> None:
        ...

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        ...