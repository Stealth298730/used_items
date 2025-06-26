from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from app.db.products.models import Products



async def get_products(db:AsyncSession):
    result = await db.execute(select(Products))
    return result.scalars().all()

async def add_product(name:str,price:int,db:AsyncSession):
    product = Products(name=name,price=price)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

async def delete_product(name:str,price:int,db:AsyncSession):
    result = await db.execute(select(Products).filter_by(name=name,price=price))
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    await db.delete(product)
    await db.commit()
    return product