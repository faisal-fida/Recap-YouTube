from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.models import ModelBase


class YoutubeSummary(ModelBase):
    __tablename__ = "youtube_summary"

    id = Column(Integer, primary_key=True)
    video_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)

    def __str__(self):
        return f"{self.video_id} - {self.title}"
