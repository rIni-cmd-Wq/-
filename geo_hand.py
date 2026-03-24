from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

geo_router = Router()

@geo_router.callback_query(F.data == "math_geo")
async def math_geo(callback: types.CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="🔺 Треугольники", callback_data="math_tri")
    kb.button(text="🔳 Площадь", callback_data="math_area")
    kb.button(text="⬅️ Назад", callback_data="back_to_subjects")
    kb.adjust(1)
    await callback.message.edit_text("выберите раздел:", reply_markup=kb.as_markup())
    await callback.answer()

@geo_router.callback_query(F.data == "math_tri")
async def math_tri(callback: types.CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="📐 Прям. △", callback_data="geo_tri2")
    kb.button(text="🔺 Равноб. и равност. △", callback_data="geo_tri3")
    kb.button(text="🌀 Общие свойства", callback_data="geo_sv")
    kb.button(text="⬅️ Назад", callback_data="math_geo")
    kb.adjust(1)
    await callback.message.edit_text("выберите тему:", reply_markup=kb.as_markup())
    await callback.answer()

