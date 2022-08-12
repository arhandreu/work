from datetime import datetime
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from api import parse
from db import sql_start, sql_add_review, show_users
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from adminBot import register_handlers_admin

storage = MemoryStorage()
sheduler = AsyncIOScheduler()

bot = Bot(token="5551675723:AAF7TrzPkM5EKyeNRooWC5xv4qnlar9ZGkg")
dp = Dispatcher(bot, storage=storage)


async def on_startup(_):
    sql_start()


async def send_message_id():
    data = parse()
    add_data = sql_add_review(data)
    if add_data != "":
        list_users = show_users()
        list_users.append(1734006490)
        for id in list_users:
            await bot.send_message(id, f"{add_data}")
    else:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Нет новых отзывов")

register_handlers_admin(dp)


sheduler.add_job(send_message_id, "interval", seconds=10)

sheduler.start()
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
