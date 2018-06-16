from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo, get_all_td
from wtforms import Form, StringField, validators


class TodoForm(Form):
    content = StringField('content', [validators.InputRequired(), validators.Length(max=20)])


@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.query.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/add', methods=['POST'])
def add():
    form = TodoForm(request.form)
    # content = request.form['content']
    if request.method == 'POST' and form.validate():
        content = form.content.data
        todo = Todo(content)
        todo.add()
        return redirect(url_for('index'))
    todos = Todo.query.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first_or_404()
    todo.delete()
    return redirect(url_for('index'))


@app.route('/done/<int:todo_id>')
def done(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first_or_404()
    if todo.status == 0:
        todo.status = 1
    else:
        todo.status = 0
    todo.add()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
