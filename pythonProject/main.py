from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command, CommandStart

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот остановлен")

async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(leceltime)s] - %(name)s -"
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    #dp.message.register(get_start, Command(commands=['start', 'run']))
    #dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())