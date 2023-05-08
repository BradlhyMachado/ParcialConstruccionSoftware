from backend.models.mysql_connection_pool import MySQLPool
from backend.models.mysql_usuario_model import usuarioModel

class profesorModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_profesor(self, id_profesor):    
        params = {'id_profesor' : id_profesor}      
        rv = self.mysql_pool.execute("""SELECT * from Profesor e inner join Usuario u on e.dni = u.dni where id_profesor = %(id_profesor)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_profesor': result[0], 'asignatura_profesor': result[1], 'profesor_dni': result[2], 'nombre': result[4], 'apellidos': result[5]}
            data.append(content)
            content = {}
        return data

    def get_profesors(self):  
        rv = self.mysql_pool.execute("SELECT * from Profesor p inner join Usuario u on p.dni = u.dni")  
        data = []
        content = {}
        for result in rv:
            content = {'id_profesor': result[0], 'asignatura_profesor': result[1], 'profesor_dni': result[2], 'nombre': result[4], 'apellidos': result[5]}
            data.append(content)
            content = {}
        return data

    def create_profesor(self, asignatura_profesor, dni, usuario_nombre, usuario_apellido, usuario_telefono, usuario_correo, usuario_contraseña, usuario_vector, usuario_ruta):    
        data = {
            'asignatura_profesor' : asignatura_profesor,
            'dni' : dni
        }  

        #Crear usuario
        usuario_data = {
            'usuario_dni': dni,
            'usuario_nombre': usuario_nombre,
            'usuario_apellido': usuario_apellido,
            'usuario_telefono': usuario_telefono,
            'usuario_correo': usuario_correo,
            'usuario_contraseña': usuario_contraseña,
            'usuario_id_grupo_usuario': 1,
            'usuario_vector' : usuario_vector,
            'usuario_ruta' : usuario_ruta
        }
        model = usuarioModel()
        model.create_usuario(**usuario_data)
        #----------------------
        
        query = """insert into Profesor(asignatura_profesor, dni)
                values (%(asignatura_profesor)s, %(dni)s)"""    
        profesor = self.mysql_pool.execute(query, data, commit=True)

        data['id_profesor'] = profesor.lastrowid
        return data
    
    def update_profesor(self, id_profesor ,asignatura_profesor, dni, usuario_nombre, usuario_apellido, usuario_telefono, usuario_correo, usuario_contraseña, usuario_vector, usuario_ruta):    
        data = {
            'id_profesor' : id_profesor,
            'asignatura_profesor' : asignatura_profesor
        }

        usuario_data = {
            'usuario_dni' : dni,
            'usuario_nombre' : usuario_nombre,
            'usuario_apellido' : usuario_apellido,
            'usuario_telefono': usuario_telefono,
            'usuario_correo': usuario_correo,
            'usuario_contraseña': usuario_contraseña,
            'usuario_id_grupo_usuario' : 1,
            'usuario_vector' : usuario_vector,
            'usuario_ruta' : usuario_ruta
        }
        model = usuarioModel()
        model.update_usuario(**usuario_data)

        query = """update Profesor set asignatura_profesor = %(asignatura_profesor)s where id_profesor = %(id_profesor)s"""    
        profesor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_profesor(self, dni):    
        params = {'dni' : dni}      

        query = """delete from Profesor where dni = %(dni)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        model = usuarioModel()
        model.delete_usuario(dni)

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = profesorModel()     

    #print(tm.get_profesor(1))
    #print(tm.get_profesors())
    #print(tm.delete_profesor(67))
    #print(tm.get_profesors())
    print(tm.create_profesor('prueba 10', 'desde python', 1)) 