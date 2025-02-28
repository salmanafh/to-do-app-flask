# to do list app
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [{
    "id": 1,
    "task": "build an API",
    "description": "using flask",
    "done": False
},
         {
    "id": 2,
    "task": "build a front end",
    "description": "using react",
    "done": False
         },
         {
    "id": 3,
    "task": "build a database",
    "description": "using postgres",
    "done": False
         },
         {
    "id": 4,
    "task": "deploy the app",
    "description": "using docker",
    "done": False
         },
         {
    "id": 5,
    "task": "test the app",
    "description": "using pytest",
    "done": False
         },
         {
    "id": 6,
    "task": "monitor the app",
    "description": "using prometheus",
    "done": False
         },
         ]

@app.route('/')
def index():
    return "Welcome to the to do list app"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    todo = [todo for todo in todos if todo['id'] == id]
    if len(todo) == 0:
        return "Todo not found", 404
    return jsonify(todo)

@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = {
        "id": todos[-1]['id'] + 1,
        "task": request.json['task'],
        "description": request.json['description'],
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo)

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo_by_id(id):
    todo = [todo for todo in todos if todo['id'] == id]
    if len(todo) == 0:
        return "Todo not found", 404
    todo[0]['task'] = request.json['task']
    todo[0]['description'] = request.json['description']
    todo[0]['done'] = request.json['done']
    return jsonify(todo)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo_by_id(id):
    todo = [todo for todo in todos if todo['id'] == id]
    if len(todo) == 0:
        return "Todo not found", 404
    todos.remove(todo[0])
    return "Todo deleted successfully"

if __name__ == '__main__':
    app.run(debug=True)