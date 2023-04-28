from fastapi import APIRouter

from server.llms.vanilla.openai_chat import chat
from server.models.message import MessageOut, MessageIn, RecipientMessages
from server.database import db_manager

messages = APIRouter()


@messages.post('/', response_model=MessageOut, status_code=201)
async def send_message(payload: MessageIn):
    message_id = await db_manager.add_message(payload)
    res = chat(payload.message)
    response = {
        'id': message_id,
        'response': res
    }
    return response


@messages.get('/', response_model=RecipientMessages)
async def get_messages():
    messages = await db_manager.get_recipient_messages()
    res = {"messages": messages}
    return res
