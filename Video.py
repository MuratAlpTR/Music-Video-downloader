# Kütüphanemizi Uzantı indirmek için --> pip install youtube_dl

# MuratAlpTR Proje tarafından geliştirilmiş

import youtube_dl

video_url = input("Video link giriniz:")

video_bilgisi = youtube_dl.YoutubeDL().extract_info(
    url=video_url, download=False)


with youtube_dl.YoutubeDL() as ydl:
    ydl.download([video_bilgisi['webpage_url']])


print(f"İndirme tamamlandı... {video_bilgisi}")
