import babel.numbers as bab

def cformat(number: float, currency: str):
    return bab.format_currency(number, currency, locale="ru_RU")