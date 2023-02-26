from aiogram import Router
from aiogram.filters import Command

from bot.handlers.message_handler import start

def register_user_commands(router: Router):
    router.message.register(start, Command(commands=['start']))