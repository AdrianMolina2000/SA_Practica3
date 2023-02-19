from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

def hash_str(str):
    return hashlib.sha256(str.encode()).hexdigest()

perfil = Blueprint('perfil', __name__,url_prefix='/perfil')
@perfil.route('/updateUser', methods=['POST', 'GET', 'PUT', 'DELETE'])
def updateUser():
    if request.method == 'PUT':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne = request.json['carne']
                name = request.json['name']
                lastname = request.json['lastname']
                email = request.json['email']
                fecha_nac = request.json['fecha_nac']
                cel = request.json['cel']
                password = hash_str(request.json['password'])
                
                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El carne no coincide con el usuario logeado'})
                if name == "":
                    return jsonify({'status': 400, 'descripcion': 'El nombre no puede estar vacio'})
                if lastname == "":
                    return jsonify({'status': 400, 'descripcion': 'El apellido no puede estar vacio'})
                if email == "":
                    return jsonify({'status': 400, 'descripcion': 'El email no puede estar vacio'})
                if fecha_nac == "":
                    return jsonify({'status': 400, 'descripcion': 'La fecha de nacimiento no puede estar vacia'})
                if cel == "":
                    return jsonify({'status': 400, 'descripcion': 'El numero de celular no puede estar vacio'})
                if password == "":
                    return jsonify({'status': 400, 'descripcion': 'La contraseña no puede estar vacia'})
                
                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para actualizar informacion'})
            
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@perfil.route('/getUser', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getInfo():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne = request.json['carne']

                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El carne no coincide con el usuario logeado'})
                
                return jsonify({"status" : 200, "carne" : "201903850", "name" : "Adrian", "lastname" : "Molina", 
                                "email" : "adriansmc@gmail.com", "fecha_nac" : "20/12/2000", "cel" : "55515147",
                                "cui" : "3020721280101"})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener informacion'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})
    
@perfil.route('/getCursos', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getCursos():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne = request.json['carne']

                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El carne no coincide con el usuario logeado'})
                
                return jsonify({"status" : 200, "total_credits" : 10, 
                                "courses" : [
                                                {"code" : 101, "name" : "Deportes 1", "credits" : 2},
                                                {"code" : 102, "name" : "Deportes 2", "credits" : 2},
                                                {"code" : 103, "name" : "Quimica", "credits" : 5}
                                            ]
                                })
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener informacion'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})
    
@perfil.route('/setCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def setCurso():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne = request.json['carne']
                code = request.json['code_course']

                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El carne no coincide con el usuario logeado'})
                if code == 0:
                    return jsonify({'status': 400, 'descripcion': 'El curso no existe'})
                
                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar curso'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@perfil.route('/deleteCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def deleteCurso():
    if request.method == 'DELETE':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne = request.json['carne']
                code = request.json['code_course']

                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El carne no coincide con el usuario logeado'})
                if code == 0:
                    return jsonify({'status': 400, 'descripcion': 'El curso no existe'})
                
                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar curso'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})