from pyrogram.types import Message, User
from pyrogram import Client

from redis.asyncio import Redis
from asyncmy.pool import Pool

from core.data.tricks import tricks
from core.utils.db_api.repo import RequestsRepo
import time

async def ping(app: Client, msg: Message, me: User, pool: Pool, repo: RequestsRepo, redis: Redis):

    time_start = time.time()
    mesg = await msg.reply(tricks['ping']['ping'], quote=False)
    time_end = time.time()
    await mesg.edit_text(tricks['ping']['ping_speed'].format(f'{time_end-time_start:.3f}'))
    await msg.delete()

