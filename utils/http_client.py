import httpx
import random
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from typing import Dict, Any

logger = logging.getLogger(__name__)

# 지터를 포함한 커스텀 wait 함수
def wait_exponential_with_jitter(multiplier=1, jitter_max=1.0):
    def custom_wait(retry_state):
        base = wait_exponential(multiplier=multiplier)(retry_state)
        jitter = random.uniform(0, jitter_max)
        return base + jitter
    return custom_wait

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential_with_jitter(multiplier=1, jitter_max=1.0)
    )
    async def get(self, params: Dict[str, Any]) -> dict:
        params["appid"] = self.api_key
        logger.info(f"appid: {self.api_key}")
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params)
            # change log level
            logger.info(f"[Weather API] Response: {response.text}")
            response.raise_for_status()
            return response.json()
