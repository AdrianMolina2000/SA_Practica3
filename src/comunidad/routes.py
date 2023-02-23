from flask import request, jsonify, Blueprint
from datetime import datetime as dt, timedelta as td
import jwt
import hashlib

def hash_str(str):
    return hashlib.sha256(str.encode()).hexdigest()

comunidad = Blueprint('comunidad', __name__,url_prefix='/comunidad')

@comunidad.route('/setPost', methods=['POST', 'GET', 'PUT', 'DELETE'])
def setPost():
    if request.method == 'POST':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                carne =  tokenDatos['carne']
                title = request.json['title']
                msg = request.json['msg']
                tag = request.json['tag']

                if title == "":
                    return jsonify({'status': 400, 'descripcion': 'El titulo no puede estar vacio'}),400
                if msg == "":
                    return jsonify({'status': 400, 'descripcion': 'El mensaje no puede estar vacio'}),400
                if tag == "":
                    return jsonify({'status': 400, 'descripcion': 'El tag no puede estar vacio'}),400

                return jsonify({"status" : 200,  "descripcion" : "Se ha creado el post correctamente"}),200
            except:
                return jsonify({'status': 400, 'descripcion': 'Datos incorrectos para agregar curso'}),400
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500



@comunidad.route('/getPost', methods=['POST', 'GET', 'PUT', 'DELETE'])
def getPost():
    if request.method == 'GET':
        token = request.headers.get('Token')
        try:
            tokenDatos = jwt.decode(token, "secret", algorithms=["HS256"])
            tokenDatos.pop("exp",None)
            
            try:
                tag = request.json['tag']
                if tag == "":
                    return jsonify({'status': 400, 'descripcion': 'El tag no puede estar vacio'}),400
                return jsonify({"status" : 200, 
                                "posts" : 
                                [
                                    {"carne" : "201903850", "title" : "Como iniciar en redes1", "msg" : "descargar gns3", "tag" : "Redes 1"},
                                ]
                            })
            except:
                return jsonify({"status" : 200, 
                                "posts" : 
                                [
                                    {"carne" : "201903850", "title" : "Como iniciar en redes1", "msg" : "descargar gns3", "tag" : "Redes 1"},
                                    {"carne" : "201903850", "title" : "Como iniciar en redes2", "msg" : "descargar gns3", "tag" : "Redes 2"},
                                ]
                            }),200
        except jwt.ExpiredSignatureError:
            return jsonify({"descripcion" : "JWT ya expiro", "status" : 400}),400
        except jwt.InvalidTokenError:
            return jsonify({"descripcion"  : "Error en token enviado", "status" : 400}),400
    else:
        return jsonify({'status': 500, 'descripcion': 'Metodo no manejado'}),500