from pyrogram import Client, enums

from core.settings import settings


app = Client('my_app', settings.app.api_id, settings.app.api_hash,
             phone_number=settings.app.phone_number,
             parse_mode=enums.ParseMode.HTML
)

