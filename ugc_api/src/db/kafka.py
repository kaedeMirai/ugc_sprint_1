from aiokafka import AIOKafkaProducer

import json

from api.v1.schemas import NewMessage
from core.settings import settings
from db.base_broker import BaseBroker


class KafkaBroker(BaseBroker):

    async def __aenter__(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka_brokers,
        )
        await self.producer.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.producer.stop()

    async def send(self, topic: str, message: NewMessage) -> None:
        await self.producer.send(
            topic=topic,
            key=message.key.encode("utf-8"),
            value=str(json.dumps(message.value)).encode("utf-8")
        )


def get_kafka_broker():
    return KafkaBroker()
