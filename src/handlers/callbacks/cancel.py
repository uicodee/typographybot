from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.keyboards.default import main_menu_keyboard

router = Router()


@router.callback_query(F.data == "cancel_actions")
async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(
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