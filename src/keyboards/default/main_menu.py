from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="Буюртмани ҳисоблаш"
    )
    return builder.as_markup(resize_keyboard=True)
