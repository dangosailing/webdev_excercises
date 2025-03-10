from flask import Blueprint, jsonify, render_template
from controllers.todo_controller import (
    get_all_todos,
)

view_routes = Blueprint("view_routes", __name__)

@view_routes.route("/", methods=["GET"])
def view_todos():
    return render_template("todos.html")