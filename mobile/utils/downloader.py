import requests
import re

class VideoHandler:
    def __init__(self, link: str):
        self.yt = link

    def video_download(self) -> bool:
        return True

    def audio_download(self) -> bool:
        return True

    def playlist_download(self) -> bool:
        return True

    @property
    def get_title(self) -> str:
        return self.yt
    
    @property
    def get_thumbnail_url(self) -> str:
        return self.yt
    
