from sqlalchemy import Column, Integer, String, Interval, DateTime
from .db import Base  # Import Base frpm db.py
from sqlalchemy.sql import func


class Sport(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(lenght=50))
    sportname = Column(String(length=50))
    duration = Column(Interval)
    created_at = Column(DateTime, default=func.now())

