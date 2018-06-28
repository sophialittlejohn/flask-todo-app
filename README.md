# Todo App API with Flask

This is a simple API written in with Flask running in a Docker container.

## Endpoints 

- ``/todo-items/<int:todo_list_id>/new/``
- ``/todo-items/<int:todo_list_id>/all/``
- ``/todo-items/delete/<int:todo_item_id>``
- ``/todo-items/update/<int:todo_item_id>``
- ``/todo-items/all/``
- ``/todo-items/<int:todo_item_id>/done``


- ``/todo-lists/all/``
- ``/todo-lists/<int:todo_list_id>/``
- ``/todo-lists/new-list/``
- ``/todo-lists/search/``


## Usage

Clone the repository to you machine:

``git clone git@github.com:sophialittlejohn/flask-todo-app.git``

Build the Docker container:

``docker build -t sophialj/flask-todo-app:latest``

Start the Docker container:

``docker-compose up -d``

You can now view the endpoints at [http://localhost:8000]()