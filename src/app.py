from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.route("/")

def hello():
    return "Hello world"

@app.route("/signup")
def signup_user():
    name = request.args.get('name')
    password = request.args.get('password')
    try: 
        user=User(
            name=name,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return "Welcome {}".format(user.name)
    except Exception as e:
        return (str(e))

@app.route("/showusers")
def show_users():
    try:
        users=User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return (str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try: 
        user = User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
        return (str(e))

@app.route("/name/<name>")

def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_bok_details():
    author = request.args.get('author')
    published = request.args.get('pubished')
    return "Author: {}, Published: {}".format(author,published)


@app.route("/users")
def get_all_users():
    users = ['Kalle', 'Pelle', 'Lelle', 'Kjelle']
    listOfUsers = ""
    for user in users:
        listOfUsers += "\n{}".format(user)
    return listOfUsers

@app.route("/<name>")
def get_user(name):
    return "This is your profile {}".format(name)

if __name__ == '__main__':
    app.run