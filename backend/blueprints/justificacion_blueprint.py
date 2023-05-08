from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_justificacion_model import justificacionModel
model = justificacionModel()


justificacion_blueprint = Blueprint('justificacion_blueprint', __name__)


@justificacion_blueprint.route('/justificacion', methods=['PUT'])
@cross_origin()
def create_justificacion():
    content = model.create_justificacion(request.json['id_asistencia'], request.json['razon'], request.json['estado'])    
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['PATCH'])
@cross_origin()
def update_justificacion():
    content = model.update_justificacion(request.json['id_justificacion'], request.json['id_asistencia'], request.json['razon'], request.json['estado'])     
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['DELETE'])
@cross_origin()
def delete_justificacion():
    return jsonify(model.delete_justificacion(int(request.json['id_justificacion'])))

@justificacion_blueprint.route('/justificacion', methods=['POST'])
@cross_origin()
def justificacion():
    return jsonify(model.get_justificacion(int(request.json['id_justificacion'])))

@justificacion_blueprint.route('/justificacions', methods=['POST'])
@cross_origin()
def justificacions():
    return jsonify(model.get_justificacions())