from aiogram import Dispatcher

from .calculate import router as calculate_router


def setup(dp: Dispatcher):
    dp.include_router(calculate_router)
