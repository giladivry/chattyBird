from pydantic import BaseModel
from typing import List


class MessageIn(BaseModel):
    message: str


class MessageOut(BaseModel):
    id: int
    response: str


class RecipientMessages(BaseModel):
    messages: List
