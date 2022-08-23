import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Settings:
    DATABASE: str = os.getenv("DATABASE")
    TEST_DATABASE: str = os.getenv("TEST_DATABASE")


settings = Settings()
