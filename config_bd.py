import mysql.connector
from mysql.connector import Error


class Clase_mysql:
    # metodo inicial para configurar los datos de la conexion
    def mysql_configurar(self, mysql_host, mysql_database:str, mysql_user:str, mysql_password:str):
        # define conexion mysql
        self.host = mysql_host
        self.database = mysql_database
        self.user = mysql_user
        self.password = mysql_password
        self.estado_conexion = None
    # metodo: Establece y devuelve una conexión a la base de datos MySQL. o devuelvo None
    def conectar(self):                        
        if self.estado_conexion is None or not self.estado_conexion.is_connected():
            try:
                # muy importante aca estoy instanciando un objeto de la libreria mysql(connector.connect)
                # se le pasan los argumentos del metodo __init__
                self.estado_conexion = mysql.connector.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
                if self.estado_conexion.is_connected():
                    # is_connected (es un metodo heredado)
                    print(f"Conexión exitosa a la BD: '{self.database}' en '{self.host}'")
                return self.estado_conexion
                # si la conexión fue exitosa
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
                return None
                #retorna None en caso de no ser exitosa la conexion.
        else:
            return self.estado_conexion
    # Cierra la conexión activa a la base de datos, si existe.
    def cerrar_conexion(self):       
        
        if self.estado_conexion and self.estado_conexion.is_connected():
            self.estado_conexion.close()
            # Conexión mysql cerrada, hago un print si lo veo necesario
    
    # Creo una consulta Insert (nuevo usuario)
    def insert_usuario(self , nombre, apellido, usuario, email, password):
        # retorna true si fue exitosa la consulta sino retorna false porque algo salio mal
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # verifica la existencia del usuario
            cursor = conexion.cursor()
            verificar = "SELECT 1 FROM usuarios WHERE usuario = %s LIMIT 1"
            cursor.execute(verificar, (usuario,))
            if cursor.fetchone():
                print(f'el usuario: {usuario} ya existe')
                return False
            # verifica la existencia del email
            verificar = "SELECT 1 FROM usuarios WHERE email = %s LIMIT 1"
            cursor.execute(verificar, (email,))
            if cursor.fetchone():
                print(f'el usuario: {email} ya existe')
                return False
            # si de ambas columnas no se encuentran registro procede al sql de insert
            consulta = "INSERT INTO usuarios (nombre, apellido, usuario, email, password) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(consulta, (nombre, apellido, usuario, email, password))
            self.conectar().commit()
            print(f'registro exitoso del usuario: {usuario}')
            return True
        except Exception as e:
            print(f'error al insertar el usuario, error: {e}')
        finally:
            if cursor:
                cursor.close()

    def crear_tabla_usuarios(self):
        conexion = self.conectar()
        if conexion:
            cursor = conexion.cursor()
            try:                
                cursor.execute("SHOW TABLES LIKE usuarios")
                resultado = cursor.fetchone()
                # si la devuelve un bool (true)
                if resultado:
                    print(f"la tabla usuarios ya existe")
                else:
                    consulta = f"""
                    CREATE TABLE usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(255) NOT NULL,
                        apellido VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        usuario VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        rol VARCHAR(20) DEFAULT 'usuario_estandar'); """            
                    cursor.execute(consulta)
                    conexion.commit()
                    print(f"la tabla usuarios creada de manera exitosa")
            except Error as err:
                print(f"""
                      Error al crear tabla usuarios, 
                      error: {err}""")
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

    def crear_usuario_sql(self):
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