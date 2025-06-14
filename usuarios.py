
class Usuarios():
    def __init__(self):
        # metodo constructor, objeto vacio
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.usuario = ""
        self.password = ""
        self.rol = 0
        self.id = 0

    def modificar(self, nombre:str=None, apellido:str=None, email:str=None, usuario:str=None, password=None, rol:int=None, id:int=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.password = password
        self.rol = rol
        self.id = id

   
          
