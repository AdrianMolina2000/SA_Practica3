from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

def hash_str(str):
    return hashlib.sha256(str.encode()).hexdigest()

auth = Blueprint('auth', __name__,url_prefix='/auth')
@auth.route('/login', methods=['POST', 'GET', 'PUT', 'DELETE'])
def login():
    if request.method == 'POST':
        try:
            email = request.json['email']
            password = hash_str(request.json['password'])
        except:
            return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para logearse'})
          
        expiracion = dt.utcnow()+td(minutes=30)
        encoded = jwt.encode({"id": 1, "password": password, "exp" : expiracion}, "secret", algorithm="HS256")
        retorno = {'token' : encoded, "status": 200}
        return jsonify(retorno)
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})