import importlib
import pkgutil
from fastapi import APIRouter

router = APIRouter()

# 현재 디렉토리에서 모든 모듈을 찾아서
package_name = __name__

for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{package_name}.{module_name}")
    if hasattr(module, "router"):
        # 각 모듈의 router를 include
        router.include_router(module.router)
