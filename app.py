from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from dotenv import load_dotenv
import os
from database.db import db
from controllers.guarderia_controller import guarderia_blueprint
from controllers.cuidador_controller import cuidador_blueprint
from controllers.perro_controller import perro_blueprint

load_dotenv()
app = Flask(__name__, template_folder="views")

secret_key = os.urandom(24)
app.config['SECRET_KEY'] = secret_key

app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}'
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(guarderia_blueprint)
app.register_blueprint(cuidador_blueprint)
app.register_blueprint(perro_blueprint)

login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id, username, password, is_admin) -> None:
        self.id = user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin

users = [
    User(1, "avelandia", "123456", True),
    User(2, "aortiz", "123456", False),
    User(3, "mortiz", "123456", False)
]

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ruta-logueada')
@login_required # Indica que es requerido ser logueado para ingresar a la ruta
def ruta():
    return render_template("ruta-logueada.html")


@app.route('/admin-dashboard')
@login_required # Indica que es requerido ser logueado para ingresar a la ruta
def dashboard_admin():
    if  current_user.is_admin:
        return redirect(url_for('perro_bp.index'))
    return redirect(url_for('ruta'))


@app.route('/login', methods=["GET", "POST"])
def Login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if user.username == username and user.password == password:
                login_user(user)
                flash('Inicio de sesión exitoso', 'success')
                if user.is_admin:
                    return redirect(url_for('dashboard_admin'))
            
                return redirect(url_for('ruta'))

