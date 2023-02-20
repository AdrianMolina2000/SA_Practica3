from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

crudCurso = Blueprint('crudCurso', __name__,url_prefix='/crudCurso')
@crudCurso.route('/setcurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def setcurso():
    if request.method == 'POST':
        try:
            code_course = request.json['code_course']
            name_course = request.json['name_course']
            credit_course = request.json['credit_course']
            pre_course = request.json['pre_course']
            optional = request.json['optional']

            if code_course <= 0:
                return jsonify({'status': 400, 'descripcion': 'El codigo del curso no existe'})
            if name_course == "":
                return jsonify(({'status': 400, 'description': 'Nombre del curso no puede estar vacion'}))
            if credit_course < 0:
                return jsonify(({'status': 400, 'description': 'Creditos del curso no pueden ser negativos'}))
            if len(pre_course) > 0:
                for course in pre_course:
                    if course <= 0:
                        return jsonify({'status': 400, 'descripcion': 'El codigo del pre-curso no existe'})
            if optional < 0 or optional > 1:
                return jsonify(({'status': 400, 'description': 'Valor de opcional no valido'}))

                    
            return jsonify({"status" : 200})
        except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar curso'})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@crudCurso.route('/deleteCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def deletecurso():
    if request.methods == 'DELETE':
        try:
            code_course = request.json['code_course']
            if code_course <= 0:
                return jsonify(({'status': 400, 'descripcopn': 'Codigo del curso no existe'}))
            return jsonify({'status': 200})
        except:
            return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar curso'})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@crudCurso.route('/getAllCursos', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getallcursos():
    if request.method == 'GET':
        try:
            return jsonify({
                'status': 200,
                'courses': [
                    {"code_course": 780, "name_course": "Software Avanzado", "credit_course": 8, "pre_course": [785], "optiona": 1}
                ]})
        except:
            return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener los cursos'})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})