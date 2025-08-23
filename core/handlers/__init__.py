from pyrogram import Client, filters
from dispyro import Dispatcher

from typing import Dict, Tuple

# handlers import
from .ping import ping


async def setup_handlers(apps_dp: Dict[str, Tuple[Client, Dispatcher]]):
    # register handlers
    dp = apps_dp['dp']
    dp.message.register(ping, filters=filters.me & filters.regex(r'^пинг$'))


