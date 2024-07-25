import logging
from command_handler import CommandHandler as TGCommandHandler
from app.db import engine, Base, Session
from telegram.ext import (
    Application,
    CommandHandler,
)
from consts import TELEGRAM_KEY


Base.metadata.create_all(engine)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

cmd_handler = CommandHandler()


def main():

    print("Starting bot")
    app = Application.builder().token(TELEGRAM_KEY).build()

    app.add_handler(CommandHandler("hello", cmd_handler.hello_command))
    app.add_handler(CommandHandler("help", cmd_handler.help_command))
    app.add_handler(CommandHandler("save", cmd_handler.save_message))
    app.add_handler(CommandHandler("top", cmd_handler.show_best_sportsman))


    print("Polling")
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
