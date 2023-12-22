import os
from pytube import YouTube
from moviepy.editor import *

def download_audio(url, output_path):
    yt = YouTube(url)

    # Filtrar apenas streams de áudio e selecionar o de maior qualidade
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    # Baixar o stream de áudio
    audio_file = audio_stream.download(output_path=output_path)

    # Converter o arquivo baixado para MP3
    mp3_filename = os.path.join(output_path, yt.title + ".mp3")
    AudioFileClip(audio_file).write_audiofile(mp3_filename)

    # Remover o arquivo original baixado
    os.remove(audio_file)

if __name__ == "__main__":
    video_url = "link_aqui"  # Insira o URL do vídeo do YouTube
    downloaded_audio_path = "/caminho/para/salvar/downloader/"

    # Baixar o áudio do vídeo
    download_audio(video_url, downloaded_audio_path)
