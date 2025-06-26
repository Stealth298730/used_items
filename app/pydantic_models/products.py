from typing import List
from pydantic import BaseModel

class ProductModel(BaseModel):
    id:int
    name: str
    price: int

    class Config:
            from_attributes = True

class ProductsModel(BaseModel):
    products: List[ProductModel]

    class Config:
            from_attributes = True