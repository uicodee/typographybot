from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from src.keyboards.default import main_menu_keyboard
from src.keyboards.default.phone import phone_keyboard
from src.states import DataForm

router = Router()


@router.message(DataForm.full_name)
async def get_fullname(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer(
        text="Телефон рақамингизни юборинг",
        reply_markup=phone_keyboard()
    )
    await state.set_state(DataForm.phone_number)


@router.message(DataForm.phone_number, F.contact)
async def get_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer(
        text="Буюртмангиз қабул қилинди! \nТез орада сизга алоқага чиқамиз.",
        reply_markup=main_menu_keyboard()
    )
    await message.bot.send_message(
        chat_id=-4142607325,
        text=data.get('msg') + "\n\n" + "<b>Буюртмачи:\n\n</b>" + data.get('full_name') + "\n" + message.contact.phone_number
    )
