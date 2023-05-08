from backend.models.mysql_connection_pool import MySQLPool

class horarioModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        rv = self.mysql_pool.execute("""SELECT * from Horario H inner join Seccion S on H.id_seccion = S.id_seccion where H.id_horario = %(id_horario)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'dia_semana': result[1], 'hora_inicio': str(result[2]), 'hora_fin': str(result[3]), 'id_seccion': result[4], "seccion" : result[6]}
            data.append(content)
            content = {}
        return data

    def get_horarios(self):  
        rv = self.mysql_pool.execute("""SELECT * from Horario H inner join Seccion S on H.id_seccion = S.id_seccion""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'dia_semana': result[1], 'hora_inicio': str(result[2]), 'hora_fin': str(result[3]), 'id_seccion': result[4], "seccion" : result[6]}
            data.append(content)
            content = {}
        return data

    def create_horario(self, dia_semana, hora_inicio, hora_fin, id_seccion):    
        data = {
            'dia_semana' : dia_semana,
            'hora_inicio' : hora_inicio,
            'hora_fin': hora_fin,
            'id_seccion': id_seccion
        }  
        query = """insert into Horario(dia_semana, hora_inicio, hora_fin, id_seccion) 
            values (%(dia_semana)s, %(hora_inicio)s, %(hora_fin)s, %(id_seccion)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_horario'] = cursor.lastrowid
        return data

    def update_horario(self, id_horario, dia_semana, hora_inicio, hora_fin, id_seccion):    
        data = {
            'id_horario' : id_horario,
            'dia_semana' : dia_semana,
            'hora_inicio' : hora_inicio,
            'hora_fin': hora_fin,
            'id_seccion': id_seccion
        }   
        query = """update Horario set dia_semana = %(dia_semana)s, hora_inicio = %(hora_inicio)s, hora_fin= %(hora_fin)s, 
        id_seccion = %(id_seccion)s where id_horario = %(id_horario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        query = """delete from Horario where id_horario = %(id_horario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



if __name__ == "__main__":    
    tm = horarioModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(tm.create_horario('vicente', 'machaca', 'vmachacaa@gmail.com'))