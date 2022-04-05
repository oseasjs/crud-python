from flask import Flask, Response, request
from src.controller import task_controller

from src import *

if __name__ == '__main__':
    app.run(debug=True, port=5001)