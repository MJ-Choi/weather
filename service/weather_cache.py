import time
from typing import Dict, Tuple

class WeatherCache:
    def __init__(self, ttl: int = 600):
        self.ttl = ttl  # Time-To-Live
        self.cache: Dict[str, Tuple[float, dict]] = {}  # 캐시 저장소

    def get(self, key: str):
        data = self.cache.get(key)
        if data and time.time() - data[0] < self.ttl:
            return data[1]
        return None

    def set(self, key: str, value: dict):
        self.cache[key] = (time.time(), value)

    def reset(self):
        self.cache.clear()