import pytest
from service.weather_cache import WeatherCache
import time

def test_cache_set_and_get():
    cache = WeatherCache(ttl=2)
    cache.set("Seoul", {"temp": 25})
    assert cache.get("Seoul") == {"temp": 25}
    time.sleep(2.1)
    assert cache.get("Seoul") is None
