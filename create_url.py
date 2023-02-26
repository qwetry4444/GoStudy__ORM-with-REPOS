from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv


def create_url():
    load_dotenv()
    postgres_url = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER"),
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT"),
        )
    print('шииииищь')
    return postgres_url
