from aiokafka import AIOKafkaConsumer
from core.config import settings


class KafkaReader:

    async def __aenter__(self):
        self.consumer = AIOKafkaConsumer(
            settings.topic,
            bootstrap_servers=settings.kafka_brokers,
            group_id=settings.group_id,
            auto_offset_reset='earliest',
            enable_auto_commit=False
        )

        await self.consumer.start()
        return self

    async def read(self, batch_size: int = 10):
        messages = []

        async for message in self.consumer:
            messages.append(message)

            if len(messages) >= batch_size:
                yield messages
                messages.clear()

    async def commit(self):
        await self.consumer.commit()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.consumer.stop()
