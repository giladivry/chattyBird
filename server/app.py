import openai
from fastapi import FastAPI
from pydantic import BaseSettings

from server.routes.messages import messages
from server.database.db import metadata, database, engine

metadata.create_all(engine)


class Settings(BaseSettings):
    OPENAI_API_KEY: str = 'OPENAI_API_KEY'

    class Config:
        env_file = '.env'


settings = Settings()
app = FastAPI(openapi_url="/messages/openapi.json", docs_url="/docs")
openai.api_key = settings.OPENAI_API_KEY


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(messages, prefix='/api/messages', tags=['messages'])
