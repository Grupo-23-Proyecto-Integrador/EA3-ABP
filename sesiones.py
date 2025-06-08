class Nueva_Sesion():
    def __init__(self):
        self._logueado = False
        self._rol = ""
        self._usuario = ""
        self._id = 0

    def configurar_sesion(self, id:int, rol:str, usuario:str):        
        if id != 0 and rol != "" and usuario != "":
            self._rol = rol
            self._usuario = usuario
            self._id = id
            self._logueado = True
            
    def activar_sesion(self):
        if self._rol != "" and self._id != 0  and self._usuario != "":
            self._logueado = True

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
    
    def info_estado(self):
        if self._logueado == True:
            print("la sesion esta activa")
        else:
            print("la sesion esta inactiva")

    def ver_estado(self):
        return self._logueado

    # ver todo solo para develop no produccion
    def ver_todo(self):
        print(f"""
                  id: {self._id}
                  usuario: {self._usuario}
                  rol: {self._rol}
                  logueado: {self._logueado}  """)         