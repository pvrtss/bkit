import babel.numbers as bab
import unittest
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from ..request import get_exchange_rate
from ..number_format import cformat
import json


def cformat(number: float, currency: str):
    return bab.format_currency(number, currency, locale="ru_RU")

class TestBotUtilities(unittest.TestCase):
    def test_cformat(self):
        self.assertEqual(cformat(1000, "RUB"), "1 000,00 ₽")
        self.assertEqual(cformat(1000, "USD"), "1 000,00 $")

    def test_get_exchange_rate(self):
        self.assertGreater(get_exchange_rate("BTC", "USD"), 30000)
        self.assertLess(get_exchange_rate("BTC", "USD"), 70000)


if __name__ == "__main__":
    unittest.main()