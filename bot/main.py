import asyncio
# from db import db
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from db.create_session import create_session_maker
from commands import register_user_commands
from bot.handlers import register_user_commands
from bot.handlers.bot_commands import bot_commands
from aiogram.types import BotCommand
#from middlwares.register_check import RegisterCheck
import db
import os
from dotenv import load_dotenv
from create_url import create_url
from db.create_session import create_session_maker
from db.create_session import Database

async def bot_start():
    print(create_url())
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    storage = MemoryStorage()

    load_dotenv()
    bot = Bot(os.getenv("BOT_TOKEN"), parse_mode="HTML")


    # db = await create_db_session(config)



    # try:
    dp = Dispatcher()
    # dp.message.middleware(RegisterCheck())
    # dp.callback_query.middleware(RegisterCheck())

    await bot.set_my_commands(commands=commands_for_bot)
    register_user_commands(dp)
    await dp.start_polling(bot, db=Database())
    #await dp.start_polling(bot, session_maker=create_session_maker())


#     finally:
#         dp.storage.close()
# #        await dp.storage.wait_closed()
#         bot.session.close()
def main():
    asyncio.run(bot_start())


if __name__ == '__main__':
    main()
