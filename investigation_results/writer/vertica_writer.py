import time
import logging

import vertica_python
from util.init_vertica import connection_info
from util.create_data import generate_random_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def write_to_vertica(data_batch):
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()

        start_time = time.time()

        for user_id, movie_id, viewed_frame in data_batch:
            cursor.execute("""
                INSERT INTO view (user_id, movie_id, viewed_frame)
                VALUES (%s, %s, %s)
            """, (user_id, movie_id, viewed_frame))

        end_time = time.time()

    logger.info(f"Data successfully added. "
                f"Number of records: {len(data_batch)}. "
                f"Execution time: {end_time - start_time} sec")
