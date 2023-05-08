from backend.models.mysql_connection_pool import MySQLPool

class justificacionModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_justificacion(self, id_justificacion):    
        params = {'id_justificacion' : id_justificacion}      
        rv = self.mysql_pool.execute("SELECT * from Justificacion J inner join Asistencia A on J.id_asistencia = A.id_asistencia where id_justificacion=%(id_justificacion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_justificacion': result[0], 'id_asistencia': result[1], 'razon': result[2], 'estado': result[3], 'id_asistencia': result[4]}
            data.append(content)
            content = {}
        return data

    def get_justificacions(self):  
        rv = self.mysql_pool.execute("SELECT * from Justificacion J inner join Asistencia A on J.id_asistencia = A.id_asistencia")  
        data = []
        content = {}
        for result in rv:
            content = {'id_justificacion': result[0], 'id_asistencia': result[1], 'razon': result[2], 'estado': result[3], 'id_asistencia': result[4]}
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, id_asistencia, razon, estado):    
        data = {
            'id_asistencia' : id_asistencia,
            'razon' : razon,
            'estado' : estado
        }  
        query = """insert into Justificacion(id_asistencia, razon, estado) 
        values (%(id_asistencia)s, %(razon)s, %(estado)s)""" 
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_justificacion'] = cursor.lastrowid
        return data

    def update_justificacion(self, id_justificacion, id_asistencia, razon, estado):    
        data = {
            'id_justificacion' : id_justificacion,
            'id_asistencia' : id_asistencia,
            'razon' : razon,
            'estado' : estado
        }  
        query = """update Justificacion set id_asistencia = %(id_asistencia)s, razon = %(razon)s, estado= %(estado)s
                    where id_justificacion = %(id_justificacion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_justificacion(self, id_justificacion):    
        params = {'id_justificacion' : id_justificacion}      
        query = """delete from Justificacion where id_justificacion = %(id_justificacion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



if __name__ == "__main__":    
    tm = justificacionModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    print(tm.create_justificacion('vicente', 'machaca', 'vmachacaa@gmail.com'))
    