from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def list_type_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="STANDART LC4 145±5 гр"
    )
    builder.button(
        text="ECONOM LC3 145±5 гр"
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
