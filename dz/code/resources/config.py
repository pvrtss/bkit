from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = "***"

CRYPTO_API_TOKEN = "***"

db_file = "resources/db.vdb"

class States(StatesGroup):
    state_start = State()
    state_from_currency = State()
    state_to_currency = State()
    state_choice = State()
    state_result = State()

'''
class States(Helper):
    mode = HelperMode.snake_case

    STATE_START = ListItem()
    STATE_FROM_CURRENCY = ListItem()
    STATE_TO_CURRENCY = ListItem()
    STATE_CHOICE = ListItem()
    STATE_RESULT= ListItem()
'''