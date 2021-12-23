from behave import given, then
import babel.numbers as bab
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


@given("Crypto currency is {crypto}, to currency is {curr}")
def have_convert_params(context, crypto, curr):
    context.crypto = crypto
    context.curr = curr


@then("Result must be between {from_curr} and {to}")
def expect_result(context, from_curr, to):
    assert get_exchange_rate(context.crypto, context.curr) > float(from_curr)
    assert get_exchange_rate(context.crypto, context.curr) < float(to)

@given("Number is {number}, currency is {curr}")
def have_convert_params(context, number, curr):
    context.number = number
    context.curr = curr


@then("Result must be _{result}_")
def expect_result(context, result):
    assert cformat(float(context.number), context.curr) == result
