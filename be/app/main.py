from fastapi import FastAPI
import uvicorn
from fastapi_sqlalchemy import DBSessionMiddleware
from app.api.router import router
from app.core.config import settings
from starlette.middleware.cors import CORSMiddleware

from app.helpers.exception_handler import CustomException, http_exception_handler

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, docs_url="/docs", redoc_url="/re-docs",
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description='''
            API for App Management System.
        ''',

    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(DBSessionMiddleware, db_url=settings.SQL_DATABASE_URL)
    application.include_router(router, prefix=settings.API_PREFIX)
    application.add_exception_handler(CustomException, http_exception_handler)

    return application

app = get_application()
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)