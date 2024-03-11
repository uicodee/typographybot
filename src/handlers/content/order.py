import math

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.helpers.data import price, get_sheet_price, get_lacquer_price, format_number
from src.keyboards.default import confirm_keyboard, list_type_keyboard
from src.keyboards.inline import confirmation_keyboard
from src.states import OrderForm

router = Router()


@router.message(OrderForm.width)
async def get_width(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            text="⚠️ Илтимос сон киритинг"
        )
    else:
        if int(message.text) > 113:
            await message.answer(
                text="⚠️ Илтимос 113 дан катта сон киритманг"
            )
        elif int(message.text) < 62:
            await message.answer(
                text="⚠️ Илтимос 62 дан кичик сон киритманг"
            )
        else:
            await state.update_data(width=int(message.text))
            await message.answer(
                text=(
                    "Ўлчамларни киритинг (см)\n"
                    "<b>Бўйи (длина):</b>"
                )
            )
            await state.set_state(OrderForm.height)


@router.message(OrderForm.height)
async def get_height(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            text="⚠️ Илтимос сон киритинг"
        )
    else:
        if int(message.text) > 82:
            await message.answer(
                text="⚠️ Илтимос 82 дан катта сон киритманг"
            )
        elif int(message.text) < 46:
            await message.answer(
                text="⚠️ Илтимос 46 дан кичик сон киритманг"
            )
        else:
            await state.update_data(height=int(message.text))
            await message.answer(
                text="Буюртма тиражини киритинг (шт):"
            )
            await state.set_state(OrderForm.count)


@router.message(OrderForm.count)
async def get_count(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            text="⚠️ Илтимос сон киритинг"
        )
    else:
        if int(message.text) < 1000:
            await message.answer(
                text="⚠️ Илтимос 1000 дан кичик сон киритманг"
            )
        else:
            await state.update_data(count=int(message.text))
            await message.answer(
                text="Қоғозга лак ишлатилсинми?",
                reply_markup=confirm_keyboard()
            )
            await state.set_state(OrderForm.lacquer)


@router.message(OrderForm.lacquer, F.text.in_(["Ха", "Йўқ"]))
async def get_lacquer(message: types.Message, state: FSMContext):
    lacquer = True if message.text == "Ха" else False
    await state.update_data(lacquer=lacquer)
    await message.answer(
        text="Қоғоз турини танланг",
        reply_markup=list_type_keyboard()
    )
    await state.set_state(OrderForm.list_type)


@router.message(OrderForm.list_type, F.text.in_(["STANDART LC4 145±5 гр", "ECONOM LC3 145±5 гр"]))
async def get_list_type(message: types.Message, state: FSMContext):
    data = await state.get_data()
    width, height, count = map(int, (data.get('width'), data.get('height'), data.get('count')))
    lacquer = bool(data.get('lacquer'))
    list_type = message.text
    list_price = price.get(list_type)
    order_type = "4+L" if lacquer else "4+0"
    per_list_price = math.ceil(round(0.145 * ((width * height) / 10000) * list_price, 2))
    plate = 300_000
    print_price = get_sheet_price(count, width, height)
    lacquer_print_price = get_lacquer_price(count, width, height)
    palette = math.ceil(count / 8000)
    print_total_price = count * print_price
    lacquer_total_price = count * lacquer_print_price if lacquer else 0
    list_total_price = per_list_price * count
    tooling_price = per_list_price * 200
    palette_packaging_price = palette * 70_000
    total_price = plate + print_total_price + lacquer_total_price + list_total_price + tooling_price + palette_packaging_price
    m = await message.answer(text="⌛️", reply_markup=ReplyKeyboardRemove())
    await m.delete()
    text = (
        f"<b>Буюртма ўлчами:</b> {width} x {height} см\n"
        f"<b>Тираж:</b> {format_number(count)} шт\n"
        f"<b>Буюртма тури:</b> {order_type}\n"
        f"<b>Қоғоз тури:</b> {list_type}\n"
        f"<b>1 лист қоғоз нархи:</b> {per_list_price} сум/лист\n\n"
        f"<b>Пластина:</b> 4 шт х 75 000 сум = <b>{format_number(plate)} сум</b>\n"
        "——————————————————\n"
        f"<b>Печать:</b> {format_number(count)} шт х {print_price} сум = <b>{format_number(print_total_price)} сум</b>\n"
        f"<b>Pantone 1:</b> {format_number(count)} шт х 0 сум = <b>0 сум</b>\n"
        f"<b>Pantone 2:</b> {format_number(count)} шт х 0 сум = <b>0 сум</b>\n"
        f"<b>Лак:</b> {format_number(count)} шт х {lacquer_print_price if lacquer else 0} сум = <b>{format_number(lacquer_total_price)} сум</b>\n"
        f"——————————————————\n"
        f"<b>Қоғоз нархи (листда):</b>\n"
        f"{format_number(count)} шт х {per_list_price} сум = <b>{format_number(list_total_price)} сум</b>\n"
        f"<b>Приладка:</b> 200 шт х {per_list_price} сум = <b>{format_number(tooling_price)} сум</b>\n"
        f"——————————————————\n"
        f"<b>Паллета+Упаковка:</b> {palette} шт х 70 000 сум = <b>{format_number(palette_packaging_price)} сум</b>\n\n"
        f"<b>Доставка по Узбекистану:</b> <u><b>Бесплатно</b></u>\n"
        f"====================================\n"
        f"<b>ЖАМИ: {format_number(total_price)} сум</b> <em>(ҚҚС билан)</em>"
    )
    await message.answer(text=text, reply_markup=confirmation_keyboard())
    await state.clear()

