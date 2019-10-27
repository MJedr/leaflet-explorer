from app import db
from models import Restaurant


r = Restaurant(name="Ciao a tutti", rating=5,
               adress="aleja Niepodległości 217, 02-087 Warszawa",
               url="https://www.facebook.com/ciaotuttipizza/",
               mean_price=50, lon=52.217447, lat=21.004316)
db.session.add(r)
db.session.commit()