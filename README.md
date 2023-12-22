#YouTube Downloader

Este projeto consiste em dois scripts Python separados para baixar vídeos e áudios do YouTube.

Características
Download de Vídeo: Baixa vídeos do YouTube em formato MP4.
Download de Áudio: Baixa a faixa de áudio de vídeos do YouTube e a converte para formato MP3.
Pré-requisitos
Antes de começar, certifique-se de ter o Python instalado em sua máquina. Este projeto foi testado com o Python 3.8, mas deve ser compatível com versões mais recentes.

Instalação
Clone o repositório para sua máquina local:
git clone https://github.com/IgorMacedo4/downloader-mp4-e-mp3-youtube-python.git
cd downloader-mp4-e-mp3-youtube-python

Instale as dependências necessárias:
pip install -r requirements.txt

Como Usar
Download de Vídeo
Para baixar um vídeo do YouTube, execute o script download_video.py com a URL do vídeo como argumento:
python download_video.py [URL do vídeo]
O vídeo será baixado no diretório especificado no script.

Download de Áudio
Para baixar apenas o áudio de um vídeo do YouTube, execute o script download_audio.py com a URL do vídeo como argumento:
python download_audio.py [URL do vídeo]
O áudio será baixado e convertido para MP3 no diretório especificado no script.

Configuração
Você pode modificar os scripts para alterar o diretório de destino dos downloads ou outras configurações.
