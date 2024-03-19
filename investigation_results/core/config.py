from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    clickhouse_host: str = Field(env='CLICKHOUSE_HOST')

    vertica_host: str = Field(env='VERTICA_HOST')
    vertica_port: int = Field(env='VERTICA_PORT')
    vertica_user: str = Field(env='VERTICA_USER')
    vertica_password: str = Field(default='', env='VERTICA_HOST')
    vertica_db: str = Field(env='VERTICA_DB')

    class Config:
        env_file = '../.env'


settings = Settings()
