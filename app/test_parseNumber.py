from command_handler import parseNumber
import pytest


def test_parseNumber_single_digit():
    assert parseNumber("I made workout for 5 mins") == 5

def test_parseNumber_two_digits():
    assert parseNumber("57 minutes") == 57

def test_parseNumber_single_digit_with_text_after():
    assert parseNumber("5minutes") is None

def test_parseNumber_two_digits_with_text_after():
    assert parseNumber("57minutes") is None

def test_parseNumber_single_digit_with_text_before():
    assert parseNumber("I made workout for5 mins") is None

def test_parseNumber_two_digits_with_text_before():
    assert parseNumber("I made workout for57 mins") is None

def test_parseNumber_single_digit_with_text_around():
    assert parseNumber("I made workout for5mins") is None

def test_parseNumber_two_digits_with_text_around():
    assert parseNumber("I made workout for57mins") is None

def test_parseNumber_more_than_two_digits():
    assert parseNumber("I made workout for 579 mins") is None
    assert parseNumber("I made workout for 5791 mins") is None

def test_parseNumber_multiply_matches():
    assert parseNumber("I made workout for 57, 1.") is None
    assert parseNumber("I made workout for 1 hour and 57 minutes") is None

def test_parseNumber_no_match():
    assert parseNumber("I made workout fifty seven minutes") is None