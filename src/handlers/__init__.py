from aiogram import Dispatcher

from src.handlers import commands, buttons, content, callbacks


def setup(dp: Dispatcher):
    commands.setup(dp)
    buttons.setup(dp)
    content.setup(dp)
    callbacks.setup(dp)
