import os

from pydantic import BaseSettings

DIR_PATH = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    port: str
    root_dir: str = DIR_PATH

    log_level: str = 'INFO'

    class Config:
        env_file = DIR_PATH + '/../.env'


settings = Settings()
