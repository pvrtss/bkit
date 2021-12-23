from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = "5054956358:AAE1OEv-NgcsB0iq0osEU0v57vdRG6LyJg0"

CRYPTO_API_TOKEN = "5f6385cb156e90c3e4c9a892b6c1516ecd507b019bcd7483cd1ff8ed8e288339"

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