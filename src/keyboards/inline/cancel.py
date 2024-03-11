from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def cancel_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="❌ Бекор қилиш",
        callback_data="cancel_actions"
    )
    return builder.as_markup()
