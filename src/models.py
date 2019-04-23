
from flask import Flask, request, jsonify
from app import db
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'password' : self.password,
        }

class Notepad(db.Model):
    __tablename__ = 'notepad'

    note_pad_id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    person = db.relationship(User)
    notes = []

    def __init__(self, user, person):
        self.user = user
        self.person = person

    def __repr__(self):
        return '<note_pad_id {}>'.format(self.note_pad_id)
    
    def serialize(self):
        return {
            'user' : self.user,
            'note_pad_id' : self.note_pad_id,
            'notes' : self.notes,
            'person' : self.person
        }
    
    def add_note(title, text):
        try:
            note = Note(
                title=title,
                text=text
            )
            db.session.add(note)
            db.session.commit()
            notes.append(note)
            return jsonify(note.serialize())
        except Exception as e:
            return (str(e))

class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    title = db.Column(db.String())
    notepad_id = db.Column(db.Integer, db.ForeignKey('notepad.note_pad_id'))
    notepad = db.relationship(Notepad)

    def __init__(self, title, text, notepad):
        self.text = text
        self.title = title
        self.notepad = notepad

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id' : self.id,
            'text' : self.text,
            'title' : self.title,
            'notepad_id' : self.notepad_id
        }

class Notepad_Notes(db.Model):
    __tablename__ = 'notepad_notes'

    id = db.Column(db.Integer, primary_key=True)
    note_pad_id = db.Column(db.Integer, db.ForeignKey('notepad.note_pad_id'))
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id' : self.id,
            'note_id' : self.note_id,
            'note_pad_id' : self.note_pad_id,
        }
 















