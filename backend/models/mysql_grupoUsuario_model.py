from backend.models.mysql_connection_pool import MySQLPool

class grupoUsuarioModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_grupoUsuario(self, id_grupo_usuario):    
        params = {'id_grupo_usuario' : id_grupo_usuario}      
        rv = self.mysql_pool.execute("""SELECT * from GrupoUsuario where id_grupo_usuario = %(id_grupo_usuario)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_grupo_usuario': result[0], 'nombre_grupo': result[1]}
            data.append(content)
            content = {}
        return data

    def get_grupoUsuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from GrupoUsuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_grupo_usuario': result[0], 'nombre_grupo': result[1]}
            data.append(content)
            content = {}
        return data

    def create_grupoUsuario(self, nombre_grupo):    
        data = {
            'nombre_grupo' : nombre_grupo
        }  
        query = """insert into GrupoUsuario(nombre_grupo)
                values (%(nombre_grupo)s)"""    
        grupo_usuario = self.mysql_pool.execute(query, data, commit=True)   

        data['id_grupo_usuario'] = grupo_usuario.lastrowid
        return data
    
    def update_grupoUsuario(self, id_grupo_usuario ,nombre_grupo):    
        data = {
            'id_grupo_usuario' : id_grupo_usuario,
            'nombre_grupo' : nombre_grupo
        }  
        query = """update GrupoUsuario set nombre_grupo = %(nombre_grupo)s where id_grupo_usuario = %(id_grupo_usuario)s"""    
        grupo_usuario = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_grupoUsuario(self, id_grupo_usuario):    
        params = {'id_grupo_usuario' : id_grupo_usuario}      
        query = """delete from GrupoUsuario where id_grupo_usuario = %(id_grupo_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = grupoUsuarioModel()     

    #print(tm.get_grupoUsuario(1))
    #print(tm.get_grupoUsuarios())
    #print(tm.delete_grupoUsuario(67))
    #print(tm.get_grupoUsuarios())
    print(tm.create_grupoUsuario('prueba 10', 'desde python', 1)) 