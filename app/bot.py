import logging
from command_handler import (
    hello_command,
    save_message,
    show_best_sportsman,
    update_username,
)
from db import engine, Base, Session
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


def main():

    print("Starting bot")
    app = Application.builder().token(TELEGRAM_KEY).build()

    app.add_handler(CommandHandler("hello", hello_command))
    app.add_handler(CommandHandler("save", save_message))
    app.add_handler(CommandHandler("top", show_best_sportsman))
    app.add_handler(CommandHandler("update_username", update_username))

    print("Polling")
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
