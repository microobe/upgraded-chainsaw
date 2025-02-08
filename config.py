import storage
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings
from aiogram.fsm.storage.redis import RedisStorage

class Secrets(BaseSettings):
    token: str
    redis_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()

default = DefaultBotProperties(parse_mode='Markdown', protect_content=True)
bot = Bot(token = secrets.token, default=default)
storage = RedisStorage.from_url(secrets.redis_url)
dp = Dispatcher(storage = storage)