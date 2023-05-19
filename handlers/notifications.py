import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger

from config import bot
from database.bot_db import sql_command_all_id


async def go_to_sleep():
    users = await sql_command_all_id()  # [(1932323,), (1932323,), (1932323,), (1932323,), ]
    for user in users:
        await bot.send_message(user[0], "ПОРА СПАТЬ!")


async def wake_up(text):
    users = await sql_command_all_id()
    for user in users:
        video = open("media/video.mp4", "rb")
        await bot.send_video(user[0], video=video, caption=text)


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        go_to_sleep,
        trigger=CronTrigger(
            hour=19,
            minute=4,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.add_job(
        wake_up,
        kwargs={
            "text": "Вставай ЕМАЕ!!!",
        },
        trigger=IntervalTrigger(
            seconds=1,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.start()
