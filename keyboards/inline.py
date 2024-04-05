from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://youtu.be/@fsoky"),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=fsoky_community")
        ]
    ]
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text="Подписаться", url="https://t.me/fsoky_community")
        ]
    ]
)