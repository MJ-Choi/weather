import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_weather_batch():
    response = client.post("/weather/batch", json={"cities": ["London"]})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print(f"response: {response.json()}")
