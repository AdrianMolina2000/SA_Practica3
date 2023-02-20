from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt


pensum = Blueprint('pensum', __name__,url_prefix='/pensum')
@pensum.route('/sendPensumUser', methods=['POST', 'GET', 'PUT', 'DELETE'])
def send_pensum_user():
    if request.method == 'POST':
        try:
            token = request.headers.get('Token')
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                carne = request.json['carne']
                code_course = request.json['code_course']

                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El carne no coincide con el usuario logeado'})
                if code_course == "":
                    return jsonify({'status': 400, 'descripcion': 'El codigo del curso no puede estar vacio'})


                return jsonify({"status" : 200})
            except:
                return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})


@pensum.route('/getPensumUser', methods=['POST', 'GET', 'PUT', 'DELETE'])
def get_pensum_user():
    if request.method == 'GET':
        try:
            token = request.headers.get('Token')
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                carne = request.json['carne']

                if carne != tokenDatos['id']:
                    return jsonify({'status': 400, 'descripcion': 'El usuario no ha sido encontrado'})
                
                return jsonify({"status" : 200, 
                                "courses" : 
                                [
                                    {"code_course" : "0780", "name_course" : "Software Avanzado"},
                                    {"code_course" : "0972", "name_course" : "Inteligencia Artificial 1"}
                                ]
                            })

            except:
                return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400})
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})