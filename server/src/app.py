from flask import Flask
from models import db, Movie, ShowTime, Theater
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)



@app.route('/')
def root():
    return "hello", {}
