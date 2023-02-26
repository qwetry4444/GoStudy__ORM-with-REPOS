from config import Config

def make_connection_string(config: Config, async_fallback: bool = False) -> str:
    result =(
        f"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}:"
        f"{config.db.port}/{config.db.database}"
    )
    return result