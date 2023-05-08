from backend.models.mysql_connection_pool import MySQLPool

class usuarioModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_usuario(self, usuario_dni):    
        params = {'usuario_dni' : usuario_dni}      
        rv = self.mysql_pool.execute("SELECT * from Usuario U inner join GrupoUsuario GU on U.id_grupo_usuario = GU.id_grupo_usuario where dni=%(usuario_dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'usuario_dni': result[0], 'usuario_nombre': result[1], 'usuario_apellido': result[2], 'usuario_telefono': result[3], 'usuario_correo': result[4], "usuario" : result[-1], "usuario_vector" : result[7], "usuario_ruta" : result[8]}
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from Usuario U inner join GrupoUsuario GU on U.id_grupo_usuario = GU.id_grupo_usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'usuario_dni': result[0], 'usuario_nombre': result[1], 'usuario_apellido': result[2], 'usuario_telefono': result[3], 'usuario_correo': result[4], "usuario" : result[-1], "usuario_vector" : result[7], "usuario_ruta" : result[8]}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, usuario_dni ,usuario_nombre, usuario_apellido, usuario_telefono, usuario_correo, usuario_contraseña, usuario_id_grupo_usuario, usuario_vector, usuario_ruta):    
        data = {
            'usuario_dni' : usuario_dni,
            'usuario_nombre' : usuario_nombre,
            'usuario_apellido' : usuario_apellido,
            'usuario_telefono': usuario_telefono,
            'usuario_correo': usuario_correo,
            'usuario_contraseña': usuario_contraseña,
            'usuario_id_grupo_usuario' : usuario_id_grupo_usuario,
            'usuario_vector' : usuario_vector,
            'usuario_ruta' : usuario_ruta
        }  
        query = """insert into Usuario(dni, nombre, apellido, telefono, correo, contrasena, id_grupo_usuario, vector, ruta) 
            values (%(usuario_dni)s, %(usuario_nombre)s, %(usuario_apellido)s, %(usuario_telefono)s, %(usuario_correo)s, %(usuario_contraseña)s, %(usuario_id_grupo_usuario)s, %(usuario_vector)s, %(usuario_ruta)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['usuario_dni'] = cursor.lastrowid
        return data

    def update_usuario(self, usuario_dni ,usuario_nombre, usuario_apellido, usuario_telefono, usuario_correo, usuario_contraseña, usuario_id_grupo_usuario, usuario_vector, usuario_ruta):    
        data = {
            'usuario_dni' : usuario_dni,
            'usuario_nombre' : usuario_nombre,
            'usuario_apellido' : usuario_apellido,
            'usuario_telefono': usuario_telefono,
            'usuario_correo': usuario_correo,
            'usuario_contraseña': usuario_contraseña,
            'usuario_id_grupo_usuario' : usuario_id_grupo_usuario,
            'usuario_vector' : usuario_vector,
            'usuario_ruta' : usuario_ruta
        }  
        query = """update Usuario set nombre = %(usuario_nombre)s, apellido = %(usuario_apellido)s, telefono= %(usuario_telefono)s, 
        correo = %(usuario_correo)s, contrasena = %(usuario_contraseña)s, id_grupo_usuario = %(usuario_id_grupo_usuario)s, vector = %(usuario_vector)s, ruta = %(usuario_ruta)s ruta where dni = %(usuario_dni)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_usuario(self, usuario_dni):    
        params = {'usuario_dni' : usuario_dni}      
        query = """delete from Usuario where dni = %(usuario_dni)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



if __name__ == "__main__":    
    tm = UsuarioModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    print(tm.create_usuario('vicente', 'machaca', 'vmachacaa@gmail.com'))