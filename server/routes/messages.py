from fastapi import APIRouter

from server.models.message import MessageOut, MessageIn, RecipientMessages
from server.database import db_manager

messages = APIRouter()


@messages.post('/', response_model=MessageOut, status_code=201)
async def send_message(payload: MessageIn):
    message_id = await db_manager.add_message(payload)

    response = {
        'id': message_id,
        **payload.dict()
    }
    return response


@messages.get('/', response_model=RecipientMessages)
async def get_messages():
    messages = await db_manager.get_recipient_messages()
    res = {"messages": messages}
    return res
