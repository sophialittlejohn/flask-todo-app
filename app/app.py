# create new todo
# list all existing todos
# delete todos
# search todos
import random
import string

from flask import Flask, request
from flask_migrate import Migrate

from database import db
from models import TodoList, TodoItem
from urls import todo_items_api, todo_lists_api

app = Flask(__name__)

# create the database file with sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_app.sqlite'
# this is so the command line doesnt complain
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


app.register_blueprint(todo_items_api, url_prefix='/todo-items')
app.register_blueprint(todo_lists_api, url_prefix='/todo-lists')


def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


@app.cli.command()
def create_dummy_data():
    for i in range(10):
        new_todo_list = TodoList(name=f'My new list: {random_string(20)}')
        for i2 in range(10):
            new_item = TodoItem(
                content=f'My new todo item: {random_string(10)}',
                todo_list=new_todo_list,
            )
            db.session.add(new_item)
    db.session.commit()


if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
