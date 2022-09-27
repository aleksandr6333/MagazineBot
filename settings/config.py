import os
from emoji import emojize


TOKEN = '5437617243:AAETf80Sxlrh1iJB450U5H1FyrX0J2VLSuC'

NAME_DB = 'products.sqlite'

VERSION = '0.0.1'

AUTHOR = 'User'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

COUNT = 0

KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_ballon: О магазине'),
    'SETTINGS': emojize(':⚙️Настройки:'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize(':rewind:⏪'),
    '>>': emojize(':fast_forward:⏩'),
    'BACK_STEP': emojize(':arrow_backward:◀'),
    'NEXT_STEP': emojize(':arrow_forward:▶'),
    'ORDER': emojize(':ok_hand:✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize(':arrow_down:🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize(':arrow_up:🔼'),
    'APPLAY': emojize('✅ Оформить заказ'),
    'COPY': emojize(':U+00A9:©️'),
}

CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ice_cream': 3,
    }

COMMANDS = {
    'START': "start",
    'HELP': "help",
}