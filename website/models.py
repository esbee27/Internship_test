from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

"""Creates model for database"""
class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    

