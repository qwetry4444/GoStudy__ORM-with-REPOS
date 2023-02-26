from dataclasses import dataclass

from environs import Env

@dataclass
class DbConfig:
    user: str
    password: str
    database: str
    host: str
    port: int

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    db: DbConfig
    tg: TgBot

def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg=TgBot(
            token=env.str('BOT_TOKEN'),
        ),
        db=DbConfig(
            user=env.str('POSTGRES_USER'),
            password=env.str('POSTGRES_PASSWORD'),
            database=env.str('POSTGRES_DB'),
            host=env.str('POSTGRES_HOST'),
            port=env.int("POSTGRES_PORT")
        ),

    )

