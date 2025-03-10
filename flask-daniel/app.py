from flask import Flask
from routes.todo_routes import todo_routes
from routes.view_routes import view_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(todo_routes, url_prefix="/todos")
app.register_blueprint(view_routes, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
