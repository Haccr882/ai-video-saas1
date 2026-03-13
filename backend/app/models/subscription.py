from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.database import Base


class Subscription(Base):

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    plan = Column(String)

    status = Column(String)
