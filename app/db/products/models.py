from uuid import uuid4
from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.ext.declarative import declarative_base


from app.config import settings


Base = declarative_base()


class Products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    name:Mapped[str] = mapped_column(String(40),unique=True,index=True,nullable=False)
