from pydantic import BaseModel
from typing import List


class Conversation(BaseModel):
    id: int
    messages: List[int]
