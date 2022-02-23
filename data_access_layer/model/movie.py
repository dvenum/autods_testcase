from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .base import Base

metadata = Base.metadata


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(1))
    year = Column(Integer)
