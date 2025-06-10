from backend.tests.conftest import sample_products_fixture

def test_rag(client, sample_products_fixture):
    response = client.get("/rag", params={"q": "test"})
    assert response.status_code == 200
    assert response.json() == {
        "answer": "Mock answer",
        "products": sample_products_fixture
    }