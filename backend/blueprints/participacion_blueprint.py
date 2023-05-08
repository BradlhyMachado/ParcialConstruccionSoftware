from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_participacion_model import participacionModel
model = participacionModel()


participacion_blueprint = Blueprint('participacion_blueprint', __name__)


@participacion_blueprint.route('/participacion', methods=['PUT'])
@cross_origin()
def create_participacion():
    content = model.create_participacion(request.json['fecha'], request.json['nota_final'], request.json['id_horario'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['PATCH'])
@cross_origin()
def update_participacion():
    content = model.update_participacion(request.json['id_participacion'], request.json['fecha'], request.json['nota_final'], request.json['id_horario'])     
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['DELETE'])
@cross_origin()
def delete_participacion():
    return jsonify(model.delete_participacion(int(request.json['id_participacion'])))

@participacion_blueprint.route('/participacion', methods=['POST'])
@cross_origin()
def participacion():
    return jsonify(model.get_participacion(int(request.json['id_participacion'])))

@participacion_blueprint.route('/participacions', methods=['POST'])
@cross_origin()
def participacions():
    return jsonify(model.get_participacions())