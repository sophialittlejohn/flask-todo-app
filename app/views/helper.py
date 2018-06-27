from flask.views import MethodView
from database import db


class APIView(MethodView):
    def __init__(self):
        super().__init__()
        self.session = db.session
