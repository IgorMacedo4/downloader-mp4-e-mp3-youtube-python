import os
from pytube import YouTube

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first()
    stream.download(output_path=output_path)

if __name__ == "__main__":
    video_url = "link_aqui"  # Insira o ID do vídeo do YouTube
    downloaded_video_path = "/caminho/para/salvar/downloader/"


    # Download the video
    download_video(video_url, downloaded_video_path)