from datetime import datetime
from database import db


class TodoItem(db.Model):
    __tablename__ = 'todo_item'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    done = db.Column(db.Boolean, default=False)
    todo_list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'), nullable=False)
    todo_list = db.relationship('TodoList', backref='todos', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'list-id': self.todo_list_id,
            'content': self.content,
            'created': self.created.strftime('%d, %b %Y'),
            'done': self.done
        }
