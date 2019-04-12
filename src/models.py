
from app import db


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
            'password' : self.password
        }

 















