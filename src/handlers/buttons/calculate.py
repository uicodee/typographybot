from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.keyboards.default import list_type_keyboard
from src.states import OrderForm

router = Router()


@router.message(F.text == "Буюртмани ҳисоблаш")
async def calculate(message: types.Message, state: FSMContext):
    await message.answer(
        text=(
            "Ўлчамларни киритинг (см)\n"
            "<b>Эни, формати (ширина):</b>"
        )
    )
    await state.set_state(OrderForm.width)
