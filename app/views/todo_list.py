import json

from views.helper import APIView

from flask import abort, request
from models import TodoList


class ListAllTodoIListsView(APIView):
    def get(self, **kwargs):
        all_lists = TodoList.query.all()
        # result = []
        # for l in all_lists:
        #     result.append(l.serialize())
        # return json.dumps(result)
        return json.dumps([l.serialize() for l in all_lists])


class AddNewTodoListView(APIView):

    def post(self, **kwargs):
        data = request.data
        if not data:
            data = '{}'
        data = json.loads(data)
        name = data.get('name')
        if not name:
            return abort(400, 'no name posted')
        new_list = TodoList(name=name)
        self.session.add(new_list)
        self.session.commit()
        return name


class TodoListGetUpdateDeleteView(APIView):

    def get(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        try:
            todo_list = TodoList.query.filter_by(id=todo_list_id).first()
            return f'{todo_list.serialize()}'
        except AttributeError:
            return f"No list with ID {todo_list_id} found!"

    def delete(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        try:
            TodoList.query.filter_by(id=todo_list_id).delete()
            self.session.commit()
            return f'List with ID {todo_list_id} deleted'
        except AttributeError:
            return f"No list with ID {todo_list_id} found!"

    def post(self, **kwargs):
        # to change name of list
        todo_list_id = kwargs.get('todo_list_id')
        data = request.data
        data = json.loads(data)
        if not data:
            return abort(400, "Please provide a new name")
        name = data.get('name')
        try:
            todo_list = TodoList.query.filter_by(id=todo_list_id).first()
            todo_list.name = name
            self.session.commit()
            return json.dumps(todo_list.serialize())
        except AttributeError:
            return f"No list with ID {todo_list_id} found!"


class SearchTodoLists(APIView):

    def get(self, **kwargs):
        q = request.values.get('q')
        todo_lists = TodoList.query.filter(TodoList.name.like(f'%{q}%'))
        return json.dumps([l.serialize() for l in todo_lists])
