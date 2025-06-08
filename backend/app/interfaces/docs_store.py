from abc import ABC, abstractmethod

class DocsStoreInterface(ABC):
    @abstractmethod
    def index_docs(self, documents: list[dict]) -> None:
        pass

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> list[dict]:
        pass