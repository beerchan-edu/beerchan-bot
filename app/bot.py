from asyncio import run
from command_handler import hello_command, save_message, test_result
from db import async_engine, Base
from telegram.ext import (
    Application,
    CommandHandler,
)
from consts import TELEGRAM_KEY

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    print("Creating tables")
    await create_tables()

    print("Starting bot")
    app = Application.builder().token(TELEGRAM_KEY).build()

    app.add_handler(CommandHandler("hello", hello_command))
    app.add_handler(CommandHandler("insert", save_message))
    app.add_handler(CommandHandler("result", test_result))

    print("Polling")
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    run(main())
    # print("Starting bot")
    # app = Application.builder().token(TELEGRAM_KEY).build()

    # # # run(create_tables())
    # # Base.metadata.create_all(async_engine)

    # # commands
    # app.add_handler(CommandHandler("hello", hello_command))
    # app.add_handler(CommandHandler("insert", save_message))
    # app.add_handler(CommandHandler("result", test_result))

    # print("Polling")
    # app.run_polling(poll_interval=3)


