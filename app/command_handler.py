from app.db import Session
from app.models import Sport
from telegram import Update
from telegram.ext import ContextTypes
import re
from datetime import timedelta

class CommandHandler:
    def __init__(self):
        pass

    async def hello_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user.name
        await update.message.reply_text(f"Hi {user}! I write your workout duration only in minutes.")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = (
            "Here are the available commands:\n"
            "/start - Start the bot and get a welcome message\n"
            "/help - Get information about available commands\n"
            "/save <message> - Save your workout message (duration in minutes)\n"
            "/top - Show the top sportsmen for the last 30 days\n"
        )
        await update.message.reply_text(help_text)

    async def save_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        with Session() as session:
            with session.begin():
                user = update.effective_user.name
                message_text = update.message.text
                digits = self.parse_number(message_text)
                if digits is not False:
                    message_text = re.sub(
                        r"/save\s+|/save@KhargolGroBogukBot\s+", "", message_text
                    )
                    add_message = Sport(
                        nickname=user,
                        user_id=str(update.effective_user.id),
                        chat_id=str(update.effective_chat.id),
                        duration=timedelta(minutes=digits),
                        message=message_text,
                    )
                    session.add(add_message)
                    await update.message.reply_text(f"I saved your result, {user}")
                else:
                    await update.message.reply_text(
                        "Write a command in correct format only in minutes: mm"
                    )

    async def show_best_sportsman(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        with Session() as session:
            with session.begin():
                chat_id = str(update.effective_chat.id)
                results = Sport.best_query(session, chat_id)
                if results:
                    number = 0
                    result_message = "TOP best sportsmen for the last 30 days:\n"
                    for result in results:
                        number += 1
                        total_seconds = result.total_duration.total_seconds()
                        hours = int(total_seconds // 3600)
                        minutes = int((total_seconds % 3600) // 60)
                        row_message = f"{number}. {result.nickname} {hours}h {minutes}m\n"
                        result_message += row_message
                    await update.message.reply_text(f"{result_message}")
                else:
                    await update.message.reply_text("No workout records found for the last 30 days.")

    @staticmethod
    def parse_number(user_string: str):
        matches = re.findall(r"\d{1,3}", user_string)
        return int(matches[0]) if len(matches) == 1 else False
