from db import Session
from models import Sport
from telegram import Update
from telegram.ext import ContextTypes
import re
from datetime import timedelta

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.name  
    await update.message.reply_text(f"Hi {user}! I write your workout duration in minutes.")


async def save_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with Session() as session:
        with session.begin():
            message_text = update.message.text
            digits = parseNumber(message_text)
            if digits:                
                add_message = Sport(nickname=update._effective_user.name, \
                    user_id=update.effective_user.id, chat_id=update.effective_chat.id,\
                        duration=timedelta(minutes=digits), message=message_text.replace("/save ", ""))
                session.add(add_message)
            else:
                await update.message.reply_text("Write a command in correct format: mm")


async def test_result(update: Update, context: ContextTypes.DEFAULT_TYPE): # not working anymore
    with Session() as session:
        with session.begin():
            user = update.effective_user.name
            sports = Sport.get_query(session, user)()
            for sport in sports:
                result = f"{sport.nickname} / {sport.message}"
                await update.message.reply_text(f"{result}")


def parseNumber(string: str):
    matches = re.findall(r'\b\d{1,2}\b', string)
    return int(matches[0]) if len(matches) == 1 else None