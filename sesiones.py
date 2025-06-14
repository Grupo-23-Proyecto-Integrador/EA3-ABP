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
            print("ocurrio un error al settear la sesion")
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