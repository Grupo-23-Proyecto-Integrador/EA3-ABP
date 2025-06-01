from dotenv import load_dotenv
import os, config_bd
from mysql.connector import Error

if __name__ == "__main__":
    # variables de entorno del .env (desarrollo) a traves de las librerias os y dotenv
    load_dotenv()
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    user = os.getenv("MYSQLUSER")
    password = os.getenv("MYSQLPASSWORD")

# Pasos a Cumplir
# crear una function (def) para poblar tabla
# crear una funcion para crear tabla si no existe aun en la BD
# desplegar menu (funcion) 2 opciones en este menu principal: registro de usuario - inicio de sesion
# desplegar menu (depende del rol de la persona que inicio sesion)
# usuario admin (permisos) ver todos los usuarios / cambiar rol de usuario / eliminar usuario

# instanciar la clase
inicio = config_bd.Configurar_mysql()
# completar los argumentos del metodo
inicio.mysql_configurar(host,database,user,password)
# efectuar una conexion de prueba
inicio.conectar()