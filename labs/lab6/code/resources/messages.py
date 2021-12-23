start_message = """
*Привет, пользователь!*

Этот бот позволяет узнать текущий курс самых популярных криптовалют (💸_Bitcoin_,💰_Ethereum_ и др.). 

Для получения курса нажмите на кнопку "Начать" ниже:
"""

from_currency_message = """
Выберите криптовалюту нажатием кнопки ниже: 
"""

err_message = """
*Нет такой команды!*
"""


to_currency_message = """
Выбранная криптовалюта: *{}*

Выберите валюту для конвертации нажатием кнопки ниже: 
"""
    

choice_message = """
Выбранная пара для конвертации: *{}* -> *{}*

Выберите действие нажатием кнопки ниже:
"""

result_message = """
_Текущий курс:_
    
    *1* *{}* -> *{}* 

Выберите действие нажатием кнопки ниже:
"""

cancel_message = '''
*Текущая операция отменена*

Введите /help или /start чтобы начать заново:
'''

help_message = '''
Для отмены текущей операции напишите /cancel

Для продолжения нажмите "Понятно" ниже:
'''

MESSAGES = {
    'States:state_start': start_message,
    'States:state_from_currency': from_currency_message,
    'States:state_to_currency': to_currency_message,
    'States:state_choice': choice_message,
    'States:state_result': result_message,
    'err': err_message,
    'cancel':cancel_message,
    'help': help_message
}