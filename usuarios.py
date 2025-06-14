
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

"""esta clase usuarios se creo con la finalidad de evitar el uso de listas y manejo de indices para recuperar cada propiedad que es la que tiene el objeto instanciado.
    cuando se iniciliza un objeto por defecto esta vacio como se ve en el metodo __init__ porque púede existir la posibilidad de devolver un objeto vacio.
    el siguiente metodo modificar es para completar las propiedades del objeto
"""""   
          
