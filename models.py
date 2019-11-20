from app import db


class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    url = db.Column(db.String())
    lat = db.Column(db.Float())
    lon = db.Column(db.Float())
    adress = db.Column(db.String(150))
    description = db.Column(db.Text())
    mean_price = db.column(db.Float())
    rating = db.column(db.Float())

    def __init__(self, name, url, lat, lon, adress, mean_price, rating):
        self.name = name
        self.url = url
        self.lat = lat
        self.lon = lon
        self.adress = adress
        self.mean_price = mean_price
        self.rating = rating

    def __repr__(self):
        return '<name {}>'.format(self.name)
