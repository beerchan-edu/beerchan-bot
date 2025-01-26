from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import username, password, host, dbname

engine = create_engine(f"postgresql+psycopg://{username}:{password}@{host}:5432/{dbname}", echo=True)
Session = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
