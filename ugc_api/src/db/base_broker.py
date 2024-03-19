from abc import ABC, abstractmethod
from api.v1.schemas import NewMessage


class BaseBroker(ABC):

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...

    @abstractmethod
    async def send(self, topic: str, message: NewMessage) -> None:
        ...
