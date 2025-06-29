def is_youtube(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url

def is_tiktok(url: str) -> bool:
    return "tiktok.com" in url or "vt.tiktok.com" in url

def is_instagram(url: str) -> bool:
    return "instagram.com" in url
