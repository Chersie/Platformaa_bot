from aiogram import types, Bot
from .create_database import User, Task, db
from gino import Gino
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql
from gino.schema import GinoSchemaVisitor

class DBCommands:
    async def get_user(self, tg_id) -> User:
        user = await User.query.where(User.tg_id == tg_id).gino.first()
        return user

    async def add_new_user(self, referrer=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.tg_id = user.id
        new_user.username = user.username
        new_user.reg_time = db.func.current_timestamp()
        if referrer:
            new_user.referrer = int(referrer)
        await new_user.create()
        return new_user

    async def add_new_task(self, client_tg_id: int, amount: int, guarantee: str,
                           platform: str, type: str, link: str) -> Task:
        client = await self.get_user(client_tg_id)
        new_task = Task()
        new_task.client = client
        new_task.amount = amount
        new_task.guarantee = guarantee
        new_task.platform = platform
        new_task.type = type
        new_task.link = link
        await new_task.create()
        return new_task

    # setters
    async def set_vk_id(self, vk_id):
        tg_id = types.User.get_current().id
        user = await self.get_user(tg_id)
        await user.update(vk_id=vk_id).apply()

    async def set_inst_id(self, inst_id):
        tg_id = types.User.get_current().id
        user = await self.get_user(tg_id)
        await user.update(inst_id=inst_id)

    async def set_balance(self, new_balance):
        tg_id = types.User.get_current().id
        user = await self.get_user(tg_id)
        await user.update(balance=new_balance).apply()

    async def set_profile_information(self, age, location, income):
        tg_id = types.User.get_current().id
        user = await self.get_user(tg_id)
        await user.update(age=age, location=location, income=income)

    # commands
    async def count_users(self):
        return await db.func.count(User.id).gino.scalar()

    async def get_referrals(self, count):
        tg_id = types.User.get_current().id
        user = await self.get_user(tg_id)
        referrals = await user.query.where(User.referrer == user.id).gino.all()
        return referrals
