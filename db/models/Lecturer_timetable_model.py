from sqlalchemy import Integer, String, Text, Column, BigInteger, VARCHAR

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Timetable_lecturer(Base):
    __tablename__ = "timetable_lecturer"

    timetable_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )

    lecturer_name = Column(
        VARCHAR(255), nullable=False
    )

    department = Column(
        Integer, nullable=True
    )

    timetable_monday = Column(
        VARCHAR(255), nullable=True
    )

    timetable_monday_class_number = Column(
        VARCHAR(255), nullable=True
    )

    timetable_tuesday = Column(
        VARCHAR(255), nullable=True
    )

    timetable_tuesday_class_number = Column(
        VARCHAR(255), nullable=True
    )
    timetable_wednesday = Column(
        VARCHAR(255), nullable=True
    )

    timetable_wednesday_class_number = Column(
        VARCHAR(255), nullable=True
    )
    timetable_thursday = Column(
        VARCHAR(255), nullable=True
    )

    timetable_thursday_class_number = Column(
        VARCHAR(255), nullable=True
    )
    timetable_friday = Column(
        VARCHAR(255), nullable=True
    )

    timetable_friday_class_number = Column(
        VARCHAR(255), nullable=True
    )
    timetable_saturday = Column(
        VARCHAR(255), nullable=True
    )

    timetable_saturday_class_number = Column(
        VARCHAR(255), nullable=True
    )
