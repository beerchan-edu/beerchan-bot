import os

from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from consts import TELEGRAM_KEY


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TODO write your code here!
    
    await update.message.reply_text(f"Hello there. {update.message.from_user.id}|{update.message.from_user.full_name}")

if __name__ == "__main__":
    print("Starting bot")
    app = Application.builder().token(TELEGRAM_KEY).build()

    # commands
    app.add_handler(CommandHandler("hello", hello_command))

    print("Polling")
    app.run_polling(poll_interval=3)
