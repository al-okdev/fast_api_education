from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    product_id: int
    name: str | None
    category: str | None
    price: float | None


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

@app.get("/products/search")
async def search_product(keyword: str, category: str = "", limit: int = 10):
    result_product = []
    for product in sample_products:
        if keyword in product['name'] and category in product['category']:
            result_product.append(product)
    
    if result_product:
        return result_product[:limit]
    else:
        return {'no product'}


@app.get("/product/{product_id}")
async def get_product(product_id: int): #  -> Product
    for product in sample_products:
        if product['product_id'] == product_id:
            return product
    return {'no product'}