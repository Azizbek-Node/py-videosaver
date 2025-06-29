from aiogram import Router, types
from services.tiktok import download_tiktok_video

tiktok_router = Router()

@tiktok_router.message()
async def handle_tiktok(message: types.Message):
    if "tiktok.com" in message.text:
        try:
            video = await download_tiktok_video(message.text)
            await message.answer_video(video)
        except Exception:
            await message.answer("TikTok videoni yuklab bo‘lmadi.")
