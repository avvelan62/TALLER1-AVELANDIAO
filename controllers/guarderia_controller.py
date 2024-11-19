from models.guarderia import Guarderia
from flask import jsonify, Blueprint

guarderia_blueprint = Blueprint('guarderia_bp', __name__, url_prefix='/guarderia')

@guarderia_blueprint.route('/')
def index():
    guarderia = Guarderia.query.all()
    return jsonify({"data": guarderia[0].nombre}), 201