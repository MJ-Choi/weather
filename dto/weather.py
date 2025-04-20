from pydantic import BaseModel, Field
from typing import List, Dict, Any

class CityList(BaseModel):
    cities: List[str] = Field(..., example=["Seoul", "New York", "Tokyo"], description="조회할 도시 이름 목록")

class WeatherData(BaseModel):
    city: str = Field(..., example="Seoul", description="도시 이름")
    data: Dict[str, Any] = Field(..., description="OpenWeatherMap API로부터 받은 원시 날씨 데이터")
