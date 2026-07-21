from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔌 Купить VPN")],
            [KeyboardButton(text="👤 Личный кабинет")],
            [KeyboardButton(text="💬 Поддержка")],
        ],
        resize_keyboard=True,
    )


def buy_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⭐ Купить за 150 Stars",
                    callback_data="buy",
                )
            ]
        ]
    )