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
            carne = int(request.json['carne'])
            password = hash_str(request.json['password'])
        except:
            return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para logearse'}),400

        #VALIDAR QUE LOS DATOS NO VENGAN VACIOS
        if carne == "":
                return jsonify({'status': 400, 'descripcion': 'El carne no puede estar vacio'}),400
        if password == "":
                return jsonify({'status': 400, 'descripcion': 'La contraseña no puede estar vacio'}),400

        #VALIDACIONES DATOS QUEMADOS
        print(carne)
        if str(carne) == "201901510" or str(carne) == "201903850":
                if str(password) != "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4":
                        return jsonify({'status': 400, 'descripcion': 'Contraseña incorrecta'}),400
        else:
                return jsonify({'status': 400, 'descripcion': 'Usuario no encontrado'}),400
                
          
        expiracion = dt.utcnow()+td(minutes=30)
        encoded = jwt.encode({"carne": carne, "password": password, "exp" : expiracion}, "secret", algorithm="HS256")
        retorno = {'token' : encoded, "status": 200}
        return jsonify(retorno),200
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500



@auth.route('/registry', methods=['POST', 'GET', 'PUT', 'DELETE'])
def registry():
    if request.method == 'POST':
        try:
            name = request.json['name']
            lastname = request.json['lastname']
            carne = str(request.json['carne'])
            cui = request.json['cui']
            email = request.json['email']
            password = hash_str(request.json['password'])
            fecha_nac = request.json['fecha_nac']
            cel = request.json['cel']
        except:
             return jsonify({'status': 400, 'descripcion': 'Datos incompletos para registrarse'}),400


        #VALIDAR QUE LOS DATOS NO VENGAN VACIOS
        if name == "":
                return jsonify({'status': 400, 'descripcion': 'El nombre no puede estar vacio'}),400
        if lastname == "":
                return jsonify({'status': 400, 'descripcion': 'El apellido no puede estar vacio'}),400
        if carne == "":
                return jsonify({'status': 400, 'descripcion': 'El carne no puede estar vacio'}),400
        if cui == "":
                return jsonify({'status': 400, 'descripcion': 'El cui no puede estar vacio'}),400
        if email == "":
                return jsonify({'status': 400, 'descripcion': 'El email no puede estar vacio'}),400
        if password == "":
                return jsonify({'status': 400, 'descripcion': 'La contraseña no puede estar vacio'}),400
        if fecha_nac == "":
                return jsonify({'status': 400, 'descripcion': 'La fecha de nacimiento no puede estar vacio'}),400
        if cel == "":
                return jsonify({'status': 400, 'descripcion': 'El numero de telefono no puede estar vacio'}),400

        #VALIDACIONES DATOS QUEMADOS
        if carne == "201901510" :
               return jsonify({'status': 400, 'descripcion': 'El carné ingresado ya se encuentra registrado'}) ,400
        elif carne == "201903850" :
               return jsonify({'status': 400, 'descripcion': 'El carné ingresado ya se encuentra registrado'}) ,400
         
        retorno = {"descripcion" : "Se ha registrado Correctamente", "status": 200}
        return jsonify(retorno),200
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500