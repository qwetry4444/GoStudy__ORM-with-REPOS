from db.models.User_model import User
from sqlalchemy import select, insert, update, func
from sqlalchemy.orm import sessionmaker, relationship, selectinload


async def get_user(user_tg_id: int, session_maker: sessionmaker) -> User:
    """
    Получить пользователя по его id
    :param user_id:
    :param session_maker:
    :return:
    """
    async with session_maker as session:
        async with session.begin():
            sql = select(User).where(User.tg_id == user_tg_id)
            result = await session.execute(sql)
    return result.scalars().one()


async def create_user(user_tg_id, user_name, user_group, session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            new_user = User(
                tg_id=user_tg_id,
                user_name=user_name,
                group_number=user_group
            )
            try:
                session.add(new_user)
                session.commit()
            except Exception as exception:
                session.rollback()
                print(exception)


async def user_exist(user_tg_id: int, db) -> bool:

    async with db.session as session:
        async with session.begin():
            sql = await select(User).where(User.tg_id == user_tg_id)
            request = await session.execute(sql)
            return bool(request)
