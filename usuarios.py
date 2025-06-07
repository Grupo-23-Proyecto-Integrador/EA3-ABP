import config_bd
from mysql.connector import Error

class Usuarios(config_bd.Clase_mysql):
    def __init__(self):
        self.__sesion_activa = False
    # roles o usuarios : Admin / Usuario estandar
        self.__rol = ""
        self.__id_usuario = 0
    def completar_perfil(self, nombre:str=None, apellido:str=None, email:str=None, usuario:str=None, password=None):
    # creacion de atributos o propiedades del objeto que se va a instanciar
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.__password = password

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_password(self, password):        
        self.__password = password
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
              rol: {self.ver_acceso}''')

    def ver_acceso(self):
        return self.__rol
    
    def ver_usuario(self):
        return self.usuario

    def ver_password(self):
        return self.__password

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
          
      
    def delete_sesion(self):
        self.__rol = ""
        self.__sesion_activa = False
        self.__id_usuario = 0


    