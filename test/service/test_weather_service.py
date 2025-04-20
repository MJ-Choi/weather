import pytest
from unittest.mock import MagicMock
from service.weather_service import WeatherService
from service.weather_cache import WeatherCache
from utils.http_client import HTTPClient
from config.setting import settings

@pytest.mark.asyncio
async def test_weather_service_cache_miss():
    # Mocking HTTPClient
    client = MagicMock(spec=HTTPClient)
    client.get.return_value = {"weather": "sunny"}

    # Mocking Cache
    cache = WeatherCache(ttl=settings.batch_ttl)
    service = WeatherService(client, cache)

    # Testing cache miss (cache is empty)
    data = await service.get_weather("New York")
    assert data.city == "New York"
    assert "weather" in data.model_dump()['data']
    client.get.assert_called_once_with({"q": "New York"})  # Ensure the client was called

@pytest.mark.asyncio
async def test_weather_service_cache_hit():
    # Mocking the HTTP client
    client = MagicMock(spec=HTTPClient)

    # Pre-populate the cache with data
    cache = WeatherCache(ttl=settings.batch_ttl)
    cache.set("New York", {"weather": "sunny"})

    service = WeatherService(client, cache)

    # Testing cache hit (data is already cached)
    data = await service.get_weather("New York")
    assert data.city == "New York"
    assert "weather" in data.model_dump()['data']
    client.get.assert_not_called()  # Ensure the client was not called since cache hit
