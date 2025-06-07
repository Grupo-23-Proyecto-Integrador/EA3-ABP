class Nueva_Sesion():
    def __init__(self):
        self.__logueado = False
        self.__rol = ""
        self.__usuario = ""
        self.__id = 0

    def configurar_sesion(self, id:int, rol:str, usuario:str):
        self.__rol = rol
        self.__usuario = usuario
        self.__id = id
        if self.__rol != "" and self.__id != 0  and self.__usuario != "":
            self.__logueado = True
            
    def activar_sesion(self):
        if self.__rol != "" and self.__id != 0  and self.__usuario != "":
            self.__logueado = True

    def cerrar_sesion(self):
        self.__logueado = False
        self.__rol = ""
        self.__usuario = ""
        self.__id = 0

    def ver_rol(self):
        return self.__rol
    
    def ver_usuario(self):
        return self.__usuario
    
    def ver_id(self):
        return self.__id
    
    def info_estado(self):
        if self.__logueado == True:
            print("la sesion esta activa")
        else:
            print("la sesion esta inactiva")

    def ver_estado(self):
        return self.__logueado         