from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
app = Flask(__name__)

count=0

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Note, Notepad, Notepad_Notes

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
            password=password,
        )
        user.note_book = user.id
        db.session.add(user)
        db.session.commit()
        return "Welcome {}".format(user.name)
    except Exception as e:
        return (str(e))

@app.route("/<id_>/add/notepad")
def add_notepad(id_):
    try: 
        user=User.query.filter_by(id=id_).first()
        notepad=Notepad(
            user=user.id,
            person=user
        )
        db.session.add(notepad)
        db.session.commit()
        return "Added {}".format(notepad.user)
    except Exception as e:
        return (str(e))

@app.route("/<id_>/hello/note")
def get_by_noteid(id_):
        try:
            notepad= Notepad.query.filter_by(user=id_).first()
            note = Note(
                title="Kalles' note",
                text="This is my incredible note",
                notepad = notepad
            )
            db.session.add(note)
            notepad.notes.append(note)
            db.session.commit()
            return "Yes"
        except Exception as e:
            return (str(e))


@app.route("/<id_>/note", methods=['GET', 'POST'])
def get_note_by_id(id_):
    r = request
    if r.method == 'GET':
        try:
            user = User.query.filter_by(id=id_).first()
            notepad = Notepad.query.filter_by(user=id_).first()
            notes = Note.query.filter_by(notepad_id=notepad.note_pad_id).all()
            length = len(notes)
            note = notes[length-1]
            return jsonify(note.serialize())
        except Exception as e:
            return (str(e))
    if r.method == 'POST':
        try:
            jsonNote = json.loads(r.data)
            text = jsonNote['text']
            title = jsonNote['title']
            notepad= Notepad.query.filter_by(user=id_).first()
            note = Note(
                title=text,
                text=title,
                notepad = notepad
            )
            db.session.add(note)
            notepad.notes.append(note)
            db.session.commit()
            
            return ("this is text")
        except Exception as e:
            print(str(e))
            print(r.data)
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


@app.route("/users")
def get_all_users():
    users = ['Kalle', 'Pelle', 'Lelle', 'Kjelle']
    listOfUsers = ""
    for user in users:
        listOfUsers += "\n{}".format(user)
    return listOfUsers

if __name__ == '__main__':
    app.run