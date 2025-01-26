import re
from datetime import timedelta

from app.db import Session
from app.models import Sport
from telegram import Update
from telegram.ext import ContextTypes


class CommandHandler:
    """
    CommandHandler class handles the commands sent to the Beerchan Bot on Telegram.
    """

    def __init__(self):
        """
        Initializes the CommandHandler class.
        Currently, it does not perform any specific initialization.
        """
        pass

    async def hello_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Sends a welcome message to the user when the /start command is issued.

        Args:
            update (Update): An instance of Update, which contains information about the incoming update.
            context (ContextTypes.DEFAULT_TYPE): An instance of ContextTypes.DEFAULT_TYPE, which provides context for the command.
        """
        user = update.effective_user.name
        welcome_message = (
            f"Hi {user}! Welcome to the Beerchan Bot.\n\n"
            "I'm here to help you track and manage your workout durations. You can save your workout time and compete with others in your chat group.\n\n"
            "Here are some commands to get you started:\n"
            "/help - Get information about available commands\n"
            "/save <message> - Save your workout message (duration in minutes)\n"
            "/top - Show the top sportsmen for the last 30 days in this chat\n\n"
            "Remember, the top rankings are specific to each chat, so you can compete with your friends and "
            "see who stays the most active. Let's get started and stay fit together!"
        )
        await update.message.reply_text(welcome_message)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Sends a message with information about available commands when the /help command is issued.

        Args:
            update (Update): An instance of Update, which contains information about the incoming update.
            context (ContextTypes.DEFAULT_TYPE): An instance of ContextTypes.DEFAULT_TYPE, which provides context for the command.
        """
        help_text = (
            "Here are the available commands:\n"
            "/start - Start the bot and get a welcome message\n"
            "/help - Get information about available commands\n"
            "/save <message> - Save your workout message (duration in minutes)\n"
            "/top - Show the top sportsmen for the last 30 days\n"
        )
        await update.message.reply_text(help_text)

    async def save_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Saves the workout message when the /save <message> command is issued.

        Args:
            update (Update): An instance of Update, which contains information about the incoming update.
            context (ContextTypes.DEFAULT_TYPE): An instance of ContextTypes.DEFAULT_TYPE, which provides context for the command.
        """
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

    async def show_best_sportsman(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """
        Displays the top sportsmen for the last 30 days in the chat when the /top command is issued.

        Args:
            update (Update): An instance of Update, which contains information about the incoming update.
            context (ContextTypes.DEFAULT_TYPE): An instance of ContextTypes.DEFAULT_TYPE, which provides context for the command.
        """
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
                        row_message = (
                            f"{number}. {result.nickname} {hours}h {minutes}m\n"
                        )
                        result_message += row_message
                    await update.message.reply_text(result_message)
                else:
                    await update.message.reply_text(
                        "No workout records found for the last 30 days."
                    )

    @staticmethod
    def parse_number(user_string: str):
        """
        Parses the workout duration from the message text.

        Args:
            user_string (str): A string containing the user's message.

        Returns:
            int: The workout duration as an integer if exactly one number is found, otherwise False.
        """
        matches = re.findall(r"\d{1,3}", user_string)
        return int(matches[0]) if len(matches) == 1 else False
