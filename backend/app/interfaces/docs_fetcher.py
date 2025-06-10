from typing import Protocol

class DocsToIndexFetcher(Protocol):
    def __call__(self) -> list[dict]: ...