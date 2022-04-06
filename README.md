## CRUD Python

### Build Branches Status

| Branch        | Build         | Coverage  |
| ------------- |:-------------:| ---------:|
| Develop       | ![CI](https://github.com/oseasjs/crud-python/workflows/CI/badge.svg?branch=develop) | [![codecov](https://codecov.io/gh/oseasjs/crud-python/branch/develop/graph/badge.svg)](https://codecov.io/gh/oseasjs/crud-python/branch/develop) |
| Main          | ![CI](https://github.com/oseasjs/crud-python/workflows/CI/badge.svg?branch=main)  | [![codecov](https://codecov.io/gh/oseasjs/crud-python/branch/main/graph/badge.svg)](https://codecov.io/gh/oseasjs/crud-python/branch/main) |

### Bootstrapped with

- [Python 3.x](https://www.python.org/doc)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [SQLite](https://www.sqlite.org/docs.html)
- [Black](https://pypi.org/project/black/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [PyLint](https://pylint.pycqa.org/en/latest/)
- [PyTest](https://docs.pytest.org/en/6.2.x/contents.html)
- [Faker](https://faker.readthedocs.io/en/master/)
- [Github Action](https://github.com/features/actions)
- [Coverage](https://coverage.readthedocs.io/en/6.3.2/)

### Project Goal

Python application that provides API to create, read, update and delete Tasks

### Modules and Strategies used

- Controller (endpoints)
- Service (business rules and persistence)
- Model (orm)
- DB Transaction
- Persistence in DB (SQLite)
- Custom Exception
- Interface
- Constants
- Test with DB Persistence using SetUp/TearDown strategy

### Installing and Running

- To install all dependencies, run the command: `pip install -r requirements.txt;`
- To run the application locally on port _5001_, run the command: `python3 app.py`
- To execute Tests (unit tests), run the command: `pytest`
- To execute Black (code formatter), run the command: `black .`
- To execute Lint (code style), run the command: `pylint .`
- To update requirements.txt (for new dependencies), run the command: `pip3 freeze > requirements.txt`

### Dependence Injection

- [Python Dependence Injector](https://github.com/ets-labs/python-dependency-injector): _Comming Soon_

### CRULs example to test the endpoints

- Add Task: 
  ```
  curl --location --request POST 'localhost:5001/tasks' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "title": "Task",
      "description": "Description"
  }'
  ```

- Update Task (replace EXISTING_TASK_ID): 
  ```
  curl --location --request PUT 'localhost:5001/tasks/EXISTING_TASK_ID' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "title": "Task Title 6a",
      "description": "Task Description 6a"
  }'
  ```

- Delete Task (replace EXISTING_TASK_ID): 
  ```
  curl --location --request DELETE 'localhost:5001/tasks/EXISTING_TASK_ID'
  ```

- Find all Tasks: 
  ```
  curl --location --request GET 'localhost:5001/tasks/all'
  ```

- Find Task by Id: 
  ```
  curl --location --request GET 'localhost:5001/tasks/6'
  ```

- Find Task by Title: 
  ```
  curl --location --request GET 'localhost:5001/tasks?title=Title'
  ```

- Find Task by Description: 
  ```
  curl --location --request GET 'localhost:5001/tasks?description=Description'
  ```


### Inspiration

- Documentation:
  - https://peps.python.org/pep-0008/
  - https://flake8.pycqa.org/en/latest/
  - https://docs.python.org/3/library/unittest.html
  - https://docs.pytest.org/en/stable/

- Videos: 

  - [Programador Lhama](https://github.com/programadorLhama) (playlist): https://www.youtube.com/playlist?list=PLAgbpJQADBGK-FaAZBvbAnqALbwcpR4Xu
  - [Roger Vieira](https://github.com/vieiraroger): https://www.youtube.com/watch?v=WDpPGFkI9UU

- Projects and article used as reference:
  - https://github.com/programadorLhama/backend_project_python-lab-
  - https://github.com/gibran-abdillah/simple-crud
  - https://thiagolopessilva.medium.com/running-unit-testing-on-github-action-using-pytest-61653d993c9c