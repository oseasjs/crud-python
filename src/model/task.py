from sqlalchemy import Column, Integer, String
from .db_base import Base


class Task(Base):
    """Task Entity"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, unique=False)

    def to_json(self):
        """Convert self object to json"""
        return {"id": self.id, "title": self.title, "description": self.description}
