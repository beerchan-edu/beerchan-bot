from sqlalchemy import Column, Integer, String, Interval, DateTime
from db import Base  
from sqlalchemy.sql import func



class Sport(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(length=50))
    user_id = Column(String(length=100))
    chat_id = Column(String(length=100))
    duration = Column(Interval)
    created_at = Column(DateTime, default=func.now())
    message = Column(String(length=200))


    def __init__(self, nickname, user_id, chat_id, message, duration):
        self.nickname = nickname
        self.user_id = user_id
        self.chat_id = chat_id
        self.duration = duration
        self.message = message


    @staticmethod
    def get_query(session, user):
        return session.query(Sport).filter_by(nickname=user).all()