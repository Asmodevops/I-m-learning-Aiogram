from aiogram.types import Message


def start_filter(message: Message) -> bool:
    return message.text == '/start'


def help_filter(message: Message) -> bool:
    return message.text == '/help'


def command_users_filter(message: Message) -> bool:
    return message.text == '/users'


def command_posts_filter(message: Message) -> bool:
    return message.text == '/posts'