from aiogram.fsm.state import StatesGroup, State


class OrderForm(StatesGroup):

    width = State()
    height = State()
    count = State()
    lacquer = State()
    list_type = State()


class DataForm(StatesGroup):

    full_name = State()
    phone_number = State()
