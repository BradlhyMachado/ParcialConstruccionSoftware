from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_usuario_model import usuarioModel
model = usuarioModel()


usuario_blueprint = Blueprint('usuario_blueprint', __name__)


@usuario_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def create_usuario():
    content = model.create_usuario(request.json['usuario_dni'], request.json['usuario_nombre'], request.json['usuario_apellido'], request.json['usuario_telefono'], request.json['usuario_correo'], request.json['usuario_contraseña'], request.json['usuario_id_grupo_usuario'], request.json['usuario_vector'], request.json['usuario_ruta'])    
    return jsonify(content)

@usuario_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    content = model.update_usuario(request.json['usuario_dni'], request.json['usuario_nombre'], request.json['usuario_apellido'], request.json['usuario_telefono'], request.json['usuario_correo'], request.json['usuario_contraseña'], request.json['usuario_id_grupo_usuario'], request.json['usuario_vector'], request.json['usuario_ruta'])    
    return jsonify(content)

@usuario_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['usuario_dni'])))

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def usuario():
    return jsonify(model.get_usuario(int(request.json['usuario_dni'])))

@usuario_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def usuarios():
    return jsonify(model.get_usuarios())