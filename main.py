from dotenv import load_dotenv
import os, config_bd, usuarios, menus
from mysql.connector import Error

if __name__ == "__main__":
    # variables de entorno del .env (desarrollo) a traves de las librerias os y dotenv
    load_dotenv()
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    user = os.getenv("MYSQLUSER")
    password = os.getenv("MYSQLPASSWORD")
    root_password = os.getenv("MYSQL_ROOT_PASSWOR")
# Pasos a Cumplir
# crear un script para poblar tabla
# instanciar la clase
inicio = config_bd.Clase_mysql()
# completar los argumentos del metodo
inicio.mysql_configurar(host,database,user,password)
# instanciar usuario
usuario = usuarios.Usuarios()
p = menus.menu_inicial()
usuario.completar_perfil(p.nombre, p.apellido, p.email, p.usuario, p.password)
resultado = inicio.insert_usuario(usuario.nombre, usuario.apellido, usuario.email, usuario.usuario, usuario.password)
