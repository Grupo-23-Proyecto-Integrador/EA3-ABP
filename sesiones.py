class Nueva():
    def __init__(self):
        self._logueado = False
        self._rol = ""
        self._usuario = ""
        self._id = 0

    def set_sesion(self, id:int, rol:str, usuario:str):
        if id == "" or id == "0" or rol == "" or usuario == "":
                 print("los datos de inicio de sesion son incorrectos")
                 return
        elif rol == "admin" or rol == "Admin":
                return "Admin"
        elif rol == "usuario_estandar":
                return "usuario_estandar"
        else:
                print("el usuario no existe, no tiene permisos suficientes o la contraseña es incorrecta intente nuevamente mas tarde")
                return "inexistente"   
             
        if id != 0 and rol != "" and usuario != "":
            self._rol = rol
            self._usuario = usuario
            self._id = id
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
    

    def ver_estado(self):
        return self._logueado

    # ver todo solo para develop no produccion
    def ver_todo(self):
        print(f"""
                  id: {self._id}
                  usuario: {self._usuario}
                  rol: {self._rol}
                  logueado: {self._logueado}  """)         