import asyncio

from aiogram import types, Bot
from gino import Gino
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql
from gino.schema import GinoSchemaVisitor

from data.config import DB_PASS, DB_USER, ip

db = Gino()


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)  # inner id
    tg_id = Column(BigInteger)  # telegram id
    vk_id = Column(BigInteger)  # vk_id
    inst_id = Column(BigInteger)  # inst_id
    username = Column(String(32))
    referrer = Column(Integer)  # inner id of user that invited current user
    reg_time = Column(TIMESTAMP)
    balance = Column(BigInteger, default=0)
    age = Column(String(5))
    location = Column(JSON)
    income = Column(Boolean)
    query: sql.Select


class Task(db.Model):
    __tablename__ = "tasks"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    client = Column(Integer)
    amount = Column(Integer)  # how many times task can be completed
    guarantee = Column(String(10))  # 0 days/3 days/14 days/forever
    platform = Column(String(10))  # vk/tg/inst
    type = Column(String(10))  # like/repost/subscribe
    link = Column(String(200))  # link to the post/account
    query: sql.Select


class Balance_operation(db.Model):
    pass


class Promo(db.Model):
    pass



async def create_db():
    await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{ip}/postgres")
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
