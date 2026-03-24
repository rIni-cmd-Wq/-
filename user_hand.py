from aiogram import Router, types, F
from database import get_user_stats

user_router=Router()

@user_router.message(F.text == "👤 Мой профиль")
async def show_profile(message: types.Message):
    stats = get_user_stats(message.from_user.id)

    if stats:
        exp, level = stats
        text=(
            f"👤 **Профиль: {message.from_user.first_name}**\n"
            f"━━━━━━━━━━━━━━\n"
            f"🌟 **Твой опыт:** {exp}\n"
            f"🆙 **Твой уровень:** {level}\n"
            f"━━━━━━━━━━━━━━\n"
            f"💡 Каждая шпора дает +5 опыта!"
        )
    else:
        text="❌ Ошибка: Нажми /start, чтобы создать профиль!"
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ В меню", callback_data="math")

    await message.answer(text, reply_markup=kb.as_markup(), parse_mode="Markdown")


