import json
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.model import Task
from src.config import DbConnectionHandler
from src.exception.business_exception import BusinessException
from .task_service_interface import TaskServiceInterface


class TaskService(TaskServiceInterface):
    """Class to manage Task Repository"""

    @classmethod
    def add(cls, body: json) -> Task:
        """
        Insert task in db
        :param - json with title and description fields
        :return task inserted
        """

        if body.get("title") is None or body.get("title").strip() == "":
            raise BusinessException("Title is required")

        if body.get("description") is None or body.get("description").strip() == "":
            raise BusinessException("Description is required")

        with DbConnectionHandler() as conn:
            try:
                new_task = Task(title=body["title"], description=body["description"])
                conn.session.add(new_task)
                conn.session.commit()

                return Task(
                    id=new_task.id,
                    title=new_task.title,
                    description=new_task.description,
                )
            except Exception as ex:
                conn.session.rollback()
                print(ex)
                raise
            finally:
                conn.session.close()

    @classmethod
    def update(cls, task_id: int, body: json) -> Task:
        """
        Update task in db
        :param - task id
        :param - json with title and description fields
        :return updated task
        """

        if task_id == None:
            raise BusinessException("Task ID is required")

        if body.get("title") is None or body.get("title").strip() == "":
            raise BusinessException("Title is required")

        if body.get("description") is None or body.get("description").strip() == "":
            raise BusinessException("Description is required")

        with DbConnectionHandler() as conn:
            try:
                task = conn.session.query(Task).filter_by(id=task_id).one()
                task.title = body["title"]
                task.description = body["description"]
                conn.session.commit()

                return Task(id=task.id, title=task.title, description=task.description)
            except Exception as ex:
                conn.session.rollback()
                print(ex)
                raise
            finally:
                conn.session.close()

    @classmethod
    def delete(cls, task_id: int = None):
        """
        Delete task on db
        :param - task id
        """

        if task_id == None:
            raise BusinessException("Task ID is required")

        with DbConnectionHandler() as conn:
            try:
                task = conn.session.query(Task).filter_by(id=task_id).one()
                conn.session.delete(task)
                conn.session.commit()

            except Exception as ex:
                conn.session.rollback()
                print(ex)
                raise
            finally:
                conn.session.close()

    @classmethod
    def find_all(cls) -> List[Task]:
        """
        Select all tasks in db
        :return - List with Tasks selected
        """

        try:
            query_data = None
            with DbConnectionHandler() as conn:
                query_data = conn.session.query(Task).all()

            return query_data

        except NoResultFound:
            return []
        except Exception as ex:
            conn.session.rollback()
            print(ex)
            raise
        finally:
            conn.session.close()

    @classmethod
    def find_by_id(cls, task_id: int = None) -> Task:
        """
        Select tasks in db by id
        :param - Id of Task
        :return - Tasks selected
        """

        if task_id == None:
            raise BusinessException("Task ID is required")

        try:
            query_data = None
            with DbConnectionHandler() as conn:
                query_data = conn.session.query(Task).filter_by(id=task_id).one()

            return query_data

        except NoResultFound:
            return []
        except Exception as ex:
            conn.session.rollback()
            print(ex)
            raise
        finally:
            conn.session.close()

    @classmethod
    def find(cls, *params) -> List[Task]:
        """
        Select tasks by title or description
        :param["title"] - task title
        :param["description"] - task description
        :return - List with Tasks selected
        """

        try:
            query_data = None
            with DbConnectionHandler() as conn:
                filters = []

                if "title" in params:
                    filters.append(Task.title.contains(params.get("title")))

                if "description" in params:
                    filters.append(Task.description.contains(params.get("description")))

                query_data = conn.session.query(Task).filter(*filters).all()

            return query_data

        except NoResultFound:
            return []
        except Exception as ex:
            conn.session.rollback()
            print(ex)
            raise
        finally:
            conn.session.close()
