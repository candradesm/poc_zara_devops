url = "https://suno.com/song/0c6ba4ed-b27c-43fa-aa23-917b62763d69"
song_id = url.split("/")[-1]

cdn_url = f"https://cdn1.suno.ai/{song_id}.mp3"

print(cdn_url)