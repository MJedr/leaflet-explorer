from sqlalchemy import create_engine


class DbUtils:
    db_string = "postgresql+psycopg2://cysia:marcysia@localhost/mydb"

    def createTable(self):
        db = create_engine(self.db_string)
        db.execute("CREATE TABLE IF NOT EXISTS restaurants (title text, director text, year text)")

    def addNewRestaurant(self, title, director, year):
        db_string = "postgresql+psycopg2://admin:admin@localhost/postgres"
        db = create_engine(db_string)
        db.execute("INSERT INTO films(title, director, year) VALUES (%s,%s, %s)", title, director, year)
