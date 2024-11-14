import unittest

from utils.downloader import VideoHandler
from utils.validators import url_validator


class VideoHandlerTestCase(unittest.TestCase):
    def setUp(self):
        _LIST_VIDEOS = [
            "https://youtu.be/ISKwApr2Zw0?si=5MXgrewRdaYqpjjr"
        ]
        self.video_test = VideoHandler(_LIST_VIDEOS[0])
        return super().setUp()
    
    def raise_error_if_url_value_is_not_str(self):
        with self.assertRaises(AssertionError):
            url_validator('')


if __name__ == "__main__":
    unittest.main(verbosity=2)
