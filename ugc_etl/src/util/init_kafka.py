import logging
from aiokafka.errors import KafkaError
from aiokafka.admin import AIOKafkaAdminClient, NewTopic

from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_topic(admin_client):
    try:
        topic = NewTopic(
            name=settings.topic,
            num_partitions=settings.partitions,
            replication_factor=settings.replication_factor,
            topic_configs={
                "min.insync.replicas": settings.replicas,
                "retention.ms": settings.time_to_retain_data
            }
        )
        await admin_client.create_topics([topic])
        logger.info(f'Topic {settings.topic} created successfully')
    except KafkaError as e:
        logger.error(f'Error: {e}')


async def init_kafka():
    admin_client = AIOKafkaAdminClient(
        bootstrap_servers=settings.kafka_brokers[0],
    )
    try:
        await admin_client.start()
        await create_topic(admin_client)
    finally:
        await admin_client.close()
