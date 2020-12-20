from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import operator
import os

load_dotenv()
app = Flask(__name__)

# set up postgres database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# import Todo model
from models import Todo
db.create_all()


@app.route('/')
def index():
    # get all Todo objects currently in db
    todo_list = Todo.query.all()
    # continue to display to-do list in same order
    sorted_list = sorted(todo_list, key=operator.attrgetter("id"))
    return render_template('index.html', todo_list=sorted_list)


@app.route('/add', methods=['POST'])
def add():
    # add new Todo item
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:todo_id>')
def update(todo_id):
    # mark item as done
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # delete item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
