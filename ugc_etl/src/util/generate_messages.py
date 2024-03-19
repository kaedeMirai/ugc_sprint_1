from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import KafkaError
import asyncio
from time import sleep
import hashlib

import logging
logging.basicConfig(level=logging.INFO)


class CustomPartitioner:
    def __call__(self, key, all_partitions, available):
        key_hash = hashlib.sha1(key.encode('utf-8')).hexdigest()
        partition = int(key_hash, 16) % all_partitions
        return partition


def create_topic(admin_client, topic_name, partitions):
    try:
        topic = NewTopic(
            name=topic_name,
            num_partitions=partitions,
            replication_factor=3,
            topic_configs={
                "min.insync.replicas": 2
            })
        admin_client.create_topics([topic])
        print(f':::::::::::::::{topic_name}')
    except KafkaError as e:
        print(f':::::::::::::::{e}')


async def produce_message(producer, topic, key, value):
    try:
        producer.send(topic=topic, key=key, value=value)
        producer.flush()
        print(f':::::::::::::::{key}')
    except KafkaError as e:
        print(f':::::::::::::::{e}')


async def main():
    kafka_bootstrap_servers = "0.0.0.0:10000"
    topic_name = 'movies'
    partitions = 3

    producer_conf = {'bootstrap_servers': kafka_bootstrap_servers}
    producer = KafkaProducer(**producer_conf)

    admin_client = KafkaAdminClient(bootstrap_servers=kafka_bootstrap_servers)

    # create_topic(admin_client, topic_name, partitions)

    if topic_name not in admin_client.list_topics():
        sleep(4)
    for i in range(20):
        await produce_message(producer, topic_name, b'movie_click', b'{"movie_id": "fb4df957-f3f0-4508-8062-c561d96b3d9a", "user_id": 3600}')
        await produce_message(producer, topic_name, b'trailer_click', b'{"movie_id": "fb4df957-f3f0-4508-8062-c561d96b3d9a", "user_id": 3600}')
        await produce_message(producer, topic_name, b'category_click', b'{"user_id": "3600", "category": "drama"}')

    # await produce_message(producer, topic_name, b'trailer', b'star wars', [('user_id', b'51235123521'), ("user_name", b'Anton')])
    # await produce_message(producer, topic_name, b'movie', b'doom', [('user_id', b'51235123521'), ("movies_id", b'3261326231')])
    # await produce_message(producer, topic_name, b'category', b'action', [('user_id', b'5123532311'), ("user_name", b'Mark')])
    # await produce_message(producer, topic_name, b'category', b'drama', [('user_id', b'51252432521'), ("user_name", b'Vadim')])
    # await produce_message(producer, topic_name, b'category', b'trill', [('user_id', b'512356364521'), ("user_name", b'Olga')])

    producer.close()


if __name__ == "__main__":
    asyncio.run(main())