from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Person(Base):

    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    group = Column(String, nullable=False)
    note = Column(Text, nullable=True)
    photo = Column(String, nullable=True)
