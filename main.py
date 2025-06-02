from dotenv import load_dotenv
import os, config_bd, usuarios
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
# desplegar menu (funcion) 2 opciones en este menu principal: registro de usuario - inicio de sesion
# desplegar menu (depende del rol de la persona que inicio sesion)
# usuario admin (permisos) ver todos los usuarios / cambiar rol de usuario / eliminar usuario

# instanciar la clase
inicio = config_bd.Clase_mysql()
# completar los argumentos del metodo
inicio.mysql_configurar(host,database,user,password)
# instanciar usuario
usuario = usuarios.Usuarios()
usuario.completar_perfil("javier", "carranza", "javi@gmail.com", "javicarranza123", "12345678")
# este metodo insert usuario funciona (en la tabla no puede haber 2 emails o apodos iguales (restriccion))
inicio.insert_usuario(usuario.nombre, usuario.apellido, usuario.usuario, usuario.email,usuario.password)