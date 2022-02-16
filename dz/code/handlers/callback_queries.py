from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from resources.config import States
import dbworker
import markups
from aiogram.dispatcher.filters import Text
from aiogram import types
from resources.messages import MESSAGES
from request import get_exchange_rate
from number_format import cformat


# Обрабатываем /help
async def handle_help(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Начинаем ввод данных (STATE_START -> STATE_FROM_CURRENCY)
async def handle_start(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await States.state_from_currency.set()
    await bot.send_message(call.from_user.id, text=MESSAGES[await state.get_state()], reply_markup=markups.from_menu, parse_mode="Markdown")


# Выбираем криптовалюту (STATE_FROM_CURRENCY -> STATE_TO_CURRENCY)
async def handle_crypto(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)
    from_currency = call.data.split('_')[1]
    dbworker.set(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"), from_currency)
    await States.state_to_currency.set()
    await bot.send_message(
        call.from_user.id, 
        text=MESSAGES[await state.get_state()].format(dbworker.get(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"))), 
        parse_mode="Markdown",
        reply_markup=markups.to_menu
    )


# Выбираем валюту (STATE_TO_CURRENCY -> STATE_CHOICE)
async def handle_curr(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)
    to_currency = call.data.split('_')[1]
    if to_currency != "back":
        dbworker.set(dbworker.make_key(call.from_user.id, "TO_CURRENCY"), to_currency)
        await States.state_choice.set()
        await bot.send_message(
            call.from_user.id, 
            text=MESSAGES[await state.get_state()].format(
                dbworker.get(dbworker.make_key(call.from_user.id, "FROM_CURRENCY")),
                dbworker.get(dbworker.make_key(call.from_user.id, "TO_CURRENCY"))
            ),
            reply_markup=markups.choice_menu,
            parse_mode="Markdown"
        )
    else:
        await States.state_from_currency.set()
        await bot.send_message(
            call.from_user.id, 
            text="Выберите криптовалюту: ", 
            reply_markup=markups.from_menu,
            parse_mode="Markdown"
        )

# Выбираем действие (STATE_CHOICE -> STATE_RESULT)
async def handle_choice(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)
    choice = call.data.split('_')[1]
    if choice == "result":
        from_currency = dbworker.get(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"))
        to_currency = dbworker.get(dbworker.make_key(call.from_user.id, "TO_CURRENCY"))
        result = cformat(float(get_exchange_rate(from_currency, to_currency)), to_currency)
        await States.state_result.set()
        await bot.send_message(
            call.from_user.id, 
            text=MESSAGES[await state.get_state()].format(
                from_currency,
                result
            ),
            reply_markup=markups.final_menu,
            parse_mode="Markdown"
        )
    else:
        if choice == "crypto":
            await States.state_from_currency.set()
            await bot.send_message(
                call.from_user.id, 
                text=MESSAGES[await state.get_state()], 
                reply_markup=markups.from_menu,
                parse_mode="Markdown"
            )
        else:
            await States.state_to_currency.set()
            await bot.send_message(
                call.from_user.id, 
                text=MESSAGES[await state.get_state()].format(dbworker.get(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"))), 
                reply_markup=markups.to_menu,
                parse_mode="Markdown"
            )

# Финальный выбор
async def handle_result(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)
    choice = call.data.split('_')[1]
    if choice == "retry":
        from_currency = dbworker.get(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"))
        to_currency = dbworker.get(dbworker.make_key(call.from_user.id, "TO_CURRENCY"))
        result = cformat(float(get_exchange_rate(from_currency, to_currency)), to_currency)
        await bot.send_message(
            call.from_user.id, 
            text=MESSAGES[await state.get_state()].format(
                from_currency,
                result
            ),
            reply_markup=markups.final_menu,
            parse_mode="Markdown"
        )
    else:
        await States.state_start.set()
        await bot.send_message(
            call.from_user.id, 
            text=MESSAGES[await state.get_state()],
            reply_markup=markups.start_menu,
            parse_mode="Markdown"
        )


def register_callback_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(handle_start, text="btnStart", state=States.state_start)
    dp.register_callback_query_handler(handle_crypto, Text(startswith="btn"), state=States.state_from_currency)
    dp.register_callback_query_handler(handle_curr, Text(startswith="btn"), state=States.state_to_currency)
    dp.register_callback_query_handler(handle_choice, Text(startswith="btn"), state=States.state_choice)
    dp.register_callback_query_handler(handle_result, Text(startswith="btn"), state=States.state_result)
    dp.register_callback_query_handler(handle_help, text="accept", state='*')
