from sqlalchemy import select
from app.dao.base import BaseDAO
from app.products.models import Products
from app.database import async_session_maker
class ProductsDAO(BaseDAO):
    model = Products
    
    
    @classmethod
    async def filter_by(cls, name=None, category=None, min_qty=None, max_qty=None, min_cost=None, max_cost=None):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            filters = []
            if name:
                filters.append(cls.model.name.ilike(f"%{name}%"))
            if category is not None:
                filters.append(cls.model.category == category)
            if min_qty is not None:
                filters.append(cls.model.qty >= min_qty)  
            if max_qty is not None:
                filters.append(cls.model.qty <= max_qty)  
            if min_cost is not None:
                filters.append(cls.model.cost >= min_cost)
            if max_cost is not None:
                filters.append(cls.model.cost <= max_cost)

            if filters:
                query = query.where(*filters)

            result = await session.execute(query)
            return result.mappings().all()