import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv(dotenv_path=".env")


class Settings:
    DATABASE: str = os.getenv("DATABASE")
    TEST_DATABASE: str = os.getenv("TEST_DATABASE")


@lru_cache
def get_settings():
    settings = Settings()
    return settings
