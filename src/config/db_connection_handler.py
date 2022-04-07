from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnectionHandler:
    """SQLAlchemy database connection"""

    def __init__(self):  # pragma: no cover
        self.__connection_string = "sqlite:///crud-python.db"
        self.session = None

    def __enter__(self):  # pragma: no cover
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # pragma: no cover
        self.session.close()  # pylint: disable=no-member
