from copy import deepcopy

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from db.db import users_template, users_db
from filters.filters import start_filter, help_filter, command_users_filter, command_posts_filter
from keyboards.pagination_kb import create_pagination_keyboard
from keyboards.reply_kb import down_kb
from lexicon.lexicon import LEXICON
from services.services import users, posts, get_specific_user, get_specific_posts

router = Router()


@router.message(start_filter)
async def process_start_command(message: Message):
    await message.answer(text=LEXICON[message.text],
                         reply_markup=down_kb)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(users_template)


@router.message(help_filter)
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(command_users_filter)
@router.message(F.text == LEXICON['get_users'])
async def process_show_all_users(message: Message):
    users_db[message.from_user.id]['users_page'] = 1
    text = users[users_db[message.from_user.id]['users_page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'users_backward',
            f'{users_db[message.from_user.id]["users_page"]}/{len(users)}',
            'users_forward'
        )
    )


@router.callback_query(F.data == 'users_forward')
async def process_users_forward_command(callback: CallbackQuery):
    if users_db[callback.from_user.id]['users_page'] < len(users):
        users_db[callback.from_user.id]['users_page'] += 1
        text = users[users_db[callback.from_user.id]['users_page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'users_backward',
                f'{users_db[callback.from_user.id]["users_page"]}/{len(users)}',
                'users_forward'
            )
        )
    await callback.answer()


@router.callback_query(F.data == 'users_backward')
async def process_users_backward_command(callback: CallbackQuery):
    if users_db[callback.from_user.id]['users_page'] > 1:
        users_db[callback.from_user.id]['users_page'] -= 1
        text = users[users_db[callback.from_user.id]['users_page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'users_backward',
                f'{users_db[callback.from_user.id]["users_page"]}/{len(users)}',
                'users_forward'
            )
        )
    await callback.answer()


@router.message(command_posts_filter)
@router.message(F.text == LEXICON['get_posts'])
async def process_show_all_posts(message: Message):
    users_db[message.from_user.id]['posts_page'] = 1
    text = posts[users_db[message.from_user.id]['posts_page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'posts_backward',
            f'{users_db[message.from_user.id]["posts_page"]}/{len(posts)}',
            'posts_forward'
        )
    )


@router.callback_query(F.data == 'posts_forward')
async def process_posts_forward_command(callback: CallbackQuery):
    if users_db[callback.from_user.id]['posts_page'] < len(users):
        users_db[callback.from_user.id]['posts_page'] += 1
        text = posts[users_db[callback.from_user.id]['posts_page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'posts_backward',
                f'{users_db[callback.from_user.id]["posts_page"]}/{len(posts)}',
                'posts_forward'
            )
        )
    await callback.answer()


@router.callback_query(F.data == 'posts_backward')
async def process_posts_backward_command(callback: CallbackQuery):
    if users_db[callback.from_user.id]['posts_page'] > 1:
        users_db[callback.from_user.id]['posts_page'] -= 1
        text = posts[users_db[callback.from_user.id]['posts_page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'posts_backward',
                f'{users_db[callback.from_user.id]["posts_page"]}/{len(posts)}',
                'posts_forward'
            )
        )
    await callback.answer()


@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    await callback.answer()


@router.message(lambda x: '/user ' in x.text and x.text.replace('/user ', '').isdigit())
async def process_show_specific_user(message: Message):
    user_id = message.text.replace('/user ', '')
    text = get_specific_user(user_id)
    await message.answer(
        text=text
    )


specific_posts: dict[int, str] = {}


@router.message(lambda x: '/posts ' in x.text and x.text.replace('/posts ', '').isdigit())
async def process_show_specific_posts(message: Message):
    user_id = message.text.replace('/posts ', '')
    if int(user_id) > len(users):
        await message.answer(
            text='Пользователь с таким ID мне не знаком. Соответственно и постов такого пользователя нет.'
        )
    else:
        global specific_posts
        specific_posts = get_specific_posts(user_id)
        users_db[message.from_user.id]['specific_posts_page'] = 1
        text = specific_posts[users_db[message.from_user.id]['specific_posts_page']]
        await message.answer(
            text=text,
            reply_markup=create_pagination_keyboard(
                'specific_posts_backward',
                f'{users_db[message.from_user.id]["specific_posts_page"]}/{len(specific_posts)}',
                'specific_posts_forward'
            )
        )


@router.callback_query(F.data == 'specific_posts_forward')
async def process_specific_posts_forward_command(callback: CallbackQuery):
    if users_db[callback.from_user.id]['specific_posts_page'] < len(specific_posts):
        users_db[callback.from_user.id]['specific_posts_page'] += 1
        text = specific_posts[users_db[callback.from_user.id]['specific_posts_page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'specific_posts_backward',
                f'{users_db[callback.from_user.id]["specific_posts_page"]}/{len(specific_posts)}',
                'specific_posts_forward'
            )
        )
    await callback.answer()


@router.callback_query(F.data == 'specific_posts_backward')
async def process_specific_posts_backward_command(callback: CallbackQuery):
    if users_db[callback.from_user.id]['specific_posts_page'] > 1:
        users_db[callback.from_user.id]['specific_posts_page'] -= 1
        text = posts[users_db[callback.from_user.id]['specific_posts_page']]
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'specific_posts_backward',
                f'{users_db[callback.from_user.id]["specific_posts_page"]}/{len(specific_posts)}',
                'specific_posts_forward'
            )
        )
    await callback.answer()