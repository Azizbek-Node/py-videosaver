from aiogram import Router, types
from services.instagram import download_instagram_content

instagram_router = Router()

@instagram_router.message()
async def handle_instagram(message: types.Message):
    if "instagram.com" in message.text:
        try:
            video_url = await download_instagram_content(message.text)
            await message.answer_video(video_url)
        except Exception as e:
            print("❌ Instagram xatosi:", str(e))
            await message.answer(f"Instagram videoni yuklab bo‘lmadi.\nXato: {str(e)}")
