from sqlalchemy import Integer, String, Text, Column, BigInteger, VARCHAR

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    user_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )
    tg_id = Column(
        BigInteger, nullable=False
    )
    user_name = Column(
        VARCHAR(32), nullable=False
    )
    group_number = Column(
        VARCHAR(10), nullable=False
    )





