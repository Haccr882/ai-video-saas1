from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.core.database import Base


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)

    filepath = Column(String)

    platform = Column(String)

    schedule_time = Column(DateTime)

    created_at = Column(DateTime, default=datetime.utcnow)
