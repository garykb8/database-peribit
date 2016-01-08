import os
import sys
import datetime
from sqlalchemy import Column, Integer, String, DateTime

from config import Base

today = datetime.date.today()

class Game(Base):
    __tablename__ = 'game'
    __table_args__ = {'mysql_engine':'InnoDB'}

    id = Column(Integer, autoincrement=True, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    year = Column(Integer)
    price = Column(Integer)
    genre = Column(String(255))
    manufacturer = Column(String(255))


