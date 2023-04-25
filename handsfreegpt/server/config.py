from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    environment: str = ""
    cors_allow_origins: List[str] = []  # eg ["http://localhost:3000"]

    def __getitem__(self, item):
        return getattr(self, item)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
