import httpx

async def download_tiktok_video(url: str) -> str:
    api = f"https://www.tikwm.com/api/?url={url}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        result = response.json()
        return result["data"]["play"]
