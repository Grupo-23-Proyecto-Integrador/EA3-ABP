import usuarios, re
# aca se definen menu de inicio que comprende inicio de sesion y registro de usuario
def menu_inicial():
    print(f"""
          Bienvenido al Menu gestor de usuarios del sistema

          * 1. Inicio de Sesion
          * 2. Registrarse en el sistema
          * 3. Salir de la aplicacion

          """)
    opcion = input(f"""ingrese alguna opcion valida:
                   """)
    if opcion == "1":
        sesion = requerir_datos_sesion()
        return sesion
    elif opcion == "2":
        p = datos_alta()
        return p
    else:
        return        
# menu de usuario segun el ron accede a un metodo u otro
# rol admin accede a : ver todos los usuarios / eliminar usuario, editar usuario
def menu_admin():
    print(f"""
          Bienvenido al Menu para Administradores del sistema

          * 1. Ver todos los usuarios del sistema
          * 2. Editar un usuario
          * 3. Eliminar un usuario
          * 4. Salir

          """)
# rol estandar : solo puede ver sus datos personales    
def menu_admin():
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
    while len(nombre_usuario) < 3:
        nombre_usuario = input("ingrese su nombre de usuario con minimo 3 caracteres: ")
    while len(nombre_usuario) > 50:
        nombre_usuario = input("ingrese su nombre de usuario con maximo 50 caracteres: ") 
    # validar password
    password = input("ingrese su password: ") 
    while len(password) < 10:
        password = input("ingrese su password con minimo 10 caracteres: ")
    while len(password) > 50:
        password = input("ingrese su password con maximo 50 caracteres: ")                    
    # instanciar objeto, rellenarlo y devolverlo a main            
    ingreso = usuarios.Usuarios()
    ingreso.completar_perfil(nombre, apellido, email, nombre_usuario, password)
    return ingreso 

def requerir_datos_sesion():    
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
    while len(nombre_usuario) < 3:
        nombre_usuario = input("ingrese su nombre de usuario con minimo 3 caracteres: ")
    while len(nombre_usuario) > 50:
        nombre_usuario = input("ingrese su nombre de usuario con maximo 50 caracteres: ") 
    # validar password
    password = input("ingrese su password: ") 
    while len(password) < 10:
        password = input("ingrese su password con minimo 10 caracteres: ")
    while len(password) > 50:
        password = input("ingrese su password con maximo 50 caracteres: ")                    
    # instanciar objeto, rellenarlo y devolverlo a main            
    sesion = usuarios.Usuarios()
    sesion.completar_perfil(email, nombre_usuario, password)
    return sesion       