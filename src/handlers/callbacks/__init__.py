from aiogram import Dispatcher
from .confirm import router as confirm_router
from .cancel import router as cancel_router


def setup(dp: Dispatcher):
    dp.include_router(cancel_router)
    dp.include_router(confirm_router)