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


@app.route('/')
def hello_world():
    return render_template('restaurants.html')


@app.route('/restauracje')
def show_restaurants():
    return render_template('map.html')


if "__main__" == __name__:
    app.run(debug=True)