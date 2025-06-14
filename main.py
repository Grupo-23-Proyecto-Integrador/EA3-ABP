
import funciones , sesiones
from mysql.connector import Error
from config_bd import conexion_instanciada

estado_global = sesiones.Nueva()

"""""
el objeto estado_global es instanciado de la clase sesiones, que es un archivo global usado en este modulo para guardar los datos de las sesiones iniciadas por los usuarios
estableciendo las propiedades de id , rol, usuario, las cuales sirven para mostrar los datos cuando se inicie sesion y para mantener la sesion abierta
el metodo set_sesion() configura la sesion y el metododo cerrar_sesion() borra o blanquea los valores del objeto.
"""

def menu_general():       
    opcion = funciones.menu_inicial()
    # opcion 1 inicio de sesion    
    if opcion == "1":
            sesion = funciones.requerir_datos_sesion()
            # devuelve usuario y contraseña
            usuario , password = sesion        
            # verifico que el usuario exista previamente en el sistema
            id, rol, usuario_verificado = conexion_instanciada.consultar_username(usuario, password)                      
            # ahora verifico el menu que le corresponde de acuerdo a la consulta de la base de datos      
            permiso = estado_global.set_sesion(id, rol, usuario_verificado)
            if permiso == "Admin":
                  menu_admin()
            elif permiso == "usuario_estandar":
                  menu_estandar()
            else:
                  print("usuario sin permisos")                      
    elif opcion == "2":
            # opcion registrar usuario nuevo
            p = funciones.datos_alta()
            resultado = conexion_instanciada.insert_usuario(p.nombre, p.apellido, p.email, p.usuario, p.ver_password())
    elif opcion == "3":
            return
            
def menu_admin():
    estado_global.ver_todo()  
    print(f"""  Bienvenido al Menu para Administradores del sistema

          * 1. Ver todos los usuarios del sistema
          * 2. Editar un usuario
          * 3. Eliminar un usuario
          * 4. Salir 

          """)    
    opcion = input("ingrese alguna opcion valida:  """)
    if opcion == "1":        
            # no se piden datos ya que trae una consulta de todos los usuarios        
            todos = conexion_instanciada.ver_usuarios()
            # simple print pra ver la tupla de resultados
            print(todos)            
    elif opcion == "2":        
            if estado_global.ver_estado:
                p = funciones.datos_editar()
                res = conexion_instanciada.editar_usuario(p.nombre, p.apellido, p.email, p.usuario, p.password, p.rol, p.id )
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
    estado_global.ver_todo()
     
    print(f"""
          Bienvenido al Menu para Usuarios
          
          * 1. ver mis datos
          * 2. Salir

          """)
    opcion = input("""
                   seleccione alguna de las 2 opciones: """)
    if opcion == "1":               
        # efectuar consulta a la base de datos con el id guardado en estado general
            mis_datos = conexion_instanciada.mis_datos(estado_global.ver_id())
            funciones.ver_misdatos(mis_datos)
            estado_global.cerrar_sesion()
    elif opcion == "2":
         estado_global.cerrar_sesion()
         return        
        

if __name__ == "__main__":    
    menu_general()

        
