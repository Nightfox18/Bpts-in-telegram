import random

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from keyboards import reply

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import CheckForDigit

router = Router()


@router.message(CommandStart(), IsAdmin(984892023))
async def start(message: Message) -> None:
    await message.answer("Hello, AIOgram 3.x", reply_markup=reply.main)

@router.message(Command("pay"), CheckForDigit())
async def pay_the_order(message: Message, command: CommandObject) ->None:
    await message.answer("Вы успешно оплатили товар!")


@router.message(Command(commands=["rn", "random-number"])) # /rn 1-100
async def get_random_number(message: Message, command: CommandObject) ->None:
    a, b = [int(n) for n in command.args.split("-")]
    rnum = random.randint(a, b)

    await message.reply(f"Random number: {rnum}")


@router.message(Command("test"))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, "test")