from sqlalchemy import delete, insert, select, update
from app.database import async_session_maker

class BaseDAO:
    model = None
    
    @classmethod
    async def find_by_filter(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().all()
          
    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().one_or_none()
    
    @classmethod
    async def fild_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
    
    @classmethod
    async def add_data(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def update_data(cls,id:int, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def delete_data_by_id(cls, model_id:int):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id==model_id)
            await session.execute(query)
            await session.commit()