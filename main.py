import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from admin import admin_router
from math_hand import math_router
from geo_hand import geo_router
from user_hand import user_router

import database
from keyboards import get_main_menu_kb




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
    await message.answer(
        "Привет! Нажми на кнопку:",
        reply_markup=get_main_menu_kb(message.from_user.id, ADMIN_ID)
    )



async def main():
    database.init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())