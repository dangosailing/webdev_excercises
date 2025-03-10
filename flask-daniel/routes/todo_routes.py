from flask import Blueprint, jsonify, request
from controllers.todo_controller import (
    get_all_todos,
    get_one_todo,
    create_new_todo,
    update_todo,
    delete_todo,
)

todo_routes = Blueprint("todo_routes", __name__)

@todo_routes.route("/", methods=["GET"])
def get_todos():
    return jsonify(get_all_todos())

@todo_routes.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    return jsonify(get_one_todo(todo_id))


@todo_routes.route("/", methods=["POST"])
def add_todos():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing data"})
    new_todo = create_new_todo(title=data["title"])
    return jsonify(new_todo), 201


@todo_routes.route("/<int:todo_id>", methods=["PUT"])
def edit_todo(todo_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data"})
    if not "status" in data.keys() or not "title" in data.keys():
        return jsonify({"error": "Missing data"})
    updated_todo = update_todo(
    id=todo_id, title=data["title"], status=data["status"]
    )
    if update_todo:
        return jsonify(updated_todo)
    return jsonify({"error": "Todo not found"}), 400


@todo_routes.route("/<int:todo_id>", methods=["DELETE"])
def remove_todo(todo_id):
    if delete_todo(todo_id):
        return jsonify({"message": "Todo deleted"})
    return jsonify({"error": "Todo not found"}), 400
