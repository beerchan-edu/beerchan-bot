import os

from dotenv import load_dotenv

load_dotenv()

username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
dbname = os.getenv("POSTGRES_DB")
host = "db"
tg_key = os.getenv("TELEGRAM_KEY")
