from fastapi import FastAPI

from config.logging_config import setup_logging
from controller import router as all_routers

# log
setup_logging()

app = FastAPI(
    title="Weather API",
    description="도시별 날씨를 조회하고, 비동기로 배치 처리도 지원하는 FastAPI 기반 API",
    version="1.0.0"
)

# 모든 controllers 내 router를 자동으로 등록
app.include_router(all_routers)
