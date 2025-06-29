import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.instagram_handler import instagram_router

load_dotenv()
bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()
dp.include_router(instagram_router)

async def main():
    print("🚀 Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
