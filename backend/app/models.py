from pydantic import BaseModel

class Query(BaseModel):
    query: str

class Product(BaseModel):
    product: str
    product_desc: str
    category: str
    category_desc: str
    price: float
    stock: int

class RAGResponse(BaseModel):
    answer: str
    products: list[Product]