from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import dotenv_values
from sqlalchemy.pool import NullPool


config = dotenv_values("./.env")
username = config.get("DB_USERNAME")
password = config.get("DB_PASSWORD")
dbname = config.get("DB_NAME")
DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@localhost:5432/{dbname}"


class Base(AsyncAttrs, DeclarativeBase):
    pass


async_engine = create_async_engine(DATABASE_URL, poolclass=NullPool, echo=True)
async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
