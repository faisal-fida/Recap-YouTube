from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from app.models import ModelBase

class Summary(ModelBase):
    __tablename__ = "summary"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    image = Column(String, nullable=False)
    
    def __str__(self):
        return f"{self.video_id} - {self.title}"
