import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Request

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exception_handler import register_exception_handlers
from app.core.logger import configure_logging
from app.middleware.request_id import RequestIDMiddleware

configure_logging()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application started")
    yield
    logger.info("Application stopped")


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,)
    app.add_middleware(RequestIDMiddleware)
    register_exception_handlers(app)
    app.include_router(api_router)
    return app


app = create_app()



@app.get("/health")
async def health():
    logger.info("Health endpoint called")

    return {
        "status": "UP",
        "service": settings.app_name,
        "version": settings.app_version,
    }
    
@app.get("/debug")
async def debug(request: Request):
    return {
        "path": request.url.path,
        "url": str(request.url)
    }

@app.get("/")
async def default():
    logger.info("defuult endpoint called")

    return {
        "status": "UP default",
        "service": settings.app_name,
        "version": settings.app_version,
    }