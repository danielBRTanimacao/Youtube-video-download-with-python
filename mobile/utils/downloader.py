from pytube import YouTube
from pytube.exceptions import PytubeError

class VideoHandler:
    def __init__(self, link: str):
        self.yt = YouTube(link)

    def video_download(self) -> bool:
        return True

    def audio_download(self) -> bool:
        return True

    def playlist_download(self) -> bool:
        return True

    @property
    def get_title(self) -> str:
        try:
            return self.yt.title
        except PytubeError as error:
            return f"titulo: Error ao buscar titulo\ndetalhe: Não foi possivel carregar o titulo do video\nerro: {error}"
    
    @property
    def get_thumbnail_url(self) -> str:
        return self.yt.thumbnail_url
    
