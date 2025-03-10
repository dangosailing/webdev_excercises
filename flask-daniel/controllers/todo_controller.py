from models.todo_model import Todo
import json


def read_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def write_todos(todos):
    with open("todos.json", "w") as file:
        json.dump(todos, file, indent=4)


def get_all_todos():
    todos = read_todos()
    return [Todo(**todo).to_dict() for todo in todos]


def get_one_todo(id: int):
    todos = read_todos()
    for todo in todos:
        if todo["id"] == id:
            return Todo(**todo).to_dict()


def create_new_todo(title: str):
    todos = read_todos()
    new_todo = Todo(id=len(todos) + 1, title=title, status=False)
    todos.append(new_todo.to_dict())
    write_todos(todos)
    return new_todo.to_dict()


def update_todo(id: int, title: str, status: bool):
    todos = read_todos()
    for todo in todos:
        if todo["id"] == id:
            if title:
                todo["title"] = title
            if status:
                todo["status"] = status
            write_todos(todos)
            return todo
    return None

def delete_todo(todo_id:int):
    todos = read_todos()
    updated_list_todos = []
    for todo in todos:
        if todo["id"] != todo_id:
            updated_list_todos.append(todo)
    # If no match, length remains the same
    if len(updated_list_todos) == len(todos):
        return None
    write_todos(updated_list_todos)
    return True
            
            
            