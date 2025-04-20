from fastapi import APIRouter
from typing import List
from dto.weather import CityList, WeatherData
from service.weather_cache import WeatherCache
from service.weather_service import WeatherService
from utils.http_client import HTTPClient
from config.setting import EnvSettings

# DI 설정
settings = EnvSettings()
client = HTTPClient(
    base_url=settings.openweather_api_url,
    api_key=settings.openweather_api_key
)
cache=WeatherCache(settings.batch_ttl)
weather_service = WeatherService(client, cache)

# 라우터 정의
router = APIRouter(prefix="/weather", tags=["Weather"])

@router.post(
    "/batch",
    summary="도시별 날씨 일괄 조회",
    response_model=List[WeatherData]
)
async def get_weather_batch(cities: CityList):
    return await weather_service.get_batch_weather(cities.cities)
