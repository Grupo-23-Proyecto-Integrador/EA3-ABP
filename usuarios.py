import config_bd
from mysql.connector import Error

class Usuarios():
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.usuario = ""
        self._password = ""

    def modificar(self, nombre:str=None, apellido:str=None, email:str=None, usuario:str=None, password=None):
        # creacion de atributos o propiedades del objeto que se va a instanciar
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self._password = password

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_password(self, password):        
        self._password = password    

    def info(self):
    # creacion de metodo de la clase para mostrar atributos (publicos o permitidos)    
        print(f'''
              nombre: {self.nombre}, 
              apellido: {self.apellido}, 
              email: {self.email},
              usuario: {self.usuario} 
              rol: {self.ver_acceso}''')

    def ver_acceso(self):
        return self._rol
    
    def ver_usuario(self):
        return self.usuario

    def ver_password(self):
        return self._password

    def set_sesion(self):
        # este metodo efectua la consulta la base de datos, devuvel 3 valores y establece la sesion o no
        # voy a trabajar con USUARIO Y CONTRASEÑA
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # verifica la existencia del usuario ( descartar email, porque un usuario puede repetir email por ahora)
            cursor = conexion.cursor()
            verificar = "SELECT id_usuario, rol, usuario FROM usuarios_login WHERE usuario = %s AND password_usuario = %s"
            cursor.execute(verificar, (self.usuario ,self.password))
            resultado = cursor.fetchone()
            # retorna una tupla, ver si puede crearse una clase para simplificar
            if resultado == True:
                print(resultado)
                return True    
            else:
            # retorno una tupla vacia    
                return False
        except Exception as e:
            print(f'error al consultar el email y password, error: {e}')
            # retorno una tupla vacia    
            return False 
        finally:
            if cursor:
                cursor.close()
                conexion.close()
   

class Editar():
    def __init__(self):
        self._id = 0
        self._email = ""
        self._nombre_usuario = ""
        self._password_usuario = ""
        self._rol = ""

    def editar_relleno(self, id_usuario, email, nombre_usuario, password_usuario, rol):
        if int(id_usuario) < 1:
            print("el id debe ser superior a 0")
            return
        self._id = id_usuario
        if len(email) < 5 :
            print("el email debe ser superior a 4 caracteres")
            return    
        self._email = email
        if nombre_usuario == "":
            print("el email debe ser superior a 4 caracteres")
            return
        self._nombre_usuario = nombre_usuario
        if len(password_usuario) < 10:
            print("el password no puede contener menos de 10 caracteres")
            return
        self._password_usuario = password_usuario
        if rol == "":
            print("el rol no puede estar vacio")
            return
        elif len(rol) < 5:
            print("el rol no corresponde a una opcion valida para el sistema")
            return
        self._rol = rol        
        
        
    def ver_id(self):
        return self._id
    def ver_nombre_usuario(self):
        return self._nombre_usuario
    def ver_email(self):
        return self._email
    def ver_id(self):
        return self._id  
    def ver_password(self):
        return self._password_usuario
    def ver_rol(self):
        return self._rol            
