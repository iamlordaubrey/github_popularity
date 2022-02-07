import httpx
import asynctest
import pytest

from fastapi import status
from unittest.mock import patch

from app.server import app
from test.utils.constants import INVALID_URLS, VALID_URLS


class MainTest(asynctest.TestCase):
    async def test_post_to_index_with_invalid_url(self):
        async with httpx.AsyncClient(app=app, base_url="http://test") as async_client:
            for url in INVALID_URLS:
                response = await async_client.post('/', data={'url': url})
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.asyncio
    @patch('httpx.AsyncClient.get')
    async def test_post_to_index_with_valid_url(self, mock_response):
        response = httpx.Response(status_code=200, text='{"id": 1, "watchers": 500, "forks": 50}')
        mock_response.return_value = response

        async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
            for url in VALID_URLS:
                response = await ac.post("/", data={'url': url})
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIn('score', response.text)
