from backend.app.interfaces.docs_store import DocsStoreInterface
from backend.app.interfaces.llm import LLMInterface
from backend.app.models import Product

PROMPT_TEMPLATE = """
You're a shopping assistant.

Based on the customer's QUESTION, recommend one or more products from the CONTEXT,
explaining why you made those choices.

Use only the products from the CONTEXT when making recommendations.

QUESTION: {question}

CONTEXT:
{context}
"""

def build_prompt(query: str, context: str) -> str:
    return PROMPT_TEMPLATE.format(question=query, context=context)

def query(query: str, store: DocsStoreInterface, llm: LLMInterface):
    docs = store.search(query, top_k=3)
    if not docs:
        return "No relevant documents found."
    products = [Product(**doc) for doc in docs]
    context = "\n\n".join([product.model_dump_json(indent=2) for product in products])
    prompt = build_prompt(query, context)
    return {
        "answer": llm.query(prompt),
        "products": products,
    }