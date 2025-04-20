from pydantic_settings import BaseSettings
from pydantic import Field

class EnvSettings(BaseSettings):
    log_level: str = "INFO"
    openweather_api_key: str  = Field(..., env="OPENWEATHER_API_KEY")# OpenWeather API 키
    openweather_api_url: str  = Field(..., env="OPENWEATHER_API_URL") # 기본 API URL
    batch_ttl: int = Field(..., alias="BATCH_DURATION_SEC") # 배치 시간

    class Config:
        env_file = ".env"  # 환경변수 파일 설정
        env_file_encoding = "utf-8"

settings = EnvSettings()