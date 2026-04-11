from aiogram import Router, types, F
import os
from dotenv import load_dotenv

load_dotenv()
admin_router = Router()
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

@admin_router.message(F.photo, F.from_user.id == ADMIN_ID)
async def get_photo_id(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"ID\n<code>{file_id}</code>", parse_mode="HTML")

@admin_router.message(F.text.contains("Админка"), F.from_user.id == ADMIN_ID)
async def admin_info(message: types.Message):
    await message.answer("🛠 Режим админа")