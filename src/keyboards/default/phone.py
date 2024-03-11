from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def phone_keyboard() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📞 Телефон рақамини юбориш", request_contact=True))
    return builder.as_markup(resize_keyboard=True)
