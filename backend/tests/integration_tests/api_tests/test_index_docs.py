from backend.tests.conftest import get_sample_products

def test_index_documents(client, mock_docs_store):
    response = client.post("/index-documents")
    assert response.status_code == 200
    assert response.json() == {"status": "indexed"}
    assert mock_docs_store.index_called_with == get_sample_products()