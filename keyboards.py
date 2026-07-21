from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import PRICE


def menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔌 Купить VPN")],
            [KeyboardButton(text="👤 Личный кабинет")],
            [KeyboardButton(text="💬 Поддержка")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )


def buy_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"⭐ Купить за {PRICE} Stars",
                    callback_data="buy"
                )
            ]
        ]
    )


def admin_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📊 Статистика"),
                KeyboardButton(text="👥 Пользователи")
            ],
            [
                KeyboardButton(text="📢 Рассылка")
            ],
            [
                KeyboardButton(text="💰 Изменить цену"),
                KeyboardButton(text="🔗 Изменить ссылку")
            ],
            [
                KeyboardButton(text="🏠 Главное меню")
            ]
        ],
        resize_keyboard=True
    )


def back_menu():
    return menu_kb()