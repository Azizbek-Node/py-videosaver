import httpx

async def download_instagram_content(url: str) -> str:
    api_url = f"https://tiklydown.com/api/ig?url={url}"

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(api_url)

        try:
            result = response.json()
        except Exception:
            print("❌ JSON formatda javob yo‘q:", response.text[:300])
            raise Exception("API JSON formatda javob qaytarmadi.")

        print("✅ TiklyDown javobi:", result)

        if not result.get("status") or not result.get("media"):
            raise Exception("Instagram videosi topilmadi.")

        return result["media"]
