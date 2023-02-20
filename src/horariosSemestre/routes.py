from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

horariosSemestre = Blueprint('horariosSemestre', __name__,url_prefix='/horariosSemestre')
@horariosSemestre.route('/addHorarioCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def addhorariocurso():
    if request.method == 'POST':
        try:
            code_course = request.json['code_course']
            code_doce = request.json['code_doce']
            section = request.json['section']
            hour_init = request.json['hour_init']
            hour_finish = request.json['hour_finish']
            dates = request.json['dates']

            if code_course <= 0:
                return jsonify({'status': 400, 'descripcion': 'El codigo del curso no existe'})
            if code_doce <= 0:
                return jsonify({'status': 400, 'descripcion': 'El codigo del docente no existe'})
            if section == "":
                return jsonify({'status': 400, 'descripcion': 'Seccion no puede estar vacio'})
            if hour_init == "":
                return jsonify({'status': 400, 'descripcion': 'Hora de inicio no puede estar vacio'})
            if hour_finish == "":
                return jsonify({'status': 400, 'descripcion': 'Hora de finalizar no puede estar vacio'})
            if len(dates) <= 0:
                return jsonify({'status': 400, 'descripcion': 'Lista de dias no puede estar vacio'})
            for day in dates:
                if day != "Lunes" and day != "Martes" and day != "Miercoles" and day != "Jueves" and day != "Viernes" and day != "Sabado" and day != "Domingo":
                    return jsonify(({'status': 400, 'descripcion': f'Dia {day} no valido'}))
            return jsonify({"status" : 200})
        except:
            return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar horario de curso'})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@horariosSemestre.route('/removeHorarioCurso', methods=['POST', 'GET', 'PUT', 'DELETE'])
def removehorario():
    if request.method == 'DELETE':
        try:
            code_course = request.json['code_course']
            if code_course <= 0:
                return jsonify({'status': 400, 'descripcion': 'El codigo del curso no existe'})
            return jsonify({"status" : 200})
        except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para eliminar horario del curso'})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})

@horariosSemestre.route('/getHorariosCursos', methods=['POST', 'GET',  'PUT', 'DELETE'])
def gethorario():
    if request.method == 'GET':
        try:
            return ({'status': 200, 'course': [
                {
                     "code_course" : 780,
                     "name_course" : "Software Avanzado",
                     "credit_course" : 8,
                     "pre_course" : [ 785 ],
                     "optional" : 1
                   }

            ]})
        except:
            return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para obtener los cursos'})
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'})