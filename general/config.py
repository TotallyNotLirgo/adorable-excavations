from functools import lru_cache
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    LOG_LEVEL: str
    LOG_FILE: str
    CONSOLE_ENABLED: bool

    WINDOW_WIDTH: int
    WINDOW_HEIGHT: int
    WINDOW_NAME: str
    TILE_SIZE: int
    SCALE: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_config() -> Config:
    return Config()