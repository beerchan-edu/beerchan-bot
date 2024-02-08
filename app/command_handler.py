from db import async_session
from models import Sport
from telegram import Update
from telegram.ext import ContextTypes
from sqlalchemy import select


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    await update.message.reply_text(f"Hi {update.effective_user.name}!")


async def save_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async with async_session() as session:
        async with session.begin():
            try:
                await update.message.reply_text("Try write smth")
                message_text = update.message.text
                add_message = Sport(message=message_text)
                add_username = Sport(nickname=update._effective_user.name)  
                session.add_all(add_message, add_username)
            except:
                await session.rollback()
            finally:
                await update.message.reply_text("You fukin did it!")


async def test_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async with async_session() as session:
        async with session.begin():
            active_username = update._effective_user.name
            try:
                stmt = select(Sport).where(Sport.nickname == active_username)
                results = await session.execute(stmt)
                for result in results:
                    await update.message.reply_text(result)
            except:
                session.rollback()
            finally:
                session.commit()    

                

