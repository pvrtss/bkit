import babel.numbers as bab
import unittest
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from config import CRYPTO_API_TOKEN
import json


def get_exchange_rate(crypto, curr):
    url = "https://min-api.cryptocompare.com/data/price"
    parameters = {"fsym": crypto, "tsyms": curr, "api_key": CRYPTO_API_TOKEN}

    session = Session()

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data[curr]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    finally:
        session.close()


def cformat(number: float, currency: str):
    return bab.format_currency(number, currency, locale="ru_RU")

class TestBotUtilities(unittest.TestCase):
    def test_cformat(self):
        self.assertEqual(cformat(1000, "RUB"), "1 000,00 ₽")
        self.assertEqual(cformat(1000, "USD"), "1 000,00 $")

    def test_get_exchange_rate(self):
        self.assertGreater(get_exchange_rate("BTC", "USD"), 30000)
        self.assertLess(get_exchange_rate("BTC", "USD"), 70000)


if __name__ == "__main__":
    unittest.main()




print(cformat(1000, "UAH"))