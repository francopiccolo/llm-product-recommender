from typing import Protocol

class DocsFetcher(Protocol):
    def __call__(self) -> list[dict]: ...