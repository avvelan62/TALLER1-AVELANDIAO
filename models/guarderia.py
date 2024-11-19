from database.db import db

class Guarderia(db.Model):
    __tablename__ = "guarderias"
    # Modelando la información que esta en base de datos
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nombre = db.Column(db.String(100), nullable = False)
    direccion = db.Column(db.String(200), nullable = False)
    telefono = db.Column(db.String(20), nullable = False)