from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.database import Base


class Account(Base):

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    platform = Column(String)

    access_token = Column(String)
