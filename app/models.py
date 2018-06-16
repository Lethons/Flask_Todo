from app import db
import datetime


class Todo(db.Model):
    # __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20))
    time = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(db.Integer, default=0)

    def __init__(self, content):
        self.content = content

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self.id
        except Exception as e:
            return e
        finally:
            return 0


def get_all_td():
    todo_list = []
    todo_list = Todo.query.filter_by().all()
    return todo_list
