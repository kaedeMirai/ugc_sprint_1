from pydantic import BaseModel


class NewMessage(BaseModel):
    key: str
    value: dict
