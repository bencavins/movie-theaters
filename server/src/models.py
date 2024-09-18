from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


db = SQLAlchemy(metadata=MetaData(naming_convention=convention))


class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    director = db.Column(db.String)

    showtimes = db.relationship('ShowTime', back_populates='movie')
    theaters = association_proxy('showtimes', 'theater')

    serialize_rules = ['-showtimes.movie']

    def __repr__(self) -> str:
        return f'<Movie {self.title} {self.director}>'


class ShowTime(db.Model, SerializerMixin):
    __tablename__ = 'showtimes'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    theater_id = db.Column(db.Integer, db.ForeignKey('theaters.id'))

    movie = db.relationship('Movie', back_populates='showtimes')
    theater = db.relationship('Theater', back_populates='showtimes')

    serialize_rules = ['-movie.showtimes', '-theater.showtimes']

    def __repr__(self) -> str:
        return f'<ShowTime {self.time}>'


class Theater(db.Model, SerializerMixin):
    __tablename__ = 'theaters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    showtimes = db.relationship('ShowTime', back_populates='theater')
    movies = association_proxy('showtimes', 'movie', creator=lambda movie_obj: ShowTime(movie=movie_obj))

    serialize_rules = ['-showtimes.theater']

    def __repr__(self) -> str:
        return f'<Theater {self.name}>'
