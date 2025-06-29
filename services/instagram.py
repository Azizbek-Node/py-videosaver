import httpx

async def download_instagram_video(post_url: str) -> str:
    api_url = "https://saveig.app/api/ajaxSearch"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest"
    }

    data = {
        "q": post_url,
        "t": "media",
        "lang": "en"
    }

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.post(api_url, data=data, headers=headers)
            response.raise_for_status()
            result = response.json()

        if not result.get("links"):
            raise Exception("Instagram videosi topilmadi.")

        return result["links"][0]["url"]  # 1-video link

    except Exception as e:
        print(f"❌ Instagram xatosi: {e}")
        raise Exception("Instagramdan video yuklab bo‘lmadi.")
