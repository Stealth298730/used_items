from typing import Annotated,List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException,status,Depends,APIRouter
from sqlalchemy import select

from app.db.users import db_actions
from app.db.base import get_db
from app.pydantic_models.products import ProductsModel,ProductModel

from app.db.products.models import Products
from app.db.products import db_actions


SQLALCHEMY_URI = "mysql+aiomysql://avnadmin:AVNS_Iikg04VtR779Zq_RmtE@mysql-14a9ee6a-serhii-4322.j.aivencloud.com:11907/used_items"
products_route = APIRouter(prefix="/products",tags=["Product"])


@products_route.post("/",status_code=status.HTTP_201_CREATED,response_model=ProductModel)
async def add_product(
    product:ProductModel,
    db:Annotated[AsyncSession,Depends(get_db)]
):
    return await db_actions.add_product(name=product.name,price=product.price,db=db)   

@products_route.get("/", status_code=status.HTTP_200_OK, response_model=List[ProductModel])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products))
    products = result.scalars().all()
    return [ProductModel.from_orm(p) for p in products] 


@products_route.delete("/",status_code=status.HTTP_202_ACCEPTED,response_model=ProductModel)
async def delete_product(
    product:ProductModel,
    db:Annotated[AsyncSession,Depends(get_db)]
):
    return await db_actions.delete_product(name=product.name,price=product.price,db=db)