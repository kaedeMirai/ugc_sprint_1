import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.router import router as ugc_router
from core.settings import settings


def build_app():
    fast_api_app = FastAPI(
        title='UGC Sprint 1',
        description='UGC api',
        version='1.0.0',
        docs_url='/api/openapi',
        openapi_url='/api/openapi.json',
        default_response_class=ORJSONResponse,
    )

    fast_api_app.include_router(ugc_router, prefix='/api/v1')

    return fast_api_app


app = build_app()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.fastapi_host,
        port=settings.fastapi_port,
        reload=True
    )
