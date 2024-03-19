from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    kafka_brokers: list = Field(env='KAFKA_BROKERS')
    clickhouse_brokers: list = Field(env='CLICKHOUSE_BROKERS')

    bootstrap_servers: str = Field(env='BOOTSTRAP_SERVERS')
    group_id: str = Field(env='GROUP_ID')
    topic: str = Field(env='TOPIC')
    partitions: int = Field(env='PARTITIONS')
    replicas: int = Field(env='REPLICAS')
    replication_factor: int = Field(env='REPLICATION_FACTOR')
    time_to_retain_data: str = Field(env='TIME_TO_RETAIN_DATA')

    class Config:
        env_file = '../.env'


settings = Settings()
