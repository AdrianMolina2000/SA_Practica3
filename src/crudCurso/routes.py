from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

crudCurso = Blueprint('crudCurso', __name__,url_prefix='/crudCurso')
@crudCurso.route('/setcurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def setcurso():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                code_course = request.json['code_course']
                name_course = request.json['name_course']
                credit_course = request.json['credit_course']
                pre_course = request.json['pre_courses']
                optional = request.json['optional']

                if code_course == "":
                    return jsonify({'status': 400, 'descripcion': 'El codigo del curso no puede estar vacion'}),400
                if name_course == "":
                    return jsonify(({'status': 400, 'description': 'Nombre del curso no puede estar vacion'})),400
                if credit_course < 0:
                    return jsonify(({'status': 400, 'description': 'Creditos del curso no pueden ser negativos'})),400
                if len(pre_course) > 0:
                    for course in pre_course:
                        if course == "":
                            return jsonify({'status': 400, 'descripcion': f'El codigo {course} del pre-curso no existe'}),400
                if optional < 0 or optional > 1:
                    return jsonify(({'status': 400, 'description': 'Valor de opcional no valido'})),400

                        
                return jsonify({"status" : 200, "descripcion" : "Se ha creado el curso correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar curso'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400

    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500

@crudCurso.route('/deleteCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def deletecurso():
    if request.method == 'DELETE':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                code_course = request.json['code_course']
                if code_course == "":
                    return jsonify(({'status': 400, 'descripcopn': 'Codigo del curso no existe'})),400
                return jsonify({'status': 200, "descripcion" : "Se ha eliminado el curso correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar curso'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500

@crudCurso.route('/getAllCursos', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getallcursos():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
            try:
                tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
                tokenDatos.pop("exp",None)

                return jsonify({
                    'status': 200,
                    'courses': [
                        {"code_course": "0780", "name_course": "Software Avanzado", "credit_course": 8, "pre_course": [785], "optiona": 1}
                    ]}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener los cursos'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500