from unittest import TestCase

from app.utils.helpers import validate_url, validate_operands, calculate_score
from test.utils.constants import INVALID_URLS, VALID_URLS, INVALID_OPERANDS, VALID_OPERANDS, OPERANDS_AND_SCORE_LIST


class HelpersTestCase(TestCase):
    def test_validate_url_with_invalid_urls(self):
        for url in INVALID_URLS:
            self.assertFalse(validate_url(url)[0])

    def test_validate_url_with_valid_urls(self):
        for url in VALID_URLS:
            self.assertTrue(validate_url(url)[0])

    def test_validate_operands_with_invalid_operands(self):
        for operand in INVALID_OPERANDS:
            self.assertFalse(validate_operands(operand))

    def test_validate_operands_with_valid_operands(self):
        for operand in VALID_OPERANDS:
            self.assertTrue(validate_operands(operand))

    def test_calculate_score(self):
        for operand in OPERANDS_AND_SCORE_LIST:
            self.assertEqual(calculate_score(operand[0], operand[1])[0], operand[2])
