from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import get_topic_by_callback, add_exp

math_router = Router()

@math_router.callback_query(F.data == "math")
async def math_topis1(callback: types.CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="🧮 Алгебра", callback_data="math_al")
    kb.button(text="📐 Геометрия", callback_data="math_geo")
    kb.button(text="🎲 Вер. и стат.", callback_data="math_ver")
    kb.button(text="⬅️ Назад", callback_data="back_to_subjects")
    kb.adjust(1)
    await callback.message.edit_text("Выберите раздел:", reply_markup=kb.as_markup())
    await callback.answer()

# 4.
@math_router.callback_query(F.data == "math_al")
async def al_topis2(callback: types.CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="📦 ФСУ", callback_data="al_fsy")
    kb.button(text="⚡️ Степени", callback_data="al_step")
    kb.button(text="⚖️ Уравнения", callback_data="al_yrov")
    kb.button(text="⬅️ Назад", callback_data="math")
    kb.adjust(1)
    await callback.message.edit_text("Выберите тему:", reply_markup=kb.as_markup())
    await callback.answer()

@math_router.callback_query(F.data.startswith("al_"))
async def show_shpora(callback: types.CallbackQuery):
    data = get_topic_by_callback(callback.data)
    if data:
        topic_name, photo_id = data
        add_exp(callback.from_user.id, 5)
        await callback.message.answer_photo(
            photo=photo_id,
            caption=f"✅ Тема: {topic_name}\n🌟 Тебе начислено +5 опыта!"
        )
    else:
        await callback.message.answer("Эта шпора еще в разработке 🛠")
        await callback.answer()