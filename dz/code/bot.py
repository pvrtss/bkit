
from resources.config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers.common import register_message_handlers
from handlers.callback_queries import register_callback_query_handlers


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

    
if __name__ == "__main__":
    register_message_handlers(dp)
    register_callback_query_handlers(dp)
    dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("cancel", "Отменить текущую операцию")
    ])
    executor.start_polling(dp, skip_updates=True)
