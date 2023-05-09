from decouple import config, Csv
from aiogram import Dispatcher, Bot

TOKEN = config("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
ADMINS = config("ADMINS", cast=Csv(post_process=tuple, cast=int))
