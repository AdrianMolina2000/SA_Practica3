from flask import Flask
from flask_cors import CORS

from auth.routes import auth
from perfil.routes import perfil
from comunidad.routes import comunidad
from pensum.routes import pensum
from crudCurso.routes import crudCurso
from horariosSemestre.routes import horariosSemestre
from crudDocente.routes import crudDocente
from calendarioEvento.routes import calendarioEvento

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(auth)
    app.register_blueprint(perfil)
    app.register_blueprint(comunidad)
    app.register_blueprint(pensum)
    app.register_blueprint(crudCurso)
    app.register_blueprint(horariosSemestre)
    app.register_blueprint(crudDocente)
    app.register_blueprint(calendarioEvento)

    return app
    