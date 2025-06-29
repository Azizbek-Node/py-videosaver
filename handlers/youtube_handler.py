from aiogram import Router, types
from services.youtube import download_youtube_video

youtube_router = Router()

@youtube_router.message()
async def handle_youtube(message: types.Message):
    if "youtube.com" in message.text or "youtu.be" in message.text:
        path = download_youtube_video(message.text)
        await message.answer_video(types.FSInputFile(path))
