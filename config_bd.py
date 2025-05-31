import mysql.connector
from mysql.connector import Error


class Configurar_mysql:
    # metodo inicial para configurar los datos de la conexion
    def __init__(self, host='localhost', database:str="db", user:str="usuario", password:str="password"):
        
        self.host = host
        self.database = database
        self.user = user
        self.password = password
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


