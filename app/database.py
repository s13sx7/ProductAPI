from typing import Annotated
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column
from config import settings, get_url


DataBaseURL = get_url()

engine = create_async_engine(DataBaseURL)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]

class Base(DeclarativeBase):
    __abstract__ = True
    ...