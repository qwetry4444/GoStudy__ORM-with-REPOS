from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

import messages
from db.functions.user_func import user_exist, create_user

class RegisterCheck(BaseMiddleware):
    """
    Middleware будет вызываться каждый раз, когда пользователь будет отправлять боту сообщения (или нажимать
    на кнопку в инлайн-клавиатуре).
    """

    def __init__(self):
        """
        Не нужен в нашем случае
        """
        pass

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        """ Сама функция для обработки вызова """
        if event.web_app_data:
            return await handler(event, data)

        session_maker = data['session_maker']

        user = event.from_user

        # Получаем менеджер сессий из ключевых аргументов, переданных в start_polling()
        if not await user_exist(user_tg_id=event.from_user.id, session_maker=session_maker):
            await event.answer(messages.REGISTRATION_MESSAGE)
            await create_user(user_tg_id=event.from_user.id,
                              user_name=event.from_user.username, session_maker=session_maker, user_group="609-22")
            await data['bot'].send_message(event.from_user.id, 'Ты успешно зарегистрирован(а)!')

        return await handler(event, data)