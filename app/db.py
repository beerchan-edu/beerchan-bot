from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import dotenv_values


config = dotenv_values("./.env")
username = config.get("DB_USERNAME")
password = config.get("DB_PASSWORD")
dbname = config.get("DB_NAME")

engine = create_engine(f"postgresql+psycopg://{username}:{password}@localhost:5432/{dbname}", echo=True)
Session = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass