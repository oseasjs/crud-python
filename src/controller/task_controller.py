import json
from flask import Response, request
from src.service.task_service import TaskService
from src.exception.business_exception import BusinessException
from src import app

# Add task
@app.route("/tasks", methods=["POST"])
def add():
    """Endpoint to add Task"""
    try:
        task = TaskService().add(request.json)
        return response(201, "task", task.to_json(), "Success")
    except BusinessException as ex:
        return response(400, "", {}, "Error: " + str(ex))


# Update task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update(task_id: int):
    """Endpoint to update existing Task"""
    try:
        task = TaskService().update(task_id, request.json)
        return response(200, "task", task.to_json(), "Success")
    except BusinessException as ex:
        return response(400, "", {}, "Error: " + str(ex))


# Delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete(task_id: int):
    """Endpoint to delete task by task_id"""
    try:
        TaskService().delete(task_id)
        return response(200, "task", {}, "Success")
    except BusinessException as ex:
        return response(400, "", {}, "Error: " + str(ex))


# Find all tasks
@app.route("/tasks/all", methods=["GET"])
def find_all():
    """Endpoint to find all tasks"""
    try:
        tasks = TaskService().find_all()
        task_list = [task.to_json() for task in tasks]
        return response(200, "tasks", task_list, "Success")
    except BusinessException as ex:
        return response(400, "", {}, "Error: " + str(ex))


# Find task by id
@app.route("/tasks/<int:task_id>", methods=["GET"])
def find_by_id(task_id: int):
    """Endpoint to find task by task_id"""
    try:
        task = TaskService().find_by_id(task_id)
        return response(200, "tasks", task.to_json(), "Success")
    except BusinessException as ex:
        return response(400, "", {}, "Error: " + str(ex))


# Find task by params
@app.route("/tasks", methods=["GET"])
def find():
    """Endpoint to find all tasks by title or description (request params)"""
    try:
        tasks = TaskService().find(request.args.to_dict())
        task_list = [task.to_json() for task in tasks]
        return response(200, "tasks", task_list, "Success")
    except BusinessException as ex:
        return response(400, "", {}, "Error: " + str(ex))


# Common response payload
def response(status, content_name, content, message=False):
    """Build http response object"""
    body = {}
    body[content_name] = content
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
