import requests
import re

class VideoHandler:
    def __init__(self, link: str):
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        self._url = link
        self._output_file = "videos-downloads"

    def video_download(self) -> bool:
        response = requests.get(self.streams, stream=True)
        if response.status_code == 200: 
            with open(f"{self.get_title}.mp4", 'wb') as file:
                pass

    def audio_download(self) -> bool:
        return True

    def playlist_download(self) -> bool:
        return True
    
    @property
    def streams(self):
        response = requests.get(self._url, headers=self.__headers)

        if response.status_code != 200: raise Exception(f"Erro ao acessar o youtube. Code: {response.status_code}")
        
        video_data = re.search(r'"url":"(https.*?mime=video.*?)"', response.text)
        if not video_data: raise Exception("Não foi possivel encontrar URL do video.")

        video_stream_url = video_data.group(1).replace("\\u0026", "&")
        return video_stream_url

    @property
    def get_title(self) -> str:
        return self._url
    
    @property
    def get_thumbnail_url(self) -> str:
        return self._url
    