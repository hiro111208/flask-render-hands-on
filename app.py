from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv(override=True)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
    'SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy(app)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(128), nullable=False)


@app.route('/')
def index():
    data = ToDo.query.all()
    return render_template('todo.html', data=data)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    new_todo = ToDo(todo=todo)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()
