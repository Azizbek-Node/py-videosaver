import yt_dlp

def download_youtube_video(url: str) -> str:
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        info = ydl.extract_info(url, download=False)
        return f"downloads/{info['title']}.mp4"
