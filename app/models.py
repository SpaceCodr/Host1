from datetime import datetime
from flask_login import UserMixin
from config import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ownership = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.Text, nullable=True)
    media_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Videos('{self.title}', '{self.ownership}', '{self.genre}', '{self.release_year}')"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
