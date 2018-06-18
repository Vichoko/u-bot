# u-cursos html/css targeted parameters
PASSWORD_FIELD_NAME = 'password'
USERNAME_FIELD_NAME = 'username'
LOG_IN_BUTTON_VALUE = 'Ingresar'
SEND_BUTTON_VALUE = 'Guardar'
MESSAGE_INPUT_NAME = "contenido"
CATEGORY_CHOSER_TEXT_INPUT_CSS_CLASS = ".chosen-text"
CATEGORY_CHOSER_ID = "id_tema_chosen"
TITLE_FIELD_NAME = "titulo"

# free game bot settings
# whitelisted email address string
WHITELIST_EMAIL_WORDS = [
    "vicenteoyanedel",
    "ifttt"
]

# whitelisted words
# if message contains any of theese words, then is a free game
WHITELIST_WORDS = [
    "100%",
    "free",
]

# blacklisted words
# if message contains any of these words, then it should be discarded
BLACKLIST_WORDS = [
    "during",
    "weekend",
    "week",
    "drm",
]
# blacklist from 1% to 99%
BLACKLIST_WORDS += ["{}%".format(str(i + 1)) for i in range(99)]

URL_WORD_LIST = [
    "ift.tt",
]
