from pytube import YouTube

class VideoHandler:
    def __init__(self, link: str):
        self._yt = YouTube(link)

    def video_download(self):
        ...

    def audio_download(self):
        ...

    def playlist_download(self):
        ...

    @property
    def get_title(self) -> str:
        return self._yt.title