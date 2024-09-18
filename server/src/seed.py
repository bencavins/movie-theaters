from app import app
from models import db, Movie, ShowTime, Theater
from datetime import datetime


def run():
    shining = Movie(title='The Shining', director='Stanley Kubrick')
    star_wars = Movie(title='Star Wars', director='George Lucas')

    db.session.add_all([shining, star_wars])

    amc = Theater(name='AMC')
    alamo = Theater(name='Alamo Drafthouse')

    db.session.add_all([amc, alamo])

    times = [
        ShowTime(movie=shining, theater=amc, time=datetime(year=2024, month=9, day=17, hour=12, minute=0, second=0)),
        ShowTime(movie=star_wars, theater=amc, time=datetime(year=2024, month=9, day=17, hour=13, minute=0, second=0)),
        ShowTime(movie=shining, theater=alamo, time=datetime(year=2024, month=9, day=17, hour=14, minute=0, second=0)),
        ShowTime(movie=star_wars, theater=alamo, time=datetime(year=2024, month=9, day=17, hour=15, minute=0, second=0)),
    ]

    db.session.add_all(times)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        run()
