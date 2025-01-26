import logging
import sys

from app.command_handler import CommandHandler as TGCommandHandler
from app.config import tg_key
from app.db import Base, engine
from telegram.ext import (
    Application,
    CommandHandler,
)

try:
    Base.metadata.create_all(engine)
except Exception as e:
    logging.error(e)
    sys.exit(1)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

cmd_handler = TGCommandHandler()


def main():
    """
    Main function to start the bot.
    This function initializes the bot application, adds command handlers, and starts polling.
    """
    logger.info("Starting bot...")

    if tg_key is None:
        logging.error("Telegram key doesn't exist")
        sys.exit(1)

    app = Application.builder().token(tg_key).build()

    app.add_handler(CommandHandler("start", cmd_handler.hello_command))
    app.add_handler(CommandHandler("help", cmd_handler.help_command))
    app.add_handler(CommandHandler("save", cmd_handler.save_message))
    app.add_handler(CommandHandler("top", cmd_handler.show_best_sportsman))

    print("Polling")

    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
