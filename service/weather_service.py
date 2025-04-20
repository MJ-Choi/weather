from service.weather_cache import WeatherCache
from utils.http_client import HTTPClient
from dto.weather import WeatherData
from typing import List
import asyncio

class WeatherService:
    def __init__(self, client: HTTPClient, cache: WeatherCache):
        self.client = client
        self.cache = cache

    async def get_weather(self, city: str) -> WeatherData:
        # 캐시된 데이터가 있으면 반환
        cached = self.cache.get(city)
        if cached:
            return WeatherData(city=city, data=cached)

        try:
            params = {"q": city}
            data = await self.client.get(params)
            self.cache.set(city, data)
            return WeatherData(city=city, data=data)
        except Exception as e:
            return WeatherData(city=city, data={"error": str(e)})

    async def get_batch_weather(self, cities: List[str]) -> List[WeatherData]:
        self.cache.reset()  # 배치 기준 TTL 리셋
        return await asyncio.gather(*(self.get_weather(city) for city in cities))