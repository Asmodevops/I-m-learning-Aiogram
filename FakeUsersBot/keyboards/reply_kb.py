from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON


get_users_button: KeyboardButton = KeyboardButton(
    text=LEXICON['get_users'],
)

get_posts_button: KeyboardButton = KeyboardButton(
    text=LEXICON['get_posts']
)


down_kb_builder = ReplyKeyboardBuilder()
down_kb_builder.row(get_users_button, get_posts_button, width=1)

down_kb: ReplyKeyboardMarkup = down_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)


