from models.cuidador import Cuidador
from models.perro import Perro
from flask import jsonify, Blueprint

cuidador_blueprint = Blueprint('cuidador_bp', __name__, url_prefix='/cuidador')

@cuidador_blueprint.route('/')
def index():
    cuidador = Cuidador.query.all()
    return jsonify({"data": cuidador[0].nombre}), 201
