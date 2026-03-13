from pydantic import BaseModel
from datetime import datetime


class VideoCreate(BaseModel):

    title: str

    platform: str

    schedule_time: datetime
