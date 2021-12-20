from resources.config import ERR_MESSAGE, TOKEN, START_MESSAGE, REPLY_MESSAGE
import logging
from request import get_exchange_rate
from aiogram import Bot, Dispatcher, executor, types
import markups

API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.answer(
        START_MESSAGE, parse_mode="Markdown", reply_markup=markups.menu
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(ERR_MESSAGE, parse_mode="Markdown", reply_markup=markups.menu)


@dp.callback_query_handler(text="btnBTC")
async def get_BTC_rate(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(
        message.from_user.id,
        REPLY_MESSAGE.format("💸Bitcoin", get_exchange_rate("BTC", "RUB")),
        parse_mode="Markdown",
        reply_markup=markups.menu,
    )


@dp.callback_query_handler(text="btnETH")
async def get_ETH_rate(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(
        message.from_user.id,
        REPLY_MESSAGE.format("💰Ethereum", get_exchange_rate("ETH", "RUB")),
        parse_mode="Markdown",
        reply_markup=markups.menu,
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
