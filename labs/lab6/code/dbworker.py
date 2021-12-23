from vedis import Vedis
from resources import config


def get(key):
    with Vedis(config.db_file) as db:
        try:
            return db[key].decode() 
        except KeyError:  
            # в случае ошибки значение по умолчанию - начало диалога
            return config.States.S_START.value  


def set(key, value):
    with Vedis(config.db_file) as db:
        try:
            db[key] = value
            return True
        except:
            return False


def make_key(chatid, keyid):
    res = str(chatid) + '__' + str(keyid)
    return res