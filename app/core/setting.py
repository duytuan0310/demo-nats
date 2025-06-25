import os
from functools import lru_cache
from pydantic import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    """Settings """
    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "")
    NATS_SERVER_URL: str = os.getenv("NATS_SERVER_URL", "nats://localhost:4222")
    DATABASE_URI: str = os.getenv("DATABASE_URI","")
@lru_cache()
def get_settings() -> Settings:
    """Get settings"""
    return Settings()
settings = get_settings()