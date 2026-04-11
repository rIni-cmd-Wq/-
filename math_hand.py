from aiogram import Router, types, F

from database import get_topic_by_callback, add_exp_smart

from keyboards import get_math_topic_kb, get_al_topic_kb
from keyboards import get_geo_topic_kb, get_geo_topic2_kb

#list
from fill_db import GEO_LICT1


math_router = Router()

#handlers reply
@math_router.message(F.text == "📚 Математика")
async def math_reply(message: types.Message):
    await message.answer("Выберите раздел:", reply_markup=get_math_topic_kb())

#handlers Inline
@math_router.callback_query(F.data == "math")
async def math_topic1(message: types.Message):
    await message.edit_text("Выберите раздел:", reply_markup=get_math_topic_kb())
    await message.answer()



# algebra
@math_router.callback_query(F.data == "math_al")
async def al_topic2(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите тему:", reply_markup=get_al_topic_kb())
    await callback.answer()

# geometry
@math_router.callback_query(F.data == "math_geo")
async def geo_topic(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите раздел:", reply_markup=get_geo_topic_kb())
    await callback.answer()

@math_router.callback_query(F.data == "math_geo_topic_tri")
async def geo_topic2(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите тему:", reply_markup=get_geo_topic2_kb())
    await callback.answer()



# handlers
@math_router.callback_query(F.data.startswith(("al_", "geo_")))
async def list(callback: types.CallbackQuery):
    if callback.data in GEO_LICT1:
        photos = GEO_LICT1[callback.data]
        for photo in photos:
            await callback.message.answer_photo(photo)
        add_exp_smart(callback.from_user.id, 5)
        return await callback.answer()

    data = get_topic_by_callback(callback.data)
    if data:
        topic_name, photo_id = data
        add_exp_smart(callback.from_user.id, 5)
        await callback.message.answer_photo(
            photo=photo_id,
            caption=f"✅ Тема: {topic_name}\n🌟 Тебе начислено +5 опыта!"
        )
    else:
        await callback.message.answer("Эта шпора еще в разработке 🛠")

    await callback.answer()