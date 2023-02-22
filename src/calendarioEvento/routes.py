from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib


def hash_str(str):
    return hashlib.sha256(str.encode()).hexdigest()


calendarioEvento = Blueprint('calendarioEvento', __name__,
                      url_prefix='/calendarioEvento')


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

                ),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener calendarioEventos'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion": "JWT ya expiro", "status": 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion": "Error en token enviado", "status": 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500

@calendarioEvento.route('/sendEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def setEvent():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)

            
            try:
                title = request.json['title']
                msg = request.json['msg']
                fecha = request.json['fecha']

                if title == "":
                    return jsonify({'status': 400, 'descripcion': 'El titulo no puede estar vacio'}),400
                if msg == "":
                    return jsonify({'status': 400, 'descripcion': 'El mensaje no puede estar vacio'}),400
                if fecha == "":
                    return jsonify({'status': 400, 'descripcion': 'La fecha no puede estar vacia'}),400

                

                return jsonify({"status" : 200, "descripcion": "Se agrego el evento correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar calendarioEvento'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),400

@calendarioEvento.route('/gestionarEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def gestionarEvent():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                id_evento = int(request.json['id_evento'])
                carne = int(request.json['carne'])
                opcion = int(request.json['opcion'])
                if id_evento == "":
                    return jsonify({'status': 400, 'descripcion': 'El id del evento no puede estar vacio'}),400
                if carne == "":
                    return jsonify({'status': 400, 'descripcion': 'El carne del usuario no puede estar vacio'}),400
                if opcion == "":
                    return jsonify({'status': 400, 'descripcion': 'La opcion no puede estar vacia'}),400

                if carne != 201902934:
                    return jsonify({'status': 400, 'descripcion': 'El carnet no existe'}),400
                if id_evento != 1:
                    return jsonify({'status': 400, 'descripcion': 'El id del evento no existe'}),400
                if opcion != 0 and opcion != 1:
                    return jsonify({'status': 400, 'descripcion': 'La opcion no es valida'}),400
                
                if opcion == 0:
                    asig = "Asignado al evento"
                elif opcion == 1:
                    asig = "Desasignado del evento"

                return jsonify({"status" : 200, "descripcion" : asig}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar calendarioEvento'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500
    
@calendarioEvento.route('/deleteEvent', methods=['POST', 'GET', 'PUT', 'DELETE'])
def deleteEvent():
    if request.method == 'DELETE':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                id_evento = int(request.json['id_evento'])

                if id_evento == "":
                    return jsonify({'status': 400, 'descripcion': 'El id del evento no puede estar vacio'}),400
                if id_evento != 1:
                    return jsonify({'status': 400, 'descripcion': 'El calendarioEvento no existe'}),400

                return jsonify({"status" : 200, "descripcion" : "evento eliminado correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar calendarioEvento'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500