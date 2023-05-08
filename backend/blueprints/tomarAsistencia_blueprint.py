from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.tomarAsistencia_model import tomarAsistenciaModel

tomarAsistencia_blueprint = Blueprint('tomarAsistencia_blueprint', __name__)
@tomarAsistencia_blueprint.route('/tomarAsistencia', methods=['POST'])
def crear_asistencia():
    fecha = request.form['fecha']
    hora_entrada = request.form['hora_entrada']
    hora_salida = request.form['hora_salida']
    dni = request.form['dni']
    id_horario = request.form['id_horario']
    foto = request.files['foto']
    
    tm = tomarAsistenciaModel()
    data = tm.crear_asistencia(fecha, hora_entrada, hora_salida, dni, id_horario, foto)
    
    return jsonify(data), 201