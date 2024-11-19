from models.perro import Perro
from flask import Blueprint, render_template

perro_blueprint = Blueprint('perro_bp', __name__, url_prefix='/perro')

@perro_blueprint.route('/')
def index():
    perro = Perro.query.all()
    count_lassie = Perro.query.filter_by(nombre='Lassie').count()
    perros_mario = Perro.query.filter(Perro.peso < 3) 
    datos = [perro, count_lassie, perros_mario]
    return render_template("perros.html", perros = datos)

@perro_blueprint.route('/lassie/count')
def contar_lassie():
    count = Perro.query.filter_by(nombre='Lassie').count()
    return render_template("perros.html", lassie = count)
