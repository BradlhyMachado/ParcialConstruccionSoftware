from backend.models.mysql_connection_pool import MySQLPool
import requests
from flask import request
from flask import json
import ast
import re

import numpy as np

from backend.models.mysql_usuario_model import usuarioModel
from backend.models.mysql_asistencia_model import asistenciaModel

class tomarAsistenciaModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def crear_asistencia(self, fecha, hora_entrada, hora_salida, dni, id_horario, foto):    
        response = requests.post("http://localhost:81/openfaceAPI", files = dict(file = foto))
        aux = response.text                         
        
        vectorInp = json.loads(aux)['result']

        modelo = usuarioModel()
        alumno = modelo.get_usuario(dni)
        
        vectorInt = alumno[0]["usuario_vector"]

        #vecstr1 = vectorInp.replace(" ", ",")
        #vecstr2 = vectorInt.replace(" ", ",")
        vecstr1 = re.sub("\s+", ',', vectorInp)
        vecstr2 = re.sub("\s+", ',', vectorInt)

        vector1 = np.array(ast.literal_eval(vecstr1))
        vector2 = np.array(ast.literal_eval(vecstr2))

        dist = np.linalg.norm(vector1-vector2)
        data = {}

        if (dist < 0.6):
            data = {
                'fecha' : fecha,
                'hora_entrada' : hora_entrada,
                'hora_salida': hora_salida,
                'dni': dni,
                'id_horario': id_horario
            }

            query = """insert into Asistencia(fecha, hora_entrada, hora_salida, dni, id_horario) 
            values (%(fecha)s, %(hora_entrada)s, %(hora_salida)s, %(dni)s, %(id_horario)s)"""
            cursor = self.mysql_pool.execute(query, data, commit=True)

            if cursor is not None:
                data['id_asistencia'] = cursor.lastrowid
            else:
                raise Exception("Error: Cursor is None in create_asistencia")
        
        data['dist'] = dist
        return data

if __name__ == "__main__":    
    tm = tomarAsistenciaModel()