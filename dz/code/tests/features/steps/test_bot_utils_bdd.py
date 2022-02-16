from behave import given, then
from request import get_exchange_rate
from number_format import cformat


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
