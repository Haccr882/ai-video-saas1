from sqlalchemy import Column, Integer, ForeignKey

from app.core.database import Base


class Analytics(Base):

    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True)

    video_id = Column(Integer, ForeignKey("videos.id"))

    views = Column(Integer)

    likes = Column(Integer)

    comments = Column(Integer)
