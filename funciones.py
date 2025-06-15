import usuarios , re

"""""
estas funciones no estan asociadas a ninguna clase, en principio responden al principio de modularidad y unica responsabilidad de cada una de ellas.
se evita de esta forma que el menu general se vea mas limpio o con menos codigo, respondiendo a buenas practicas.
"""

""" la funcion datos_alta() ejecuta validaciones de inputs, hace uso del mudulo re ( expresion regular de email) para esa validacion.
esta funcion retorna un objeto de la clase usuarios y se usa el metodo modificar (que funciona como metodo setter) """
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
    u = usuarios.Usuarios()
    u.modificar(nombre, apellido, nombre_usuario, email, password)
    return u 
# esta funcion cumple el rol casi identico a la anterior para validar campos de los atributos a modificar, retorna un objeto de la clase usuarios
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
    # esta parte setea el valor o rol para setearlo en el objeto (usuario) y retornalo 
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
"""
esta funcion requerir_datos_sesion() pertenece al modulo funciones.py
no requiere argumentos y retorna o devuelve una tupla (arreglo) con las variables usuario y password) que luego van a ser desestructurados fuera de esta funcion
efectua validaciones de minimo y maximo de caracteres permitidos.
"""
def requerir_datos_sesion():    
    usuario = input("ingrese su usuario: ")
    while len(usuario) < 5:
        usuario = input("ingrese su usuario con minimo 5 caracteres: ")
    # validar password
    password = input("ingrese su password: ") 
    while len(password) < 10:
        password = input("ingrese su password con minimo 10 caracteres: ")
    while len(password) > 50:
        password = input("ingrese su password con maximo 50 caracteres: ")                    
    login = (usuario , password)
    return login

""""esta funcion menu_inicial()
    muestra en pantalla 3 opciones: (inicio de sesion / registrarse como nuevo usuario / salir de la app)
    internamente tiene un bucle while que itera un arreglo y pregunta que mientras sea diferente a la opcion 1, 2, 3 siga ejecutando el bucle
    si el input suministrado es igual a alguna de las 3 opciones, devuelve ese valor , el return de la funcion es con ese valor.
"""
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
# la funcion ver_misdatos(lista) hace un print de pantalla de la lista segun los indices
def ver_misdatos(datos):
    print(f"""
            id: {datos[0]}
            usuario: {datos[1]}
            permisos: {datos[2]}
            nombre: {datos[3]}
            apellido: {datos[4]}
            email: {datos[5]}
            """)
    
# esta funcion recibe 3 argumentos, permiso que es string y 2 funciones ( admin , estandar)  y retorna 1 funcion dependiendo del valor del parametro permiso  
def selector_menu(permiso, menu_admin, menu_estandar):
    if permiso == "Admin":
                  return menu_admin
    elif permiso == "usuario_estandar":
                  return menu_estandar
    else:
        print("usuario sin permisos")     