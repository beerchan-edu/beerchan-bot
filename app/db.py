from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import dotenv_values

Base = declarative_base()

def db_connect():    #Connetcion to database from docker container  
# with psql  from .env values (using same vaules from docker-compose.yml)
    config = dotenv_values("./.env")
    username = config.get("DB_USERNAME")
    password = config.get("DB_PASSWORD")
    dbname = config.get("DB_NAME")

    engine = create_engine(f"postgresql+psycopg://{username}:{password}@localhost:5432/{dbname}", echo=True)
    connection = engine.connect()

    return engine, connection



def create_session(engine): #Creating session for entering the database
    Session = sessionmaker(bind=engine)
    return Session()