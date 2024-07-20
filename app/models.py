from sqlalchemy import Column, Integer, String, Interval, DateTime
from app.db import Base
from sqlalchemy.sql import func
from sqlalchemy import select
from datetime import datetime, timedelta


class Sport(Base):
    __tablename__ = "sports"
    id = Column(Integer, primary_key=True)
    nickname = Column(String(length=50))
    user_id = Column(String(length=200))
    chat_id = Column(String(length=200))
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
    def best_query(session, chat_id):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        stmt = (
            select(Sport.nickname, func.sum(Sport.duration).label("total_duration"))
            .where(Sport.chat_id == chat_id, Sport.created_at >= thirty_days_ago)
            .group_by(Sport.nickname)
            .order_by(func.sum(Sport.duration).desc())
            .limit(10)
        )
        return session.execute(stmt)

    @staticmethod
    def records_by_user_id_query(session, user_id):
        return session.query(Sport).filter_by(user_id=user_id).all()
