from aiogram.fsm.state import StatesGroup, State


class BroadcastState(StatesGroup):
    waiting_text = State()


class PriceState(StatesGroup):
    waiting_price = State()


class LinkState(StatesGroup):
    waiting_link = State()