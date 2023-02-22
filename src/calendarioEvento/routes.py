from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib


def hash_str(str):
    return hashlib.sha256(str.encode()).hexdigest()


calendarioEvento = Blueprint('calendariocalendarioEvento', __name__,
                      url_prefix='/calendariocalendarioEvento')


@calendarioEvento.route('/getAllEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getEvent():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp", None)

            try:
                return jsonify(
                    {
                        "status": 200,
                        "list_calendarioEventos": [
                            {
                                "id": 1,
                                "carne": 201902934,
                                "title": "Conferencia SOA",
                                "msg": "Se realizara una conferencia hablando sobre…",
                                "fecha": "11/02/2023"
                            }
                        ]
                    }

                )
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener calendarioEventos'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion": "JWT ya expiro", "status": 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion": "Error en token enviado", "status": 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@calendarioEvento.route('/sendEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def setEvent():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne = request.json['carne']
                title = request.json['tittle']
                msg = request.json['msg']
                fecha = request.json['fecha']

                if carne == "":
                    return jsonify({'status': 400, 'descripcion': 'El carne no puede estar vacio'})
                if title == "":
                    return jsonify({'status': 400, 'descripcion': 'El titulo no puede estar vacio'})
                if msg == "":
                    return jsonify({'status': 400, 'descripcion': 'El mensaje no puede estar vacio'})
                if fecha == "":
                    return jsonify({'status': 400, 'descripcion': 'La fecha no puede estar vacia'})

                if carne != "201902934":
                    return jsonify({'status': 400, 'descripcion': 'El carnet no existe'})

                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar calendarioEvento'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@calendarioEvento.route('/gestionarEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def gestionarEvent():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                id_calendarioEvento = request.json['id_calendarioEvento']
                id_usuario = request.json['id_usuario']
                opcion = request.json['opcion']

                if id_calendarioEvento == "":
                    return jsonify({'status': 400, 'descripcion': 'El id del calendarioEvento no puede estar vacio'})
                if id_usuario == "":
                    return jsonify({'status': 400, 'descripcion': 'El id del usuario no puede estar vacio'})
                if opcion == "":
                    return jsonify({'status': 400, 'descripcion': 'La opcion no puede estar vacia'})

                if id_usuario != "1":
                    return jsonify({'status': 400, 'descripcion': 'El carnet no existe'})
                if id_calendarioEvento != "0":
                    return jsonify({'status': 400, 'descripcion': 'El calendarioEvento no existe'})
                if opcion != "0" and opcion != "1":
                    return jsonify({'status': 400, 'descripcion': 'La opcion no es valida'})
                
                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar calendarioEvento'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})
    
@calendarioEvento.route('/deleteEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def deleteEvent():
    if request.method == 'DELETE':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                id_calendarioEvento = request.json['id_calendarioEvento']

                if id_calendarioEvento == "":
                    return jsonify({'status': 400, 'descripcion': 'El id_calendarioEvento no puede estar vacio'})
                if id_calendarioEvento != "0":
                    return jsonify({'status': 400, 'descripcion': 'El calendarioEvento no existe'})

                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar calendarioEvento'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})