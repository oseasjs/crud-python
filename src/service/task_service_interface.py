from abc import ABC, abstractmethod
from typing import List
import json
from src.model.task import Task  # pylint: disable=E0401


class TaskServiceInterface(ABC):
    """Interface to Task Service Interface"""

    @abstractmethod
    def add(self, body: json) -> Task:
        """Insert task"""
        raise Exception("Should implement method: add")

    @abstractmethod
    def update(self, task_id: int, body: json) -> Task:
        """Update task"""
        raise Exception("Should implement method: update")

    @abstractmethod
    def delete(self, task_id: int) -> Task:
        """Delete task by id"""
        raise Exception("Should implement method: delete")

    @abstractmethod
    def find_all(self) -> List[Task]:
        """Select task"""
        raise Exception("Should implement method: findAll")

    @classmethod
    def find_by_id(cls, task_id: int = None) -> List[Task]:
        """Select task by id"""
        raise Exception("Should implement method: findById")

    @classmethod
    def find(cls, *params) -> List[Task]:
        """Select tasks by title and description"""
        raise Exception("Should implement method: find")
