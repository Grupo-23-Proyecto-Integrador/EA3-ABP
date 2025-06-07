from dotenv import load_dotenv
import os, config_bd, usuarios, re, sesiones
from mysql.connector import Error

# variables de entorno del .env (desarrollo) a traves de las librerias os y dotenv

# aca se definen menu de inicio que comprende inicio de sesion y registro de usuario
def menu_inicial():
    print(f"""
          Bienvenido al Menu gestor de usuarios del sistema

          * 1. Inicio de Sesion
          * 2. Registrarse en el sistema
          * Presione cualquier tecla para salir de la aplicacion

          """)
    opcion = input(f"""ingrese alguna opcion valida:
                   """)
    if opcion == "1":
        # opcion inicio de sesion de usuario existente
        sesion = requerir_datos_sesion()
        # tupla desestructurada
        usuario , password = sesion        
        # efectuar la consulta a la bd con usuario y contraseña, esto me devolvera un objeto de tipo "sesion" para establecer sesion y para seleccionar el menu segun el rol
        s = conexion_instanciada.consultar_username(usuario, password)
        # ahora verifico el menu que le corresponde de acuerdo a la consulta de la base de datos      
        if s.ver_rol() == "admin" or s.ver_rol() == "Admin":
            print(f"""
                  Usuario: {s.ver_usuario()}
                  Acceso: {s.ver_rol()}""")
            menu_admin()
        if s.ver_rol() == "usuario_estandar":
            print(f"""
                  Usuario: {s.ver_usuario()}
                  Acceso: {s.ver_rol()}""")
            menu_estandar()       
    elif opcion == "2":
        # opcion registrar usuario nuevo
        p = datos_alta()

        resultado = conexion_instanciada.insert_usuario(p.nombre, p.apellido, p.email, p.usuario, p.ver_password())
    else:
        return        
# menu de usuario segun el rol accede a un metodo u otro
def menu_admin():
    print(f"""
          Bienvenido al Menu para Administradores del sistema

          * 1. Ver todos los usuarios del sistema
          * 2. Editar un usuario
          * 3. Eliminar un usuario
          * 4. Salir

          """)
   
def menu_estandar():
    # rol estandar : solo puede ver sus datos personales 
    print(f"""
          Bienvenido al Menu para Usuarios
          
          * 1. ver mis datos
          * 2. Salir

          """)
    
def datos_alta():
    # validacion nombre
    nombre = input("ingrese su nombre: ") 
    while len(nombre) < 3:
        nombre = input("ingrese su nombre con minimos 3 caracteres: ")
    while len(nombre) > 50:
        nombre = input("ingrese su nombre con maximo 50 caracteres: ")
    # validacion apellido
    apellido = input("ingrese su apellido: ") 
    while len(apellido) < 3:
        apellido = input("ingrese su apellido con minimo 3 caracteres: ")
    while len(apellido) > 50:
        apellido = input("ingrese su apellido con maximo 50 caracteres: ")
    # validar email
    email = input("ingrese su email: ") 
    while len(email) < 5:
        email = input("ingrese su email con minimo 5 caracteres: ")    
    expresion = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'    
    while re.match(expresion, email) == None:
        email = input("ingrese email valido: ")
    while len(email) > 50:
        email = input("ingrese su email con maximo 50 caracteres: ")
    # validar usuario
    nombre_usuario = input("ingrese su nombre de usuario: ") 
    while len(nombre_usuario) < 5:
        nombre_usuario = input("ingrese su nombre de usuario con minimo 5 caracteres: ")
    while len(nombre_usuario) > 50:
        nombre_usuario = input("ingrese su nombre de usuario con maximo 50 caracteres: ") 
    # validar password
    password = input("ingrese su password: ") 
    while len(password) < 10:
        password = input("ingrese su password con minimo 10 caracteres: ")
    while len(password) > 50:
        password = input("ingrese su password con maximo 50 caracteres: ")                    
    # instanciar objeto, rellenarlo y devolverlo a main            
    u = usuarios.Usuarios()
    u.completar_perfil(nombre, apellido, nombre_usuario,email, password)
    return u 

def requerir_datos_sesion():
    # en este metodo ya estoy instanciando un objeto usuario con los datos necesarios
    # validar usuario
    usuario = input("ingrese su usuario: ")
    while len(usuario) < 5:
        usuario = input("ingrese su usuario con minimo 5 caracteres: ")
    # validar password
    password = input("ingrese su password: ") 
    while len(password) < 10:
        password = input("ingrese su password con minimo 10 caracteres: ")
    while len(password) > 50:
        password = input("ingrese su password con maximo 50 caracteres: ")                    
    # instanciar objeto, rellenarlo y devolverlo a main            
    login = (usuario , password)
    return login


if __name__ == "__main__":
    load_dotenv()
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    user = os.getenv("MYSQLUSER")
    password = os.getenv("MYSQLPASSWORD")
    root_password = os.getenv("MYSQL_ROOT_PASSWOR")
# instanciar la clase
conexion_instanciada = config_bd.Clase_mysql() 
# Pasos a Cumplir
# crear un script para poblar tabla

# completar los argumentos del metodo
conexion_instanciada.mysql_configurar(host,database,user,password)
# carga del menu principal
menu_inicial()

        
