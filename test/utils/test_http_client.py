import pytest

from utils.http_client import HTTPClient
from config.setting import EnvSettings

@pytest.mark.asyncio
async def test_httpclient_get_success():
    settings = EnvSettings()
    client = HTTPClient(settings.openweather_api_url, settings.openweather_api_key)
    result = await client.get({"q": "Seoul"})
    assert "weather" in result
