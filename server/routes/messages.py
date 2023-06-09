from fastapi import APIRouter

from server.llms.vanilla.openai_chat import chat
from server.models.message import MessageOut, MessageIn, ConversationMessages
from server.database import dal

messages = APIRouter()


@messages.post('/', response_model=MessageOut, status_code=201)
async def send_message(payload: MessageIn):
    message_id = await dal.add_message(payload)
    res = chat(payload.message)
    response = MessageOut(id=message_id, message=payload.message, response=res)

    return response


@messages.get('/', response_model=ConversationMessages)
async def get_messages():
    messages = await dal.get_recipient_messages()
    res = {"messages": messages}
    return res
