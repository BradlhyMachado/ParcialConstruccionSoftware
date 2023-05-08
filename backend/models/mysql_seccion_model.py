from backend.models.mysql_connection_pool import MySQLPool

class seccionModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_seccion(self, id_seccion):    
        params = {'id_seccion' : id_seccion}      
        rv = self.mysql_pool.execute("""SELECT * from Seccion s inner join Curso c on c.id_curso = s.id_curso where id_seccion = %(id_seccion)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion': result[0], 'nombre_seccion': result[1], 'curso': result[4]}
            data.append(content)
            content = {}
        return data

    def get_seccions(self):  
        rv = self.mysql_pool.execute("SELECT * from Seccion s inner join Curso c on c.id_curso = s.id_curso")  
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion': result[0], 'nombre_seccion': result[1], 'curso': result[4]}
            data.append(content)
            content = {}
        return data

    def create_seccion(self, nombre_seccion, id_curso):    
        data = {
            'nombre_seccion' : nombre_seccion,
            'id_curso' : id_curso
        }  
        query = """insert into Seccion(nombre_seccion, id_curso)
                values (%(nombre_seccion)s, %(id_curso)s)"""    
        seccionr = self.mysql_pool.execute(query, data, commit=True)   

        data['id_seccion'] = seccionr.lastrowid
        return data
    
    def update_seccion(self, id_seccion, nombre_seccion, id_curso):    
        data = {
            'id_seccion': id_seccion,
            'nombre_seccion' : nombre_seccion,
            'id_curso' : id_curso
        }  
        query = """update Seccion set nombre_seccion = %(nombre_seccion)s, id_curso = %(id_curso)s where id_seccion = %(id_seccion)s"""    
        seccionr = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_seccion(self, id_seccion):    
        params = {'id_seccion' : id_seccion}      
        query = """delete from Seccion where id_seccion = %(id_seccion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = seccionModel()     

    #print(tm.get_seccion(1))
    #print(tm.get_seccions())
    #print(tm.delete_seccion(67))
    #print(tm.get_seccions())
    print(tm.create_seccion('prueba 10', 'desde python', 1)) 