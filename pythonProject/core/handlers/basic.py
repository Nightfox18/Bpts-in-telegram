from aiogram import Bot
from aiogram.types import Message

async def get_start (message: Message, bot):
    await bot.send_message(message.from_user.id, f"<b>Привет {message.from_user.first_name}. Рад тебя видеть</b>") #Сообщение от бота
    await message.answer(f"<s>Привет {message.from_user.first_name}. Рад тебя видеть</s>") # Ответ на сообщнеи
    await message.reply(f"<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть</tg-spoiler>") # Ответ с указанием сообщения на которое ответил бот

async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Отлично. Ты отправил ищображение, я сохраню его себе:)")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

