import usuarios , re

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
    u.modificar(nombre, apellido, nombre_usuario, email, password)
    return u 

def datos_editar():
    usuario = usuarios.Usuarios()
    id = "0"
    while int(id) < 1:
        id= input("ingrese el id del usuario a editar: ")
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
    password_usuario = input("ingrese su password: ") 
    while len(password_usuario) < 10:
        password_usuario = input("ingrese su password con minimo 10 caracteres: ")
    while len(password_usuario) > 50:
        password_usuario = input("ingrese su password con maximo 50 caracteres: ")
    # validacion rol
    rol_id = 0
    rol = input("ingrese el nuevo rol de usuario: ") 
    while len(rol) < 5 and len(rol) < 16:
        rol = input("ingrese un rol valido (Admin o usuario_estandar por ejemplo): ")
    if rol == "Admin":
        rol_id = 1
    elif rol == "usuario_estandar":
        rol_id = 2
    else: 
        return usuario     
    usuario.modificar(nombre, apellido, email, nombre_usuario, password_usuario, rol_id)      
    return usuario

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

def menu_inicial():
    print(f"""
          Bienvenido al Menu gestor de usuarios del sistema

          * 1. Inicio de Sesion
          * 2. Registrarse en el sistema
          * 3. Para salir de la aplicacion

          """)
    opcion = "0"
    while opcion not in ["1","2","3"]:        
        opcion = input(f"""ingrese alguna opcion valida :  """)
    return opcion   

def ver_misdatos(datos):
    print(f"""
            id: {datos[0]}
            usuario: {datos[1]}
            permisos: {datos[2]}
            nombre: {datos[3]}
            apellido: {datos[4]}
            email: {datos[5]}
            """)