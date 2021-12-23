from behave import given, then
import babel.numbers as bab
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from resources.config import CRYPTO_API_TOKEN
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