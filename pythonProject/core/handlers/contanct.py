from aiogram.types import Message
from aiogram import Bot

async def get_true_contacn(message: Message, bot: Bot, phone: str):
    await message.answer(f"Ты отправил <b>свой</b> контакт {phone}")

async def get_fake_contacn(message: Message, bot: Bot):
    await message.answer(f"Ты отправил <b>чужой</b> контакт")