from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_matricula_model import matriculaModel
model = matriculaModel()


matricula_blueprint = Blueprint('matricula_blueprint', __name__)


@matricula_blueprint.route('/matricula', methods=['PUT'])
@cross_origin()
def create_matricula():
    content = model.create_matricula(request.json['id_estudiante'], request.json['semestre'], request.json['carrera'], request.json['estado'], request.json['id_seccion'])    
    return jsonify(content)

@matricula_blueprint.route('/matricula', methods=['PATCH'])
@cross_origin()
def update_matricula():
    content = model.update_matricula(request.json['id_matricula'], request.json['id_estudiante'], request.json['semestre'], request.json['carrera'], request.json['estado'], request.json['id_seccion'])     
    return jsonify(content)

@matricula_blueprint.route('/matricula', methods=['DELETE'])
@cross_origin()
def delete_matricula():
    return jsonify(model.delete_matricula(int(request.json['id_matricula'])))

@matricula_blueprint.route('/matricula', methods=['POST'])
@cross_origin()
def matricula():
    return jsonify(model.get_matricula(int(request.json['id_matricula'])))

@matricula_blueprint.route('/matriculas', methods=['POST'])
@cross_origin()
def matriculas():
    return jsonify(model.get_matriculas())