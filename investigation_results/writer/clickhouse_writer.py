import time
import logging

from clickhouse_driver import Client
from core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def write_to_ch(data_batch):
    with Client(host=settings.clickhouse_host) as client:

        start_time = time.time()

        for user_id, movie_id, viewed_frame in data_batch:
            client.execute(f"""
                INSERT INTO test.view (user_id, movie_id, viewed_frame)
                VALUES ('{user_id}', '{movie_id}', {viewed_frame})
            """)

        end_time = time.time()

    logger.info(f"Data successfully added. "
                f"Number of records: {len(data_batch)}. "
                f"Execution time: {end_time - start_time} sec.")
