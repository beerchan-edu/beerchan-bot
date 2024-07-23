from app.command_handler import parseNumber
import pytest


def test_parseNumber():
    test_cases = {
        "I made workout for 5 mins": 5,
        "57 minutes": 57,
        "I made workout for 575 mins": 575,
        "5678 minutes": False,
        "Sentense without digits": False,
        "1 hour 30 mins": False,
        "20m": 20,
        "10 minutes and 5 seconds": False,
    }
    for input_text, expected_output in test_cases.items():
        assert parseNumber(input_text) == expected_output