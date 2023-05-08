from backend.models.mysql_connection_pool import MySQLPool

class participacionModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_participacion(self, id_participacion):    
        params = {'id_participacion' : id_participacion}      
        rv = self.mysql_pool.execute("SELECT * from Participacion P inner join Horario H on P.id_horario = H.id_horario where id_participacion=%(id_participacion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_participacion': result[0], 'fecha': result[1], 'nota_final': result[2], 'id_horario': result[3], 'dia': result[5]}
            data.append(content)
            content = {}
        return data

    def get_participacions(self):  
        rv = self.mysql_pool.execute("SELECT * from Participacion P inner join Horario H on P.id_horario = H.id_horario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_participacion': result[0], 'fecha': result[1], 'nota_final': result[2], 'id_horario': result[3], 'dia': result[5]}
            data.append(content)
            content = {}
        return data

    def create_participacion(self, fecha, nota_final, id_horario):    
        data = {
            'fecha' : fecha,
            'nota_final' : nota_final,
            'id_horario' : id_horario
        }  
        query = """insert into Participacion(fecha, nota_final, id_horario) 
        values (%(fecha)s, %(nota_final)s, %(id_horario)s)""" 
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_participacion'] = cursor.lastrowid
        return data

    def update_participacion(self, id_participacion, fecha, nota_final, id_horario):    
        data = {
            'id_participacion' : id_participacion,
            'fecha' : fecha,
            'nota_final' : nota_final,
            'id_horario' : id_horario
        }  
        query = """update Participacion set fecha = %(fecha)s, nota_final = %(nota_final)s, id_horario= %(id_horario)s
                    where id_participacion = %(id_participacion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_participacion(self, id_participacion):    
        params = {'id_participacion' : id_participacion}      
        query = """delete from Participacion where id_participacion = %(id_participacion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



if __name__ == "__main__":    
    tm = participacionModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    print(tm.create_participacion('vicente', 'machaca', 'vmachacaa@gmail.com'))