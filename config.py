from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings


class Secrets(BaseSettings):
    token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()

default = DefaultBotProperties(parse_mode='Markdown', protect_content=True)
bot = Bot(token = secrets.token, default=default)
dp = Dispatcher()