import os

from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from consts import TELEGRAM_KEY

from .db import Base, db_connect, create_session 
from .models import Sport 


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    await update.message.reply_text(f"Hi {update.effective_user.name}!")

if __name__ == "__main__":
    print("Starting bot")
    app = Application.builder().token(TELEGRAM_KEY).build()

    # commands
    app.add_handler(CommandHandler("hello", hello_command))

    print("Polling")
    app.run_polling(poll_interval=3)

# Connection to db and creating table
# engine = db_connect()
# Base.metadata.create_all(engine)

# Creating session
# session = create_session(engine)
