from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message
async def send_echo(message: Message) -> None:
    await message.answer(f'Это эхо! {message.text}')