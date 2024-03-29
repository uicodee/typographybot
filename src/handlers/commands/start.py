from aiogram import Router, types
from aiogram.filters import CommandStart

from src.infrastructure.database.dao import HolderDao
from src.keyboards.default import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao):
    await message.answer(
        text=(
            "Буюртмангиз ўлчамлари ва тираж сонини киритиб, "
            "сотув менежерига мурожаат қилмасдан буюртма нархини ҳисоблашингиз мумкин.\n\n"
            "Офсет машина модели: Komori 644-L\n"
            "Максимал қоғоз ўлчами: 82 х 113 см\n"
            "Минимал қоғоз ўлчами: 46 х 62 см\n\n"
            "Максимал босиш майдони: 81 х 112 см"
        ),
        reply_markup=main_menu_keyboard()
    )
