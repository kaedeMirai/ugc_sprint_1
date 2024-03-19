import time
import logging

from clickhouse_driver import Client
from core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_from_ch(batch_size):
    with Client(host=settings.clickhouse_host) as client:

        start_time = time.time()

        result = client.execute(f"""SELECT * FROM test.view LIMIT ({batch_size})""")

        end_time = time.time()

    logger.info(f"Data received successfully . "
                f"Number of records: {len(result)}. "
                f"Execution time: {end_time - start_time} sec.")
