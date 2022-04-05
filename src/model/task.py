from sqlalchemy import Column, Integer, String
from .db_base import Base


class Task(Base):
    """Task Entity"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, unique=False)

    def __repr__(self):
        return f"Task [title={self.title}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.title == other.title
            and self.description == other.description
        ):
            return True
        return False

    def to_json(self):
        """Convert self object to json"""
        return {"id": self.id, "title": self.title, "description": self.description}
