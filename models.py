from app import db


class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    url = db.Column(db.String())
    lat = db.Column(db.Float())
    lon = db.Column(db.Float())
    adress = db.Column(db.String(150))
    description = db.Column(db.Text())
    mean_price = db.column(db.Float())
    rating = db.column(db.Float())

    def __init__(self, name, url, lat, lon, adress, mean_price, rating):
        self.name = name

    def __repr__(self):
        return '<name {}>'.format(self.name)
