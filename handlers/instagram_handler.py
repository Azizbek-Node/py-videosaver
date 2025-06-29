from aiogram import Router, types, F
from services.instagram import download_instagram_video

instagram_router = Router()

@instagram_router.message(F.text.lower().contains("instagram.com"))
async def handle_instagram_link(message: types.Message):
    url = message.text.strip()
    await message.reply("⏳ Yuklab olinmoqda...")

    try:
        video_url = await download_instagram_video(url)
        await message.reply_video(video_url, caption="✅ Instagram videosi!")
    except Exception as e:
        await message.reply(f"❌ Instagram xatosi: {e}")
