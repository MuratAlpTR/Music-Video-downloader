# Kütüphanemizi Uzantı indirmek için --> pip install youtube_dl

# MuratAlpTR Proje tarafından geliştirilmiş

import youtube_dl

music_url = input('Video link : ')

video_bilgisi = youtube_dl.YoutubeDL().extract_info(
    url = music_url,download=False)

##############################################################################

# Müzik format geçerli :  
# "AAC", "ALAC", "AIFF", "FLAC", "MP3", "M4A", "OPUS", "VORBIS", "WAV"

dosya_adi = f"{video_bilgisi['title']}.ALAC"


##############################################################################


ayarlar={
    'format':'bestaudio/best',
    'keepvideo': False,
    'outtmpl': dosya_adi,
}


with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_bilgisi['webpage_url']])

    
print(f"İndirme tamamlandı... {dosya_adi}")