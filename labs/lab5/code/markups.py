from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=2)
btnBTC = InlineKeyboardButton(text="💸Bitcoin", callback_data="btnBTC")
btnETH = InlineKeyboardButton(text="💰Ethereum", callback_data="btnETH")

menu.insert(btnBTC)
menu.insert(btnETH)
