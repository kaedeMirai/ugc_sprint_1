from fastapi import Depends
from api.v1.schemas import NewMessage
from db.base_broker import BaseBroker
from db.kafka import get_kafka_broker


class UgcService:
    async def send(self, topic: str, message: NewMessage):
        async with get_kafka_broker() as broker:
            await broker.send(topic, message)


def get_ugc_service():
    return UgcService()
