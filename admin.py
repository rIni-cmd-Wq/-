from aiogram import Router, types, F
import os

admin_router = Router()

ADMIN_ID = (os.getenv("ADMIN_ID"))

@admin_router.message(F.text ==  "⚙️ Админка", F.from_user.id == ADMIN_ID)
async def admin(message: types.Message):
    await message.answer("🛠 Режим админа! Пришли фото, и я выдам его ID.")

@admin_router.message(F.photo,  F.from_user.id == ADMIN_ID)
async def photo_id(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"ID твоей шпоры:\n<code>{file_id}</code>", parse_mode="HTML")
