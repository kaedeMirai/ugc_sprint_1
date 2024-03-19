from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    fastapi_host: str = Field(alias="FASTAPI_HOST")
    fastapi_port: int = Field(alias="FASTAPI_PORT")

    kafka_brokers: list = Field(alias="KAFKA_BROKERS")


settings = Settings()
