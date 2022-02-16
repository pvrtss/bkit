# Начало диалога (. -> STATE_START)
from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from resources.config import States
import dbworker
import markups
from resources.messages import MESSAGES
from request import get_exchange_rate
from number_format import cformat


async def cmd_start(message: types.Message, state: FSMContext):
    await States.state_start.set()
    await message.answer(MESSAGES[await state.get_state()], parse_mode="Markdown", reply_markup=markups.start_menu)

async def cmd_cancel(message: types.Message, state: FSMContext):
    if await state.get_state() == None:
        return
    else:
        await state.finish()
        await message.answer(MESSAGES['cancel'], parse_mode="Markdown")

async def cmd_help(message: types.Message, state: FSMContext):
    await message.answer(MESSAGES['help'], parse_mode="Markdown", reply_markup=markups.help_menu)


async def err_handle(message: types.Message, state: FSMContext):
    if await state.get_state() == None:
        return
    current_state = await state.get_state()
    reply_markup = None
    reply_msg = ''
    if current_state == 'States:state_start':
        reply_msg = MESSAGES['err'] + MESSAGES[current_state]
        reply_markup = markups.start_menu
    elif current_state == 'States:state_from_currency':
        reply_msg = MESSAGES['err'] + MESSAGES[current_state]
        reply_markup = markups.from_menu
    elif current_state == 'States:state_to_currency':
        reply_msg = MESSAGES['err'] + MESSAGES[current_state].format(dbworker.get(dbworker.make_key(message.from_user.id, "FROM_CURRENCY")))
        reply_markup = markups.to_menu
    elif current_state == 'States:state_choice':
        reply_msg = MESSAGES['err'] + MESSAGES[current_state].format(
            dbworker.get(dbworker.make_key(message.from_user.id, "FROM_CURRENCY")),
            dbworker.get(dbworker.make_key(message.from_user.id, "TO_CURRENCY"))
        )
        reply_markup = markups.choice_menu
    elif current_state == 'States:state_result':
        from_currency = dbworker.get(dbworker.make_key(message.from_user.id, "FROM_CURRENCY"))
        to_currency = dbworker.get(dbworker.make_key(message.from_user.id, "TO_CURRENCY"))
        result = cformat(float(get_exchange_rate(from_currency, to_currency)), to_currency, locale="ru_RU")
        
        reply_msg = MESSAGES['err'] + MESSAGES[current_state].format(
            from_currency,
            result
        )
        reply_markup = markups.final_menu

    
    await message.answer(reply_msg, parse_mode="Markdown", reply_markup=reply_markup)


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start', 'help'])
    dp.register_message_handler(cmd_cancel, commands=['cancel'], state="*")
    dp.register_message_handler(cmd_help, commands=['help'], state="*")
    dp.register_message_handler(err_handle, state="*")