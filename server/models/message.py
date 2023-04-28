from pydantic import BaseModel
from typing import List


class MessageIn(BaseModel):
    message: str


class MessageOut(MessageIn):
    id: int
    response: str


class ConversationMessages(BaseModel):
    messages: List[str]
