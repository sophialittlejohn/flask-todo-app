from flask import Blueprint

from views.todo_item import AddNewTodoItemView, ListAllTodoItemsByListView, ListAllTodoItems
from views.todo_list import ListAllTodoIListsView, TodoListGetUpdateDeleteView, AddNewTodoListView

todo_items_api = Blueprint('todo_items_api', 'todo_items_api')
todo_lists_api = Blueprint('todo_lists_api', 'todo_lists_api')


todo_items_api.add_url_rule('<int:todo_list_id>/new/', view_func=AddNewTodoItemView.as_view('new-todo-items'))
todo_items_api.add_url_rule('<int:todo_list_id>/all/', view_func=ListAllTodoItemsByListView.as_view('list-all-td-items'))
todo_items_api.add_url_rule('all/', view_func=ListAllTodoItems.as_view('list-all-todo-items'))


todo_lists_api.add_url_rule('/all/', view_func=ListAllTodoIListsView.as_view('list-all-todos'))
todo_lists_api.add_url_rule('/<int:todo_list_id>/', view_func=TodoListGetUpdateDeleteView.as_view('g-d-u-todo-list'))
todo_lists_api.add_url_rule('/new-list/', view_func=AddNewTodoListView.as_view('add-new-todo-list'))
