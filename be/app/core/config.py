import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = 'FASTAPI BASE'
    SECRET_KEY: str
    API_PREFIX: str = '/v1'
    BACKEND_CORS_ORIGINS: List[str] = ['*']
    SQL_DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7
    SECURITY_ALGORITHM: str = 'HS256'
    logging_config_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logging.ini'))

    model_config = SettingsConfigDict(
        env_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env')),
        extra='forbid'  # This is default. Helps catch misnamed env vars
    )


settings = Settings()
