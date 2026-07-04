from typing import Any

from pydantic import BaseModel
from app.constants.event_type import EventType


class OrderCreatedEvent(BaseModel):
    event_id: str
    event_type: EventType
    request_id: str
    payload: dict[str, Any]