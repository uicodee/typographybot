from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def confirm_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="Ха"
    )
    builder.button(
        text="Йўқ"
    )
    return builder.as_markup(resize_keyboard=True)
