import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from dotenv import load_dotenv
from admin import admin_router
from math_hand import math_router
from geo_hand import geo_router
import database
from user_hand import user_router


load_dotenv()
API_TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_router(admin_router)
dp.include_router(math_router)
dp.include_router(geo_router)
dp.include_router(user_router)



@dp.message(CommandStart())
async def start(message: types.Message):
    database.create_user(message.from_user.id)
    kb = ReplyKeyboardBuilder()
    kb.button(text="📚 Математика")
    kb.button(text="👤 Мой профиль",)
    if message.from_user.id == ADMIN_ID:
        kb.button(text="⚙️ Админка")

    kb.adjust(1)
    await message.answer("Привет! Нажми на кнопку:", reply_markup=kb.as_markup(resize_keyboard=True))
@dp.message(F.text == "📚 Математика")
async def choose_subject(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="📐 Математика", callback_data="math")
    await message.answer("?", reply_markup=kb.as_markup())


async def main():
    database.init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())