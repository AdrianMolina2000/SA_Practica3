from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib


def hash_str(str):
    return hashlib.sha256(str.encode()).hexdigest()


crudDocente = Blueprint('crudDocente', __name__, url_prefix='/crudDocente')


@crudDocente.route('/getAllcrudDocente', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getcrudDocente():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
           
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp", None)
            
            #if "201901510" != str(tokenDatos['carne']):
            #    return jsonify({'status': 400, 'descripcion': 'El usuario no ha sido encontrado'}),400
              

            try:
                return jsonify(
                    {
                        "status": 200,
                        "lista_crudDocente":
                            [
                                {
                                    "id": 2,
                                    "email": "germanpc9@gmail.com",
                                    "name": "German Jose",
                                    "lastname": "Paz Cordon"
                                }
                            ]
                    }
                ),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener crudDocentes'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion": "JWT ya expiro", "status": 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion": "Error en token enviado", "status": 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500

@crudDocente.route('/addcrudDocente', methods=['POST', 'GET', 'PUT', 'DELETE'])
def postcrudDocente():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)

            #if "201903850" != str(tokenDatos['carne']):
            #    return jsonify({'status': 400, 'descripcion': 'El usuario no ha sido encontrado'}),400
            
            try:
                email = request.json['email']
                name = request.json['name']
                lastname = request.json['lastname']

                if email == "":
                    return jsonify({'status': 400, 'descripcion': 'El email no puede estar vacio'}),400
                if name == "":
                    return jsonify({'status': 400, 'descripcion': 'El nombre no puede estar vacio'}),400
                if lastname == "":
                    return jsonify({'status': 400, 'descripcion': 'El apellido no puede estar vacio'}),400
                
                if email == "germanpc90@gmail.com":
                    return jsonify({'status': 400, 'descripcion': 'El Docente ya existe.'}),400


                return jsonify({"status" : 200, "descripcion": "Se ha insertado el docente correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar crudDocente'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500
    
@crudDocente.route('/removecrudDocente', methods=['POST', 'GET', 'PUT', 'DELETE'])
def deletecrudDocente():
    if request.method == 'DELETE':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            #if "201903850" != str(tokenDatos['carne']):
            #   return jsonify({'status': 400, 'descripcion': 'El usuario no ha sido encontrado'}),400
            try:
                email = request.json['email']

                if email == "":
                    return jsonify({'status': 400, 'descripcion': 'El email no puede estar vacio'}),400
                
                if email != "germanpc9@gmail.com":
                    return jsonify({'status': 400, 'descripcion': 'El crudDocente no existe.'}),400

                return jsonify({"status" : 200, "descripcion": "Se ha eliminado el docente correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar crudDocente'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500