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


class GetTodoItemsView(APIView):

    def get(self, **kwargs):
        todo_list_id = kwargs.get('todo_list_id')
        todo_item = list(TodoItem.query.filter_by(todo_list_id=todo_list_id))
        if todo_item:
            return json.dumps([l.serialize() for l in todo_item])
        return f"No list with ID {todo_list_id} found!"


class DeleteTodoItemsView(APIView):

    def delete(self, **kwargs):
        todo_item_id = kwargs.get('todo_item_id')
        try:
            TodoItem.query.filter_by(id=todo_item_id).delete()
            self.session.commit()
            return f'Item with ID {todo_item_id} deleted'
        except AttributeError:
            return f"No item with ID {todo_item_id} found!"


class UpdateTodoItemView(APIView):

    def post(self, **kwargs):
        todo_item_id = kwargs.get('todo_item_id')
        data = request.data
        if not data:
            return abort(400, "Please provide a new name")
        data = json.loads(data)
        content = data.get('content')
        try:
            todo_list = TodoItem.query.filter_by(id=todo_item_id).first()
            todo_list.content = content
            self.session.commit()
            return json.dumps(todo_list.serialize())
        except AttributeError:
            return f"No item with ID {todo_item_id} found!"


class ListAllTodoItems(APIView):

    def get(self, **kwargs):
        todo_items = TodoItem.query.all()
        return json.dumps([l.serialize() for l in todo_items])
