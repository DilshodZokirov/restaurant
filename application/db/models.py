from datetime import datetime
from application.configs.db_config import Base
from sqlalchemy import Boolean, String, Integer, Text, DateTime, Column, Float, ForeignKey


class User(Base):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    username: str = Column(String(length=120), nullable=False, unique=True)
    language: str = Column(String, default='en')
    role: str = Column(String(length=120), default="employee", server_default='employee')
    status: str = Column(String(length=50), default="pending")
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String(length=120), nullable=False, unique=True)
    description: str = Column(Text)
    star: float = Column(Float, default=1.0)
    director: int = Column(Integer, ForeignKey('users.id'))
    is_closed: bool = Column(Boolean, default=True)
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')


class Table(Base):
    __tablename__ = 'table'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey('users.id'))
    restaurant_id: int = Column(Integer, ForeignKey('restaurant.id'))
    qr_code: str = Column(String)
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    number: int = Column(Integer)


class Product(Base):
    __tablename__ = 'product'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String)
    description: int = Column(Text)
    price: float = Column(Float)
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')


class TableProduct(Base):
    __tablename__ = 'table_product'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    table_id: int = Column(Integer, ForeignKey('table.id'))
    product_id: int = Column(Integer, ForeignKey('product.id'))
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
