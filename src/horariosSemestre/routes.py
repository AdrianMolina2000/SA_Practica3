from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

horariosSemestre = Blueprint('horariosSemestre', __name__,url_prefix='/horariosSemestre')
@horariosSemestre.route('/addHorarioCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def addhorariocurso():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                code_course = request.json['code_course']
                code_doce = request.json['code_doce']
                section = request.json['section']
                hour_init = request.json['hour_init']
                hour_finish = request.json['hour_finish']
                dates = request.json['dates']

                if code_course == "":
                    return jsonify({'status': 400, 'descripcion': 'El codigo del curso no existe'}),400
                if code_doce <= 0:
                    return jsonify({'status': 400, 'descripcion': 'El codigo del docente no existe'}),400
                if section == "":
                    return jsonify({'status': 400, 'descripcion': 'Seccion no puede estar vacio'}),400
                if hour_init == "":
                    return jsonify({'status': 400, 'descripcion': 'Hora de inicio no puede estar vacio'}),400
                if hour_finish == "":
                    return jsonify({'status': 400, 'descripcion': 'Hora de finalizar no puede estar vacio'}),400
                if len(dates) <= 0:
                    return jsonify({'status': 400, 'descripcion': 'Lista de dias no puede estar vacio'}),400
                for day in dates:
                    if day != "Lunes" and day != "Martes" and day != "Miercoles" and day != "Jueves" and day != "Viernes" and day != "Sabado" and day != "Domingo":
                        return jsonify(({'status': 400, 'descripcion': f'Dia {day} no valido'}))
                return jsonify({"status" : 200, "descripcion" : "Se ha agregado el horario correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar horario de curso'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500

@horariosSemestre.route('/removeHorarioCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def removehorario():
    if request.method == 'DELETE':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                code_course = request.json['code_course']
                section = request.json['section']
                if code_course == "":
                    return jsonify({'status': 400, 'descripcion': 'El codigo del curso no existe'}),400
                if section == "":
                    return jsonify({'status': 400, 'descripcion': 'La seccion no debe estar vacia'}),400
                return jsonify({"status" : 200, "descripcion" : "Se ha eliminado el horario correctamente"}),200
            except:
                 return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar horario del curso'}),400
            
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500

@horariosSemestre.route('/getHorariosCursos', methods=['POST', 'GET',  'PUT', 'DELETE'])
def gethorario():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            try:
                
                return ({'status': 200, 'course': [
                    {
                        "code_course" : 780,
                        "name_course" : "Software Avanzado",
                        "credit_course" : 8,
                        "pre_course" : [ 785 ],
                        "optional" : 1
                    }

                ]}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener los cursos'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500