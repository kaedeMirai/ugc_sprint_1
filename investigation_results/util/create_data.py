import uuid
import random


def generate_random_data(batch_size):
    data_list = []

    for _ in range(batch_size):
        user_id = uuid.uuid4()
        movie_id = uuid.uuid4()
        viewed_frame = random.randint(1, 7200)
        data_list.append((user_id, movie_id, viewed_frame))

    return data_list
