import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    LabeledPrice,
    PreCheckoutQuery,
)

from config import BOT_TOKEN
from keyboards import menu_kb, buy_kb

VPN_LINK = "https://raw.githubusercontent.com/s68181791-bit/-santizz/main/LTE.txt"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать!\n\n"
        "Здесь можно приобрести VPN для обхода белых списков.",
        reply_markup=menu_kb(),
    )


@dp.message(F.text == "🔌 Купить VPN")
async def buy(message: Message):
    await message.answer(
        "🌐 Обход белых списков\n\n"
        "💰 Стоимость: 150 ⭐",
        reply_markup=buy_kb(),
    )


@dp.message(F.text == "👤 Личный кабинет")
async def profile(message: Message):
    await message.answer(
        "У вас пока нет активной подписки."
    )


@dp.message(F.text == "💬 Поддержка")
async def support(message: Message):
    await message.answer(
        "@your_support"
    )


@dp.callback_query(F.data == "buy")
async def invoice(callback: CallbackQuery):
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title="VPN",
        description="Обход белых списков",
        payload="vpn",
        currency="XTR",
        prices=[
            LabeledPrice(
                label="VPN",
                amount=150
            )
        ]
    )

    await callback.answer()


@dp.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery):
    await query.answer(ok=True)


@dp.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.answer(
        "✅ Спасибо за покупку!\n\n"
        "Ваша ссылка:\n\n"
        f"{VPN_LINK}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())