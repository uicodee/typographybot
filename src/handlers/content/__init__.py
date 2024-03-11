from aiogram import Dispatcher

from .order import router as order_router
from .data import router as data_router


def setup(dp: Dispatcher):
    dp.include_router(order_router)
    dp.include_router(data_router)
