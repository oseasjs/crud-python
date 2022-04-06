import unittest
from faker import Faker
from src.model import Task
from src.config import DbConnectionHandler
from .task_service import TaskService
from src.exception.business_exception import BusinessException

faker = Faker()


class TaskServiceTest(unittest.TestCase):
    def setUp(self):
        super(TaskServiceTest, self).setUp()
        self.expected_task = add_task(
            faker.random_number(digits=5), faker.name(), faker.name()
        )

    def tearDown(self):
        super(TaskServiceTest, self).tearDown()
        delete_task(self.expected_task.id)
        self.mock_data = []

    def test_add_success(self):
        """Test task service add method"""

        params = {"title": faker.name(), "description": faker.name()}
        task = TaskService().add(params)

        task_inserted = select_task(task.id)

        assert task
        assert task_inserted
        assert task_inserted.id == task.id
        assert task_inserted.title == task.title
        assert task_inserted.description == task.description

        delete_task(task_inserted.id)

    def test_add_missing_title_failed(self):
        """Test task service add method missing title field on payload"""
        try:
            params = {"description": faker.name()}
            TaskService().add(params)
        except BusinessException as ex:
            assert str(ex).upper() == "TITLE IS REQUIRED"

    def test_add_blank_title_failed(self):
        """Test task service add method with blank title on payload"""
        try:
            params = {"title": " "}
            TaskService().add(params)
        except BusinessException as ex:
            assert str(ex).upper() == "TITLE IS REQUIRED"

    def test_add_missing_description_failed(self):
        """Test task service add method missing description field on payload"""

        try:
            params = {"title": faker.name()}
            TaskService().add(params)
        except BusinessException as ex:
            assert str(ex).upper() == "DESCRIPTION IS REQUIRED"

    def test_add_blank_description_failed(self):
        """Test task service add method with blank description on payload"""

        try:
            params = {"title": faker.name(), "description": " "}
            TaskService().add(params)
        except BusinessException as ex:
            assert str(ex).upper() == "DESCRIPTION IS REQUIRED"

    def test_update_success(self):
        """Test task service update method"""

        params = {"title": faker.name(), "description": faker.name()}
        task = TaskService().update(self.expected_task.id, params)

        task_updated = select_task(task.id)

        assert task
        assert task_updated
        assert task_updated.id == task.id
        assert task_updated.title == task.title
        assert task_updated.description == task.description

    def test_update_missing_task_id_failed(self):
        """Test task service update method missing task_id param"""
        try:
            TaskService().update(None, {})
        except BusinessException as ex:
            assert str(ex).upper() == "TASK ID IS REQUIRED"

    def test_update_missing_title_failed(self):
        """Test task service update method missing title field on payload"""
        try:
            params = {"description": faker.name()}
            TaskService().update(self.expected_task.id, params)
        except BusinessException as ex:
            assert str(ex).upper() == "TITLE IS REQUIRED"

    def test_update_blank_title_failed(self):
        """Test task service add method with blank title on payload"""
        try:
            params = {"title": " "}
            TaskService().update(self.expected_task.id, params)
        except BusinessException as ex:
            assert str(ex).upper() == "TITLE IS REQUIRED"

    def test_update_missing_description_failed(self):
        """Test task service add method missing description field on payload"""

        try:
            params = {"title": faker.name()}
            TaskService().update(self.expected_task.id, params)
        except BusinessException as ex:
            assert str(ex).upper() == "DESCRIPTION IS REQUIRED"

    def test_update_blank_description_failed(self):
        """Test task service add method with blank description on payload"""

        try:
            params = {"title": faker.name(), "description": " "}
            TaskService().update(self.expected_task.id, params)
        except BusinessException as ex:
            assert str(ex).upper() == "DESCRIPTION IS REQUIRED"

    def test_delete_success(self):
        """Test task service delete method"""

        task_id = faker.random_number(digits=5)
        task_inserted = add_task(
            faker.random_number(digits=5), faker.name(), faker.name()
        )
        TaskService().delete(task_inserted.id)

        expected_task = select_task(task_inserted.id)
        assert expected_task is None

    def test_delete_missing_task_id_failed(self):
        """Test task service delete missing task_id method"""

        try:
            TaskService().delete(None)
        except BusinessException as ex:
            assert str(ex).upper() == "TASK ID IS REQUIRED"

    def test_find_all_success(self):
        """Test task service find_all method"""

        task_list = TaskService().find_all()
        task_list_filtered = list(
            filter(lambda t: t.id == self.expected_task.id, task_list)
        )

        assert len(task_list_filtered) == 1
        assert self.expected_task.id == task_list_filtered[0].id
        assert self.expected_task.title == task_list_filtered[0].title
        assert self.expected_task.description == task_list_filtered[0].description

    def test_find_by_id_success(self):
        """Test task service find_by_id method"""

        task = TaskService().find_by_id(self.expected_task.id)

        assert task
        assert self.expected_task.id == task.id
        assert self.expected_task.title == task.title
        assert self.expected_task.description == task.description

    def test_find_by_id_missing_task_id_failed(self):
        """Test task service find_by_id method"""

        try:
            task = TaskService().find_by_id(None)
        except BusinessException as ex:
            assert str(ex).upper() == "TASK ID IS REQUIRED"

    def test_find_by_title_success(self):
        """Test task service find by title method"""

        params = []
        params.append({"title", self.expected_task.title})
        task_list = TaskService().find(params)
        task_list_filtered = list(
            filter(lambda t: t.id == self.expected_task.id, task_list)
        )

        assert len(task_list_filtered) > 0
        assert self.expected_task.id == task_list_filtered[0].id
        assert self.expected_task.title == task_list_filtered[0].title
        assert self.expected_task.description == task_list_filtered[0].description

    def test_find_by_description_success(self):
        """Test task service find by description method"""

        params = []
        params.append({"description", self.expected_task.description})
        task_list = TaskService().find(params)
        task_list_filtered = list(
            filter(lambda t: t.id == self.expected_task.id, task_list)
        )

        assert len(task_list_filtered) > 0
        assert self.expected_task.id == task_list_filtered[0].id
        assert self.expected_task.title == task_list_filtered[0].title
        assert self.expected_task.description == task_list_filtered[0].description


def add_task(task_id: int, title: str, description: str) -> Task:
    with DbConnectionHandler() as conn:
        try:
            conn.session.execute(
                "INSERT INTO tasks (id, title, description) VALUES ('{}', '{}', '{}');".format(
                    task_id, title, description
                )
            )
            conn.session.commit()
            return Task(
                id=task_id,
                title=title,
                description=description,
            )
        except Exception as ex:
            conn.session.rollback()
            print(ex)
            raise
        finally:
            conn.session.close()


def delete_task(task_id: int):
    with DbConnectionHandler() as conn:
        try:
            conn.session.execute("DELETE FROM tasks WHERE id={};".format(task_id))
            conn.session.commit()
        except Exception as ex:
            conn.session.rollback()
            print(ex)
            raise
        finally:
            conn.session.close()


def select_task(task_id: int) -> Task:
    with DbConnectionHandler() as conn:
        try:
            task = conn.session.execute(
                "SELECT * FROM tasks WHERE id='{}';".format(task_id)
            ).fetchone()
            conn.session.commit()

            if task == None:
                return None

            return Task(
                id=task.id,
                title=task.title,
                description=task.description,
            )
        except Exception as ex:
            conn.session.rollback()
            print(ex)
            raise
        finally:
            conn.session.close()


if __name__ == "__main__":
    unittest.main()
