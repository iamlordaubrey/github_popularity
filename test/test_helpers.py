import unittest

from app.utils.helpers import validate_url, validate_operands, calculate_score


class HelpersTestCase(unittest.TestCase):
    def test_validate_url_with_invalid_urls(self):
        invalid_urls = [
            'https://www.google.com/',
            'http://github.com/vuejs',
            'localhost',
            'a',
            '1'
        ]

        for url in invalid_urls:
            self.assertFalse(validate_url(url)[0])

    def test_validate_url_with_valid_urls(self):
        valid_urls = [
            'https://github.com/freeCodeCamp/freeCodeCamp',
            'https://github.com/sindresorhus/awesome',
            'https://github.com/vuejs/vue',
        ]

        for url in valid_urls:
            self.assertTrue(validate_url(url)[0])

    def test_validate_operands_with_invalid_operands(self):
        invalid_operands = [
            ('a', 3),
            (None, 2),
            ([3, True, 'a'], 5),
        ]

        for operand in invalid_operands:
            self.assertFalse(validate_operands(operand))

    def test_validate_operands_with_valid_operands(self):
        valid_operands = [
            (1, 3),
            [400, 70],
        ]

        for operand in valid_operands:
            self.assertTrue(validate_operands(operand))

    def test_calculate_score(self):
        list_of_operands = [
            (1, 2, 5),
            (400, 70, 540),
            (1000, 1000, 3000),
        ]

        for operand in list_of_operands:
            self.assertEqual(calculate_score(operand[0], operand[1])[0], operand[2])
