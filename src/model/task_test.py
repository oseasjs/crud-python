import json
import unittest
from faker import Faker
from .task import Task

faker = Faker()


class TaskTest(unittest.TestCase):
    """Class to test TaskService methods"""

    @classmethod
    def test_to_json(cls):
        task = Task()
        task.id = faker.random_number(digits=5)
        task.title = faker.name()
        task.description = faker.name()

        assert task.to_json() == {"id": task.id, "title": task.title, "description": task.description}