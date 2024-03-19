import asyncio
from time import sleep
import logging

from extract.kafka_reader import KafkaReader
from transform.transform import transform_messages
from load.clickhouse_writer import ClickhouseWriter
from util.init_kafka import init_kafka
from util.init_clickhouse import init_clickhouse
from util.backoff import backoff

logging.basicConfig(level=logging.INFO)


@backoff(start_sleep_time=0.1, factor=2, border_sleep_time=10)
async def run_etl(batch_size: int = 10):
    async with KafkaReader() as reader:
        async for messages in reader.read(batch_size):
            transformed_messages = transform_messages(messages)

            async with ClickhouseWriter() as writer:
                await writer.write(transformed_messages)

            await reader.commit()

            logging.info(f'Successfully wrote {len(transformed_messages)} messages to clickhouse.')
            sleep(3)


@backoff(start_sleep_time=0.1, factor=2, border_sleep_time=10)
async def main():
    await init_kafka()
    await init_clickhouse()

    while True:
        await run_etl()


if __name__ == "__main__":
    asyncio.run(main())
