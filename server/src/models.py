from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()


class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    director = db.Column(db.STring)


class ShowTime(db.Model, SerializerMixin):
    __tablename__ = 'showtimes'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)


class Theater(db.Model, SerializerMixin):
    __tablename__ = 'theater'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
