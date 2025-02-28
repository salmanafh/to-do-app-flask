# To-Do List App
A simple To-Do List API built using Flask.

## Features

* View all to-do tasks

* Retrieve a specific task by ID

* Create a new task

* Update an existing task

* Delete a task

## Installation 

1. Clone this repository:
`git clone https://github.com/your-repo/todo-list-app.git
cd todo-list-app`

2. Create a virtual environment and activate it:
`python -m venv venv
source venv/bin/activate  # On Windows use "venv\Scripts\activate"`

3. Install dependencies:
`pip install flask`

## Usage
1. Run the Flask app:
`python app.py`
3. The API will be accessible at http://127.0.0.1:5000/

## API Endpoints
### Get all tasks

**Endpoint:** `POST /api/example`

**Request Body:**
```
[
  {
    "id": 1,
    "task": "build an API",
    "description": "using flask",
    "done": false
  }
]
...
```

### Get a task by ID

* Endpoint: `GET/todos/<id>`
* Response:
```
{
  "id": 1,
  "task": "build an API",
  "description": "using flask",
  "done": false
}
```

### Create a new task

* Endpoint: `POST /todos`
* Request Body:
```
{
  "task": "New Task",
  "description": "Task description"
}
```

* Response:
```
{
  "id": 7,
  "task": "New Task",
  "description": "Task description",
  "done": false
}
```

### Update a task

* Endpoint: `PUT /todos/<id>`
* Request Body:
```
{
  "task": "Updated Task",
  "description": "Updated description",
  "done": true
}
```

* Response:
```
{
  "id": 1,
  "task": "Updated Task",
  "description": "Updated description",
  "done": true
}
```

### Delete a task

* Endpoint: DELETE /todos/<id>
* Response: "Todo deleted successfully"


## Dependencies

* Python 3.10.15
* Flask
