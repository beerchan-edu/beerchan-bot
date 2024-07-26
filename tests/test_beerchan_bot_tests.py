from app.command_handler import CommandHandler
from unittest.mock import AsyncMock, Mock
import pytest



def test_parseNumber():
    cmd_handler = CommandHandler()
    test_cases = {
        "I made workout for 5 mins": 5,
        "57 minutes": 57,
        "I made workout for 575 mins": 575,
        "5678 minutes": False,
        "1 hour 30 mins": False,
        "20m": 20,
        "10 minutes and 5 seconds": False,
        "Sentense without digits": False,
        "": False,
        "567883625327": False,
        "5 10 15 375": False
    }
    for input_text, expected_output in test_cases.items():
        assert cmd_handler.parseNumber(input_text) == expected_output


@pytest.mark.asyncio
async def test_help_command():
    cmd_handler = CommandHandler()
    update = Mock()
    context = Mock()
    update.message.reply_text = AsyncMock()

    await cmd_handler.help_command(update, context)

    help_text = (
        "Here are the available commands:\n"
        "/start - Start the bot and get a welcome message\n"
        "/help - Get information about available commands\n"
        "/save <message> - Save your workout message (duration in minutes)\n"
        "/top - Show the top sportsmen for the last 30 days\n"
    )
    update.message.reply_text.assert_called_once_with(help_text)


@pytest.mark.asyncio
async def test_hello_command():
    cmd_handler = CommandHandler()
    update = Mock()
    context = Mock()
    update.effective_user.name = "TestUser"
    update.message.reply_text = AsyncMock()

    await cmd_handler.hello_command(update, context)

    update.message.reply_text.assert_called_once_with("Hi TestUser! I write your workout duration only in minutes.")