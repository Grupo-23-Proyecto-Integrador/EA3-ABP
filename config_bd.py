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
            verificar = "SELECT 1 FROM usuarios_login WHERE usuario = %s LIMIT 1"
            cursor.execute(verificar, (usuario,))
            if cursor.fetchone():
                print(f'el usuario: {usuario} ya existe')
                return False
            # verifica la existencia del email
            verificar = "SELECT 1 FROM usuarios_login WHERE email = %s LIMIT 1"
            cursor.execute(verificar, (email,))
            if cursor.fetchone():
                print(f'el usuario: {email} ya existe')
                return False
            # si de ambas columnas no se encuentran registro procede al sql de insert en tablas separadas
            # insertar nombre y apellido en la tabla datos_sensibles
            consulta_datos_sensibles = "INSERT INTO datos_sensibles (nombre, apellido) VALUES (%s,%s)"
            cursor.execute(consulta_datos_sensibles,(nombre,apellido))
            self.conectar().commit()
            # insertar usuario email y password en tabla usuarios_login
            consulta = "INSERT INTO usuarios_login (usuario, email, password) VALUES (%s,%s,%s)"
            cursor.execute(consulta, (usuario, email, password))
            self.conectar().commit()
            print(f'registro exitoso del usuario: {usuario} con el email: {email}')
            return True
        except Exception as e:
            print(f'error al insertar el usuario, error: {e}')
        finally:
            if cursor:
                cursor.close()
