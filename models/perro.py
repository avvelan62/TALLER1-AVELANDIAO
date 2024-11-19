from database.db import db

class Perro(db.Model):
    __tablename__ = "perro"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nombre = db.Column(db.String(45), nullable = False)
    raza = db.Column(db.String(45), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    peso = db.Column(db.Numeric(5,2), nullable = False)
