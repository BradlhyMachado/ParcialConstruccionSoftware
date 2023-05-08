from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_profesor_model import profesorModel
model = profesorModel()

profesor_blueprint = Blueprint('profesor_blueprint', __name__)

@profesor_blueprint.route('/profesor', methods=['PUT'])
@cross_origin()
def create_profesor():
    content = model.create_profesor(request.json['asignatura_profesor'], request.json['usuario_dni'], request.json['usuario_nombre'], request.json['usuario_apellido'], request.json['usuario_telefono'], request.json['usuario_correo'], request.json['usuario_contraseña'], request.json['usuario_vector'], request.json['usuario_ruta'])    
    return jsonify(content)

@profesor_blueprint.route('/profesor', methods=['PATCH'])
@cross_origin()
def update_profesor():
    content = model.update_profesor(request.json['id_profesor'], request.json['asignatura_profesor'], request.json['usuario_dni'], request.json['usuario_nombre'], request.json['usuario_apellido'], request.json['usuario_telefono'], request.json['usuario_correo'], request.json['usuario_contraseña'], request.json['usuario_vector'], request.json['usuario_ruta'])     
    return jsonify(content)

@profesor_blueprint.route('/profesor', methods=['DELETE'])
@cross_origin()
def delete_profesor():
    return jsonify(model.delete_profesor(int(request.json['dni'])))

@profesor_blueprint.route('/profesor', methods=['POST'])
@cross_origin()
def profesor():
    return jsonify(model.get_profesor(int(request.json['id_profesor'])))

@profesor_blueprint.route('/profesors', methods=['POST'])
@cross_origin()
def profesors():
    return jsonify(model.get_profesors())