import json

from flask import request, abort

from models import TodoItem
from views.helper import APIView


class AddNewTodoItemView(APIView):

    def post(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        data = request.data
        print(data)
        data = json.loads(data)
        content = data.get('content')
        if not content:
            return abort(400, 'no content posted')
        new_item = TodoItem(todo_list_id=todo_list_id, content=content)
        self.session.add(new_item)
        self.session.commit()
        return json.dumps(new_item.serialize())


class ListAllTodoItemsByListView(APIView):

    def get(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        try:
            todo_item = TodoItem.query.filter_by(todo_list_id=todo_list_id)
            self.session.commit()
            return f'{todo_item.serialize()}'
        except AttributeError:
            return f"No list with ID {todo_list_id} found!"


class ListAllTodoItems(APIView):

    def get(self, **kwargs):
        todo_items = TodoItem.query.all()
        return json.dumps([l.serialize() for l in todo_items])
