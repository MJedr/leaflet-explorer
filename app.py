from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db) # this
Bootstrap(app)

from models import *


@app.route('/')
def show_restaurants():
    restaurants = Restaurant.query.all()
    info = [[[restaurant.lon, restaurant.lat], restaurant.name] for restaurant in restaurants][-1]
    coords = info[0]
    name = info[1]
    return render_template('restaurants.html', coords=coords)


if "__main__" == __name__:
    app.run(debug=True)