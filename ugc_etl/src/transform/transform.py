import json
import uuid
from aiokafka import ConsumerRecord
import logging

from models.models import MessageDto


def transform_messages(messages: list[ConsumerRecord]) -> list[tuple]:
    transformed_messages = []

    for message in messages:
        try:
            logging.info(message)
            deserialized_value = json.loads(message.value.decode('utf-8'))
            movie_id = str(deserialized_value['movie_id']) if 'movie_id' in deserialized_value else None

            message_dto = MessageDto(
                id=str(uuid.uuid4()),
                user_id=str(deserialized_value['user_id']),
                movie_id=movie_id,
                action=message.key.decode('utf-8'),
                timestamp=message.timestamp,
                event_data=message.value.decode('utf-8')
            )

            transformed_message = tuple(message_dto.dict().values())
            transformed_messages.append(transformed_message)
        except (json.JSONDecodeError, ValueError) as e:
            logging.error(e)
            continue

    return transformed_messages
