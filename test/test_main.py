import unittest

from app.utils.validators import url_validator


class UtilsTestCase(unittest.TestCase):
    def test_url_validator_with_invalid_urls(self):
        invalid_urls = ['https://www.google.com/', 'localhost', 'a', '1']

        for url in invalid_urls:
            self.assertFalse(url_validator(url))

    def test_url_validator_with_valid_urls(self):
        valid_urls = [
            'https://github.com/freeCodeCamp/freeCodeCamp',
            'https://github.com/sindresorhus/awesome',
            'https://github.com/vuejs/vue',
        ]

        for url in valid_urls:
            self.assertTrue(url_validator(url))
