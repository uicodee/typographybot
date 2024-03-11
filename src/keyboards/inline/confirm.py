from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ConfirmCallbackData(CallbackData, prefix="confirm"):

    action: str


def confirmation_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="✅ Буюртма бериш",
        callback_data=ConfirmCallbackData(action="confirm")
    )
    builder.button(
        text="❌ Бекор қилиш",
        callback_data=ConfirmCallbackData(action="cancel")
    )
    builder.adjust(1)
    return builder.as_markup()
