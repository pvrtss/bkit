from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from resources.config import States
import dbworker
import markups
from aiogram.dispatcher.filters import Text
from aiogram import types
from resources.messages import MESSAGES
from request import get_exchange_rate
import babel.numbers as bab

# Выбираем криптовалюту (STATE_FROM_CURRENCY -> STATE_TO_CURRENCY)
async def handle_crypto(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    bot = call.bot
    await bot.delete_message(call.from_user.id, call.message.message_id)
    from_currency = call.data.split('_')[1]
    dbworker.set(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"), from_currency)
    print(await state.get_state())
    await States.state_to_currency.set()
    print(await state.get_state())
    await bot.send_message(
        call.from_user.id, 
        text=MESSAGES[await state.get_state()].format(dbworker.get(dbworker.make_key(call.from_user.id, "FROM_CURRENCY"))), 
        parse_mode="Markdown",
        reply_markup=markups.to_menu
    )

