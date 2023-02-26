from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import asyncpg
from config import Config
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from db.utils import make_connection_string
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.engine import URL
from create_url import create_url
from .repositories import UserRepo, ChatRepo

async def create_async_engine(url: URL | str) -> AsyncEngine:
    print(create_url())
    return _create_async_engine(
        url=url, encoding="utf-8", pool_pre_ping=True
    )


async def create_session_maker(engine: AsyncEngine = None) -> sessionmaker:
    print('484848')
    return sessionmaker(
        engine or create_async_engine(create_url()),
        class_=AsyncSession,
        expire_on_commit=False,
    )


class Database:
    """
    Database class is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions
    """

    user: UserRepo
    """ User repository """
    chat: ChatRepo
    """ Chat repository """

    session: AsyncSession

    def __init__(
        self, session: AsyncSession = create_session_maker, user: UserRepo = None, chat: ChatRepo = None
    ):
        self.session = session
        self.user = user or UserRepo(session=session)
        self.chat = chat or ChatRepo(session=session)