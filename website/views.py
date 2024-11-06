from flask import Blueprint, Flask, jsonify, request
from . import db

views = Blueprint('views', __name__)
tasks = []
id_counter = 1

# finds a task by id
def task_finder(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

# Route to get all tasks
@views.route("/tasks", methods=["GET"])
def find_tasks():
    return jsonify(tasks)

# Route to find task by id
@views.route("/tasks/<int:task_id>", methods=["GET"])
def find_task(task_id):
    task = task_finder(task_id)
    if task is None:
        return jsonify({"error": "No task of such"}), 404
    return jsonify(task)

# Creates a new task
@views.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter

    info = request.get_json()
    if not info or "description" not in info or "title" not in info:
        return jsonify({"error": "Invalid request"}), 400
    
    n_task = {
        "id": id_counter,
        "title": info["title"],
        "description": info["description"],
        "completed": False
    }
    tasks.append(n_task)
    id_counter += 1
    return jsonify(n_task), 201


# Returns all users
@views.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Gets a user
@views.route("/user", methods=["POST"])
def create_user():
    global task_id_counter
    user = request.get_json()
    if not user or "email" not in user or "username" not in user:
        return jsonify({"error": "Invalid request"}), 400
        n_task = {
                "id": user["id"],
                "username": user["username"],
                "description": user["emsil"],
                }
    return jsonify(n_task), 201
