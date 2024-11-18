import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest

from mobile.utils.downloader import VideoHandler
from mobile.utils.validators import url_validator


LIST_VIDEOS = [
    "https://youtu.be/qzOlJX3H--Q?si=6o735aGUGbN2-ZCZ",
    "https://youtu.be/ISKwApr2Zw0?si=5MXgrewRdaYqpjjr",
    "https:///ISKwApr2Zw0?si=5MXgrewRdaYqpjjr"
]

class VideoHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.video_test = VideoHandler(LIST_VIDEOS[0])
        return super().setUp()

    def test_streams_raise_error_if_link_is_not_validated_or_acess(self):
        self.video_test = VideoHandler(LIST_VIDEOS[2])
        with self.assertRaises(Exception):
            self.video_test.streams
    
    def test_property_get_title_return_a_str(self):
        self.assertIsInstance(self.video_test.get_title, str)

    def test_property_get_thumbnail_url_return_a_str(self):
        self.assertIsInstance(self.video_test.get_thumbnail_url, str)

    def test_raise_error_if_url_value_is_not_str(self):
        with self.assertRaises(AssertionError):
            url_validator(1)

    def test_raise_false_if_url_value_is_not_validated(self):
        self.assertEqual(url_validator(LIST_VIDEOS[2]), False)

    def test_raise_true_if_url_value_is_validated(self):
        self.assertEqual(url_validator(LIST_VIDEOS[0]), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)