import time
import logging

import vertica_python
from util.init_vertica import connection_info
from util.create_data import generate_random_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_from_vertica(batch_size):
    with vertica_python.connect(**connection_info) as connection:
        cursor = connection.cursor()

        start_time = time.time()

        cursor.execute(f"""SELECT * FROM view LIMIT {batch_size}""")
        result = cursor.fetchall()

        end_time = time.time()

    logger.info(f"Data successfully added. "
                f"Number of records: {len(result)}. "
                f"Execution time: {end_time - start_time} sec")
