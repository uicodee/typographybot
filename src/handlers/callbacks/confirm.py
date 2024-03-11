from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.keyboards.default import main_menu_keyboard
from src.keyboards.inline import cancel_keyboard
from src.keyboards.inline.confirm import ConfirmCallbackData
from src.states import DataForm

router = Router()


@router.callback_query(ConfirmCallbackData.filter())
async def confirm_query(callback: types.CallbackQuery, callback_data: ConfirmCallbackData, state: FSMContext):
    msg = callback.message.html_text
    await state.update_data(msg=msg)
    if callback_data.action == "confirm":
        await callback.message.answer(
            text="Буюртма бериш учун ташкилот номи ва исмингизни киритинг",
            reply_markup=cancel_keyboard()
        )
        await state.set_state(DataForm.full_name)
    elif callback_data.action == "cancel":
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
