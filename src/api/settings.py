import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class DbSettings(BaseSettings):
    db_host: str = os.getenv("POSTGRES_HOST")
    db_port: str = os.getenv("POSTGRES_PORT")
    db_name: str = os.getenv("POSTGRES_DB")
    db_user: str = os.getenv("POSTGRES_USER")
    db_password: str = os.getenv("POSTGRES_PASSWORD")

    POSTGRES_URL: str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


class Settings(BaseSettings):
    """
    All api settings
    """
    db: DbSettings = DbSettings()


settings = Settings()
