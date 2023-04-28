from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
from sqlalchemy.pool import StaticPool

DATABASE_URI = 'sqlite:///tmp.db'

engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False},  poolclass=StaticPool)
metadata = MetaData()


messages = Table(
    'messages',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('message', String(10000)),
)

messages.create(bind=engine, checkfirst=True)
database = Database(DATABASE_URI)
