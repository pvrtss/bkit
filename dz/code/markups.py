from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu =InlineKeyboardMarkup(row_width=1)
btnStart = InlineKeyboardButton(text="✅Начать", callback_data="btnStart")

start_menu.insert(btnStart)

from_menu = InlineKeyboardMarkup(row_width=2)
btn_BTC = InlineKeyboardButton(text="🪙Bitcoin", callback_data="btn_BTC")
btn_ETH = InlineKeyboardButton(text="💰Ethereum", callback_data="btn_ETH")
btn_XRP = InlineKeyboardButton(text="💸XRP", callback_data="btn_XRP")
btn_SOL = InlineKeyboardButton(text="🤑Solana", callback_data="btn_SOL")

from_menu.insert(btn_BTC)
from_menu.insert(btn_ETH)
from_menu.insert(btn_XRP)
from_menu.insert(btn_SOL)

to_menu = InlineKeyboardMarkup(row_width=2)
btn_USD = InlineKeyboardButton(text="💵USD", callback_data="btn_USD")
btn_RUB = InlineKeyboardButton(text="🇷🇺RUB", callback_data="btn_RUB")
btn_EUR = InlineKeyboardButton(text="💶EUR", callback_data="btn_EUR")
btn_UAH = InlineKeyboardButton(text="🇺🇦UAH", callback_data="btn_UAH")
btn_back_from = InlineKeyboardButton(text="Назад", callback_data="btn_back_from")

to_menu.insert(btn_USD)
to_menu.insert(btn_RUB)
to_menu.insert(btn_EUR)
to_menu.insert(btn_UAH)
to_menu.insert(btn_back_from)

choice_menu = InlineKeyboardMarkup(row_width=1)
btn_back_crypto = InlineKeyboardButton(text="Назад к выбору криптовалюты", callback_data="btn_crypto")
btn_back_curr =  InlineKeyboardButton(text="Назад к выбору валюты для конвертации", callback_data="btn_curr")
btn_result = InlineKeyboardButton(text="Показать результат", callback_data="btn_result")

choice_menu.insert(btn_result)
choice_menu.insert(btn_back_crypto)
choice_menu.insert(btn_back_curr)

final_menu = InlineKeyboardMarkup(row_width=1)
btn_retry = InlineKeyboardButton(text="Обновить курс", callback_data="btn_retry")
btn_finish =  InlineKeyboardButton(text="Завершить/Начать заново", callback_data="btn_finish")

final_menu.insert(btn_retry)
final_menu.insert(btn_finish)

help_menu = InlineKeyboardMarkup(row_width=1)
btn_accept = InlineKeyboardButton(text="Понятно", callback_data="accept")

help_menu.insert(btn_accept)
