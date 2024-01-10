import os

from typing import Final
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_KEY: Final = os.environ["TELEGRAM_KEY"]