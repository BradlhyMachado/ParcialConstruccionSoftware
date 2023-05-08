from backend.models.mysql_connection_pool import MySQLPool

class matriculaModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_matricula(self, id_matricula):    
        params = {'id_matricula' : id_matricula}      
        rv = self.mysql_pool.execute("SELECT * from Matricula where id_matricula=%(id_matricula)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_matricula': result[0], 'id_estudiante': result[1], 'semestre': result[2], 'carrera': result[3], 'estado': result[4], 'id_seccion': result[5]}
            data.append(content)
            content = {}
        return data

    def get_matriculas(self):  
        rv = self.mysql_pool.execute("SELECT * from Matricula")  
        data = []
        content = {}
        for result in rv:
            content = {'id_matricula': result[0], 'id_estudiante': result[1], 'semestre': result[2], 'carrera': result[3], 'estado': result[4], 'id_seccion': result[5]}
            data.append(content)
            content = {}
        return data

    def create_matricula(self, id_estudiante, semestre, carrera, estado, id_seccion):    
        data = {
            'id_estudiante' : id_estudiante,
            'semestre' : semestre,
            'carrera' : carrera,
            'estado' : estado,
            'id_seccion' : id_seccion
        }  
        query = """insert into Matricula(id_estudiante, semestre, carrera, estado, id_seccion) 
        values (%(id_estudiante)s, %(semestre)s, %(carrera)s, %(estado)s, %(id_seccion)s)""" 
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_matricula'] = cursor.lastrowid
        return data

    def update_matricula(self, id_matricula, id_estudiante, semestre, carrera, estado, id_seccion):    
        data = {
            'id_matricula' : id_matricula,
            'id_estudiante' : id_estudiante,
            'semestre' : semestre,
            'carrera' : carrera,
            'estado' : estado,
            'id_seccion' : id_seccion
        }  
        query = """update Matricula set id_estudiante = %(id_estudiante)s, semestre = %(semestre)s, carrera = %(carrera)s, estado = %(estado)s, id_seccion= %(id_seccion)s
                    where id_matricula = %(id_matricula)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_matricula(self, id_matricula):    
        params = {'id_matricula' : id_matricula}      
        query = """delete from Matricula where id_matricula = %(id_matricula)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



if __name__ == "__main__":    
    tm = matriculaModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    print(tm.create_participacion('vicente', 'machaca', 'vmachacaa@gmail.com'))