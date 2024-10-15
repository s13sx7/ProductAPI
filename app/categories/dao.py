from sqlalchemy import func, select
from app.dao.base import BaseDAO
from app.categories.models import Categories
from app.database import async_session_maker
from app.products.models import Products

class CategoriesDAO(BaseDAO):
    model = Categories
    
    @classmethod
    async def qty_products_in_categories(cls):
        async with async_session_maker() as session:
            query = select(cls.model.id, cls.model.name, func.count(Products.id).label('product_qty')).join(Products, Products.category==Categories.id).group_by(Categories.id, Categories.name)
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def qty_products_in_category(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.id, cls.model.name, func.count(Products.id).label('product_qty')).join(Products, Products.category==Categories.id).where(Products.category == model_id).group_by(Categories.id, Categories.name)
            result = await session.execute(query)
            return result.mappings().all()