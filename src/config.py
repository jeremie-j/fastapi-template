from functools import cache
from os import getenv
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "prod"]
    DATABASE_URL: str


@cache
def get_settings():
    config_name = getenv("CONFIG_NAME")
    return Settings(env_file=f".{config_name}.env", ENVIRONMENT=config_name)
