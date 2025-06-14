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

    def ver_password(self):
        return self._password
   

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
