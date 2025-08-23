from pyrogram import Client, idle, filters, enums
from dispyro.enums import RunLogic
from dispyro import Dispatcher

from redis.asyncio import Redis
from asyncmy.pool import Pool

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Tuple, Dict

# local imports
from core.handlers import setup_handlers
from core.utils.db_api.database import create_mysql_pool, db_setup
from core.utils.db_api.repo import RequestsRepo
from core.filters.is_user import is_user
from core.settings import logger, settings
from core.service.loop_task import scheduler_tasks
from core.func import full_name_getter

import asyncio
import uvloop
import logging
import os

async def on_startup(app: Client):
    me = await app.get_me()
    logger.info(f'App {full_name_getter(me)} [{me.id}] - PID {os.getpid()} запущено.')

async def start_client(
    pool: Pool,
    redis: Redis, 
    ses_name: str = 'my_app'
) -> Dict[str, Tuple[Client, Dispatcher]]:
    apps_dp = {'app': Client, 'dp': Dispatcher}
    app = Client(
        f'core/sessions/{ses_name}',
        settings.app.api_id,
        settings.app.api_hash,
        phone_number=settings.app.phone_number,
        parse_mode=enums.ParseMode.HTML
    )
    apps_dp['app'] = app
    
    # Invoke start method of client & dispatchers
    await apps_dp['app'].start()
    
    repo = RequestsRepo()

    me = await app.get_me()
    dp = Dispatcher(
        app,
        me=me,
        repo=repo,
        pool=pool,
        redis=redis,
        run_logic=RunLogic.UNLIMITED
    )
    dp.message.filter(filters.text & is_user & ~filters.forwarded & (filters.private | filters.group))
    apps_dp['dp'] = dp
    
    return apps_dp

async def main():
    
    redis = Redis(host=settings.redis.ip, port=6379, decode_responses=True)
    scheduler = AsyncIOScheduler()
    pool = await create_mysql_pool()
    
    # apps & dispatcher objects
    apps_dp = await start_client(pool, redis)
    
    await db_setup(pool)
    await scheduler_tasks(pool, apps_dp['app'], scheduler)
    await setup_handlers(apps_dp)
    
    try:
        await on_startup(apps_dp['app'])
        scheduler.start()
        await idle()
    finally:
        pass


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())