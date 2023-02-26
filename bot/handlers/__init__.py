from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.command import CommandStart
from aiogram.fsm.state import any_state
from aiogram.types import ContentType
from aiogram.utils.i18n import lazy_gettext as __

from bot.handlers.message_handler import start

__all__ = ('register_user_commands', 'bot_commands', 'register_user_handlers',)


def register_user_commands(router: Router) -> None:
    """
    Зарегистрировать хендлеры пользователя
    :param router:
    """
    router.message.register(start, Command(commands=['start']))


register_user_handlers = register_user_commands
