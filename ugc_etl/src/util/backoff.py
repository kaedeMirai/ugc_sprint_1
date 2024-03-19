import random
import logging
import time
from functools import wraps

import clickhouse_driver
from aiokafka.errors import KafkaError, KafkaConnectionError


def backoff(start_sleep_time=0.1, factor=2, border_sleep_time=1):

    def backoff(func):
        @wraps(func)
        def inner(*args, **kwargs):
            n = 0
            sleep_time = start_sleep_time
            jitter = random.random()
            while sleep_time < border_sleep_time:
                try:
                    return func(*args, **kwargs)
                except (clickhouse_driver.errors.NetworkError, KafkaError, KafkaConnectionError) as ex:
                    logging.error(ex)
                    sleep_time = start_sleep_time * (factor ** n) + jitter
                    time.sleep(sleep_time)
                    n += 1
            raise ConnectionError
        return inner
    return backoff
