from elasticsearch import Elasticsearch

from backend.app.db.elastic import ElasticDocsStore
from backend.app.llms.gpt import GPT

def get_docs_store():
    es = Elasticsearch("http://localhost:9200")
    index = "product_vectors"
    return ElasticDocsStore(es, index)

def get_docs_to_index_fetcher():
    from backend.tests.conftest import get_sample_products
    return get_sample_products

def get_llm():
    return GPT()