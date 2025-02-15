from pydantic_settings import BaseSettings, SettingsConfigDict # type: ignore
from dotenv import load_dotenv  # type: ignore


class settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings():
    return settings()