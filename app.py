from src.controller import task_controller  # noqa: F401
from src import *  # noqa: F403

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # noqa: F403,F405
