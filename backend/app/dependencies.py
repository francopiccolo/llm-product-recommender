from elasticsearch import Elasticsearch

from backend.app.db.elastic import ElasticDocsStore
from backend.app.llms.gpt import GPT

def get_docs_store():
    es = Elasticsearch("http://localhost:9200")
    index = "product_vectors"
    return ElasticDocsStore(es, index)

def get_docs_fetcher():
    pass

def get_llm():
    return GPT()