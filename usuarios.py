class Usuarios:
    __sesion_activa = False
    # roles o usuarios : Admin / Usuario estandar

    def __init__(self, nombre:str, apellido:str, email:str, usuario:str, password:str, rol:str= None):
    # creacion de atributos o propiedades del objeto que se va a instanciar
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.__password = password
        self.rol = rol

    def info(self):
    # creacion de metodo de la clase para mostrar atributos (publicos o permitidos)    
        print(f'''
              nombre: {self.nombre}, 
              apellido: {self.apellido}, 
              email: {self.email},
              usuario: {self.usuario} 
              rol: {self.rol}''')
