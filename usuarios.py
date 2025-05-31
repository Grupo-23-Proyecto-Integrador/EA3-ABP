import config_bd
from mysql.connector import Error

class Usuarios:
    __sesion_activa = False
    # roles o usuarios : Admin / Usuario estandar

    def __init__(self, nombre:str, apellido:str, email:str, usuario:str, password:str, rol:str= None):
    # creacion de atributos o propiedades del objeto que se va a instanciar
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.__password = password
        self.rol = rol

    def info(self):
    # creacion de metodo de la clase para mostrar atributos (publicos o permitidos)    
        print(f'''
              nombre: {self.nombre}, 
              apellido: {self.apellido}, 
              email: {self.email},
              usuario: {self.usuario} 
              rol: {self.rol}''')


class User(config_bd.Configurar_mysql):
    # Clase usuario, heredando las configuraciones de conexión a MySQL de MySQLConfig.
    
    def __init__(self, host='localhost', database='your_database', user='your_user', password='your_password', username=None, email=None):
        # Llama al constructor de la clase padre
        super().__init__(host, database, user, password) 
        self.username = username
        self.email = email

    def get_usuario_por_email(self, usuario_email):
        # Recupera un usuario de la base de datos por su ID.
        # Retorna dict or None: Un diccionario con los datos del usuario si se encuentra, None en caso contrario.
        
        connection = self.get_connection()
        if connection:
            cursor = connection.cursor(dictionary=True) # dictionary=True para obtener resultados como diccionarios
            try:
                consulta = "SELECT id, usuario, email FROM usuarios WHERE email = %s"
                cursor.execute(consulta, (usuario_email,))
                user_data = cursor.fetchone()
                return user_data
            except Error as e:
                print(f"Error al obtener usuario por ID: {e}")
                return None
            finally:
                cursor.close()
                self.close_connection() # Es importante cerrar la conexión cuando ya no se necesita

    def crear_usuario(self, usuario, email):
        # Inserta un nuevo usuario en la base de datos.
        # Retorna: int or None: El ID del usuario recién insertado si la operación fue exitosa, None en caso contrario.
        
        connection = self.conectar()
        if connection:
            cursor = connection.cursor()
            try:
                consulta = "INSERT INTO usuarios (usuario, email) VALUES (%s, %s)"
                cursor.execute(consulta, (usuario, email))
                connection.commit() # Confirmar los cambios
                print(f"Usuario '{usuario}' creado exitosamente.")
                return cursor.lastrowid # Retorna el ID del último registro insertado
            except Error as e:
                connection.rollback() # Revertir los cambios en caso de error
                print(f"Error al crear usuario: {e}")
                return None
            finally:
                cursor.close()
                self.cerrar_conexion()