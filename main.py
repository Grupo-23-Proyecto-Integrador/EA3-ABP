from dotenv import load_dotenv
import os, re
import sesiones , config_bd , usuarios
from mysql.connector import Error

# variables de entorno del .env (desarrollo) a traves de las librerias os y dotenv

# aca se definen menu de inicio que comprende inicio de sesion y registro de usuario
# instanciar objeto con sus metodos para la gestion del estado de sesion global
estado_global = sesiones.Nueva_Sesion()

def menu_inicial():    
    opcion = "0"
    while opcion != "3":
        print(f"""
          Bienvenido al Menu gestor de usuarios del sistema

          * 1. Inicio de Sesion
          * 2. Registrarse en el sistema
          * 3. Para salir de la aplicacion

          """)
        opcion = input(f"""ingrese alguna opcion valida :  """)    
        if opcion == "1":
        # opcion inicio de sesion de usuario existente
            sesion = requerir_datos_sesion()
        # tupla desestructurada
            u , password = sesion        
        # efectuar la consulta con usuario y contraseña, esto me devolvera un objeto con id, rol y usuario (para rellenear mi objeto sesion)
            # desestructuracion en el orden opuesto a la creacion en model
            id, rol, usuario = conexion_instanciada.consultar_username(u, password)                       
                        
        # ahora verifico el menu que le corresponde de acuerdo a la consulta de la base de datos      
            if id == "" or id == "0" or rol == "" or usuario == "":
                 print("los datos de inicio de seion son incorrectos")
                 return
            elif rol == "admin" or rol == "Admin":
                estado_global.configurar_sesion(id, rol, usuario)                        
                menu_admin()
            elif rol == "usuario_estandar":
                estado_global.configurar_sesion(id, rol, usuario)                       
                menu_estandar()
            else:
                print("el usuario no existe, no tiene permisos suficientes o la contraseña es incorrecta intente nuevamente mas tarde")
                      
        elif opcion == "2":
        # opcion registrar usuario nuevo
            p = datos_alta()
            resultado = conexion_instanciada.insert_usuario(p.nombre, p.apellido, p.email, p.usuario, p.ver_password())
        elif opcion == "3":
            return
            
# menu de usuario segun el rol accede a un metodo u otro
def menu_admin():
    print(f"""
                  Usuario: {estado_global.ver_usuario()}
                  Acceso: {estado_global.ver_rol()}
                  Codigo: {estado_global.ver_id()} """) 
    
        
    print(f"""
          Bienvenido al Menu para Administradores del sistema

          * 1. Ver todos los usuarios del sistema
          * 2. Editar un usuario
          * 3. Eliminar un usuario
          * 4. Salir 

          """)
    
    opcion = input(f"""ingrese alguna opcion valida:
                   """)

    if opcion == "1":        
        # no se piden datos ya que trae una consulta de todos los usuarios        
            todos = conexion_instanciada.ver_usuarios()
        # simple print pra ver la tupla de resultados
            print(todos)
        # finalizada la operacion ejecutar un menu de destrucion de la sesion
            estado_global.cerrar_sesion()            
    elif opcion == "2":        
            print("usted debe seleccionar los datos a modificar")
        # nuevamente verificar los permisos de admin almacenados en local
        # opcion editar usuario ( le tengo que solicitar algun campo, id, usuario o mail a mi eleccion)
        # finalizada la operacion ejecutar un menu de destrucion de la sesion
            estado_global.cerrar_sesion()
    elif opcion == "3":
            # nuevamente verificar los permisos de admin almacenados en local
            if estado_global.ver_estado:
                # no se piden datos ya que trae una consulta de todos los usuarios        
                todos = conexion_instanciada.ver_usuarios()
                # simple print pra ver la tupla de resultados
                print(todos)
                # este metodo devuelve true o false dependiendo si la cesion esta activa
                usuario = "0"
                while usuario == "0":
                    usuario = input(f"""
                    ingrese el ID del usuario que desee eliminar de forma permanente:  
                               """)                
                    # opcion eliminar usuario ( le tengo que solicitar campo, id)
                    print(f"el id: {usuario} proporcionado, este usuario sera eliminado de forma permanente con todos los datos personales asociados")
                    confirmacion = ""
                    while confirmacion != "si":
                        confirmacion = input("""escriba 'si' para confirmar
                                             """)               
                        operacion = conexion_instanciada.eliminar_usuario_id(usuario)
                        # finalizada la operacion ejecutar un menu de destrucion de la sesion
                        print(f"usuario por id:{usuario} el resultado de la eliminacion es: {operacion}")
            estado_global.cerrar_sesion()            
    elif opcion == "4":
        # finalizada la operacion ejecutar un menu de destrucion de la sesion
            estado_global.cerrar_sesion()        
            return
    
def menu_estandar():
    print(f"""
                  Usuario: {estado_global.ver_usuario()}
                  Acceso: {estado_global.ver_rol()}
                  Codigo: {estado_global.ver_id()} """)    
    # rol estandar : solo puede ver sus datos personales
     
    print(f"""
          Bienvenido al Menu para Usuarios
          
          * 1. ver mis datos
          * 2. Salir

          """)
    opcion = input("""
                   seleccione alguna de las 2 opciones: """)
    if opcion == "1":               
        # efectuar consulta a la base de datos con el id guardado en estado general
            id = estado_global.ver_id()
            d = conexion_instanciada.mis_datos(id)
            print(d)
            estado_global.cerrar_sesion()
    elif opcion == "2":
         estado_global.cerrar_sesion()
         return        
        
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

        
