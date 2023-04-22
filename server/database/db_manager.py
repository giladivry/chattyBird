from server.models.message import MessageIn
from server.database.db import messages, database


async def add_message(payload: MessageIn):
    query = messages.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_message(id):
    query = messages.select(messages.c.id == id)
    return await database.fetch_one(query=query)


async def get_recipient_messages():
    query = messages.select()
    return await database.fetch_all(query=query)
