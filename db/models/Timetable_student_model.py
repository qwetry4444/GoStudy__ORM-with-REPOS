from sqlalchemy import Integer, String, Text, Column, BigInteger, VARCHAR

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Timetable_student(Base):
    __tablename__ = "timetable_student"

    timetable_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )
    group_number = Column(
        VARCHAR(10), nullable=False
    )
    weekday = Column(
        VARCHAR(10), nullable=False
    )
    timetable = Column(
        VARCHAR(2000), nullable=False
    )
