import config_bd
from mysql.connector import Error

class Usuarios(config_bd.Clase_mysql):
    __sesion_activa = False
    # roles o usuarios : Admin / Usuario estandar
    __rol = "usuario_estandar"

    def __init__(self, nombre:str, apellido:str, email:str, usuario:str, password:str):
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

       
    def sesion(self):
        if self.__sesion_activa:
            print(f'el usuario: {self.usuario} ha iniciado sesion')
        else:
            print(f'el usuario: {self.usuario} no ha iniciado sesion')    
  
    
    def es_admin(self):
        return self.__rol == 'admin'


    