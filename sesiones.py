class Nueva_Sesion():
    def __init__(self):
        self.__rol = ""
        self.__usuario = ""
        self.__id = 0

    def configurar_sesion(self, id:int, rol:str, usuario:str):
        self.__rol = rol
        self.__usuario = usuario
        self.__id = id

    def ver_rol(self):
        return self.__rol
    
    def ver_usuario(self):
        return self.__usuario
    
    def ver_id(self):
        return self.__id