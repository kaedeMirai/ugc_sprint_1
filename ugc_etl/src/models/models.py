from pydantic import BaseModel


class MessageDto(BaseModel):
    id: str
    user_id: str
    movie_id: str | None = None
    action: str
    timestamp: int
    event_data: str
