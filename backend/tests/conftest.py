import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.dependencies import get_docs_store, get_llm


@pytest.fixture
def sample_products():
    return [
        {
            "product": "A",
            "product_desc": "This is product A",
            "category": "Electronics",
            "category_desc": "Electronic products",
            "price": 50,
            "stock": 2,
        },
        {
            "product": "B",
            "product_desc": "This is product B",
            "category": "Electronics",
            "category_desc": "Electronic products",
            "price": 30,
            "stock": 0,
        },
    ]

@pytest.fixture
def mock_docs_store(sample_products):
    class MockDocsStore:
        def search(self, query: str, top_k: int):
            return sample_products
    return MockDocsStore()

@pytest.fixture
def mock_llm():
    class MockLLM:
        def query(self, prompt: str):
            return "Mock answer"
    return MockLLM()

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def override_dependencies(mock_docs_store, mock_llm):
    app.dependency_overrides[get_docs_store] = lambda: mock_docs_store
    app.dependency_overrides[get_llm] = lambda: mock_llm
    yield
    app.dependency_overrides.clear()

