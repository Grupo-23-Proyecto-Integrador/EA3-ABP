""" la clase Nueva es para instanciar un objeto vacio con valores de una sesion sin iniciar
el metodo set_sesion() configura el objeto con valores de un usuario logueado exitosamente, dentro del metodo set_sesion() tiene validaciones.
el objeto generado cumple la finalidad de variable global que conserva las configuraciones necesarias que usan otras funciones
el nombre estado_global nos parecio mas asertivo.
estado_global lo que busca es evitar hacer la misma consulta de existencia de un usuario determinado en la base de datos (rendimiento por ejemplo)
Los metodos siguientes son para ver las propiedades del objeto son privadas tienen guion bajo.
los unicos 3 metodos que permiten acceder y editar las porpiedades del objeto son set_sesion() y cerrar_sesion()
"""

class Nueva():
    def __init__(self):
        self._logueado = False
        self._rol = ""
        self._usuario = ""
        self._id = 0

    def set_sesion(self, id:int, rol:str, usuario:str):
        if id > 0 and rol == 1:
            # 1 es admin
            self._id = id
            self._rol = 1
            self._logueado = True
            self._usuario = usuario
            return "Admin"
        elif id > 0 and rol == 2:
            # 2 es usuario estandar
            self._id = id
            self._rol = 1
            self._logueado = True
            self._usuario = usuario
            return "usuario_estandar"
        else:
            print("ocurrio un error al setear la sesion")
            return ""    

    def cerrar_sesion(self):
        self._logueado = False
        self._rol = ""
        self._usuario = ""
        self._id = 0

    def ver_rol(self):
        return self._rol
    
    def ver_usuario(self):
        return self._usuario
    
    def ver_id(self):
        return self._id   
    
    def ver_estado(self):
        return self._logueado

    def ver_todo(self):
        print(f"""
                  id: {self._id}
                  usuario: {self._usuario}
                  rol: {self._rol}
                  logueado: {self._logueado}  """)         