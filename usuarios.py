import config_bd
from mysql.connector import Error

class Usuarios(config_bd.Clase_mysql):
    def __init__(self):
        self.__sesion_activa = False
    # roles o usuarios : Admin / Usuario estandar
        self.__rol = ""
        self.__id_usuario = 0
    def completar_perfil(self, nombre:str=None, apellido:str=None, email:str=None, usuario:str=None, password:str=None):
    # creacion de atributos o propiedades del objeto que se va a instanciar
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.password = password

    def conexion_inicial(self, host='localhost', database='database', user='user', password='password'):
        # Llama al constructor de la clase padre
        super().mysql_configurar(host, database, user, password)    
        # establecer aqui los datos de la conexion para la clase padre
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def info(self):
    # creacion de metodo de la clase para mostrar atributos (publicos o permitidos)    
        print(f'''
              nombre: {self.nombre}, 
              apellido: {self.apellido}, 
              email: {self.email},
              usuario: {self.usuario} 
              rol: {self.__rol}''')
       
    def __establecer_sesion(self):
        # hacer la consulta sql para ver si existe el usuario
        # retornar el id o algun campo mas
        # establecer la sesion como activa
        # establecer el rol de acuerdo a lo devuelvo de la consulta
        print("completar el metodo")   
      
    def __destruir_sesion(self):
        self.__rol = ""
        self.__sesion_activa = False
        self.__id_usuario = 0


    