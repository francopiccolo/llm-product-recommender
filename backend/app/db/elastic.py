from elasticsearch import Elasticsearch

from backend.app.interfaces.docs_store import DocsStoreInterface

class ElasticDocsStore(DocsStoreInterface):
    def __init__(self, es: Elasticsearch, index: str):
        self.es = es
        self.index = index

    def index_documents(self, documents: list[dict]) -> None:
        for i, doc in enumerate(documents):
            self.es.index(index=self.index, id=i, document=doc)

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        res = self.es.search(index=self.index, query={"match": {"content": query}}, size=top_k)
        return [hit["_source"] for hit in res["hits"]["hits"]]
