import config_bd
from mysql.connector import Error

class Usuarios(config_bd.Configurar_mysql):
    __sesion_activa = False
    # roles o usuarios : Admin / Usuario estandar
    __rol = "usuario_estandar"

    def __init__(self, nombre:str, apellido:str, email:str, usuario:str, password:str):
    # creacion de atributos o propiedades del objeto que se va a instanciar
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
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
              rol: {self.__rol}''')

    def crear_usuario(self):
        # Inserta un nuevo usuario en la base de datos.
        # Retorna: int or None: El ID del usuario recién insertado si la operación fue exitosa, None en caso contrario.
        
        connection = self.conectar()
        if connection:
            cursor = connection.cursor()
            try:
                consulta = "INSERT INTO usuarios (usuario, nombre, apellido, email, password) VALUES (%s, %s %s, %s %s)"
                cursor.execute(consulta, (self.usuario, self.nombre, self.apellido, self.email , self.__password))
                connection.commit() # Confirmar los cambios
                print(f"Usuario '{self.usuario}' creado exitosamente.")
                return cursor.lastrowid # Retorna el ID del último registro insertado
            except Error as e:
                connection.rollback() # Revertir los cambios en caso de error
                print(f"Error al crear usuario: {e}")
                return None
            finally:
                cursor.close()
                self.cerrar_conexion()

    def get_usuario_por_email(self, usuario_email):
        # Recupera un usuario de la base de datos por su ID.
        # Retorna dict or None: Un diccionario con los datos del usuario si se encuentra, None en caso contrario.
        
        estado_conexion = self.conectar()
        if estado_conexion:
            cursor = estado_conexion.cursor(dictionary=True) # dictionary=True para obtener resultados como diccionarios
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
                self.cerrar_conexion() # Es importante cerrar la conexión cuando ya no se necesita

    def sesion(self):
        if self.__sesion_activa:
            print(f'el usuario: {self.usuario} ha iniciado sesion')
        else:
            print(f'el usuario: {self.usuario} no ha iniciado sesion')    

    def crear_tabla_usuarios(self, tabla:str="tabla"):
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            try:                
                cursor.execute("SHOW TABLES LIKE %s", tabla)
                resultado = cursor.fetchone()
                # si la devuelve un bool (true)
                if resultado:
                    print(f"la tabla {tabla} ya existe")
                else:
                    consulta_sql = f"""
                    CREATE TABLE {tabla} (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR (255) NOT NULL,
                        apellido VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        usuario VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                        rol VARCHAR(100) DEFAULT 'usuario_estandar'
                    );
                    """
                    cursor.execute(consulta_sql)
                    conexion.commit()
                    print(f"la tabla {tabla} creada de manera exitosa")
            except Error as err:
                print(f"Error al crear tabla: {tabla}, error: {err}")
                return None
            finally:
                cursor.close()
                self.cerrar_conexion()
    
    

    

    