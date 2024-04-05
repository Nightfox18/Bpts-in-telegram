from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from keyboards.inline import sub_channel

class CheckSubscripton (BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@fsoky_community", event.from_user.id)

        if chat_member.status == "left":
            await event.answer(
                "Подпишись на канал чтобы пользоваться ботом!",
                reply_markup=sub_channel
            )
        else:
            return await handler(event, data)