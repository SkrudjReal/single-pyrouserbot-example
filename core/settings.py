from environs import Env
from dataclasses import dataclass

from pytz import timezone
from pathlib import Path

import logging

@dataclass
class App:
    api_id: int
    api_hash: str
    phone_number: str

@dataclass 
class MysqlDB:
    ip: str
    db: str
    password: str
    user: str

@dataclass
class RedisDB:
    ip: str

@dataclass
class Settings:
    app: App
    db: MysqlDB
    redis: RedisDB


def get_settings(path: str = 'settings.env'):
    if not Path(path).exists():
        raise FileNotFoundError(f"Environment file {path} not found.")
    env = Env()
    env.read_env(path)
    return Settings(
        app=App(
            api_id=env.int('API_ID'),
            api_hash=env.str('API_HASH'),
            phone_number=env.str('PHONE_NUMBER', default='')
        ),
        db=MysqlDB(
            ip=env.str('ip'),
            db=env.str('db'),
            user=env.str('user'),
            password=env.str('password')
        ),
        redis=RedisDB(
            ip=env.str('REDIS_IP')
        )
    )

def setup_logger(name: str = 'pyrogram', level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logging.getLogger("pyrogram").setLevel(logging.INFO)
    logging.getLogger("asyncmy").setLevel(logging.ERROR)
    
    if not logger.hasHandlers():
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s | %(name)s: %(message)s")

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


logger = setup_logger(level=logging.INFO)
settings = get_settings()
moscow_tz = timezone('Europe/Moscow')