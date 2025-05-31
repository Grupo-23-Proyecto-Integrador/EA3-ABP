from dotenv import load_dotenv
import os, config_bd
from mysql.connector import Error

if __name__ == "__main__":
    # variables de entorno del .env (desarrollo) a traves de las librerias os y dotenv
    load_dotenv()
    host = os.get("HOST")
    database = os.get("DATABASE")
    user = os.get("MYSQLUSER")
    password = os.get("MYSQLPASSWORD")

    
    instancia_conexion = config_bd.Configurar_mysql(host, database, user, password)
    conexion = instancia_conexion.conectar()
    if conexion:
        # if conexion es true
        try:
            cursor = conexion.cursor()
            # efectuar consulta
            cursor.close()
        except Error as e:
            print(f"Error en la consulta de la BD: {e}")
        finally:
            instancia_conexion.cerrar_conexion() # cerrar la conexión siempre (importante)
