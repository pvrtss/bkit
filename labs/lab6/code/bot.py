from resources.config import TOKEN, States
from aiogram.dispatcher.filters.state import State, StatesGroup
from resources.messages import MESSAGES
import logging
from request import get_exchange_rate
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import markups
from handlers.common import register_message_handlers
from handlers.callback_queries import register_callback_query_handlers


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    register_message_handlers(dp)
    register_callback_query_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
