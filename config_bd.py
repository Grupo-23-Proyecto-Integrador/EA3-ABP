import mysql.connector , os
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("MYSQLUSER")
password = os.getenv("MYSQLPASSWORD")
root_password = os.getenv("MYSQL_ROOT_PASSWOR")

""" esta clase unicamente se encarga de interactuar con la base de datos, unica responsabilidad a traves de sus metodos
    los metodos corresponden a un CRUD (crear, leer, actualizar, borrar) de gestion de usuarios.
    el primer metodo de esta clase configura el objeto con todas las configuraciones de la base da datos mysql que se encuentran configurados en el archivo .env (variables de entorno).
    los metodos conectar y cerrar_conexion cumplen la finalidad de preparar la conexion y cerrar la conexion luego de la consulta (cada matodo).
    el objeto instanciado y configurado sera exportado de este modulo hacia el modulo principal o main.py
 """

class Conexion_mysql:

    def mysql_configurar(self, mysql_host:str, mysql_database:str, mysql_user:str, mysql_password:str):
        # define conexion mysql
        self._host = mysql_host
        self._database = mysql_database
        self._user = mysql_user
        self._password = mysql_password
        self._estado_conexion = None
    
    def conectar(self):                        
        if self._estado_conexion is None or not self._estado_conexion.is_connected():
            try:
                # muy importante aca estoy instanciando un objeto de la libreria mysql(connector.connect)
                # se le pasan los argumentos del metodo __init__
                self._estado_conexion = mysql.connector.connect(
                    host=self._host,
                    database=self._database,
                    user=self._user,
                    password=self._password
                )
                if self._estado_conexion.is_connected():
                    # is_connected (es un metodo heredado)
                    print(f"")
                    # el print de mostrar conexion exitosa es opcional, estaba para comprobar que efectivamente funcione
                return self._estado_conexion
                # si la conexión fue exitosa
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
                return None
                #retorna None en caso de no ser exitosa la conexion.
        else:
            return self._estado_conexion
   
    def cerrar_conexion(self):       
        
        if self._estado_conexion and self._estado_conexion.is_connected():
            self._estado_conexion.close()
            # Conexión mysql cerrada, hago un print si lo veo necesario
    
    def insert_usuario(self , nombre, apellido, usuario, email, password):
        # revisar este metodo constantemente ya que esta el rediseño de las tablas y sus relaciones
        # retorna true si fue exitosa la consulta sino retorna false porque algo salio mal
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # verifica la existencia del usuario
            cursor = conexion.cursor()
            verificar = "SELECT 1 FROM usuarios_login WHERE usuario = %s LIMIT 1"
            cursor.execute(verificar, (usuario,))
            if cursor.fetchone():
                print(f'el usuario: {usuario} ya existe')
                return False
            # verifica la existencia del email
            verificar = "SELECT 1 FROM usuarios_login WHERE email = %s LIMIT 1"
            cursor.execute(verificar, (email,))
            if cursor.fetchone():
                print(f'el usuario: {email} ya existe')
                return False
            consulta = "INSERT INTO usuarios_login (nombre, apellido, usuario, rol, email, password_usuario) VALUES (%s,%s,%s,%s,%s,%s)"
            usuario_estandar = 2
            cursor.execute(consulta, (nombre, apellido, usuario, usuario_estandar, email, password))
            # solucionado, habia puesto una sintaxis de postgres y eso me daba error en el return id
            id_generado = cursor.lastrowid
            self.conectar().commit()            
            print(f'registro exitoso id: {id_generado} del usuario: {usuario} con el email: {email}')
            return True
        except Exception as e:
            print(f'error al insertar el usuario, error: {e}')
        finally:
            if cursor:
                cursor.close()

    def consultar_usuario_email(self , email, password):        
        # consultar usuario por email y password
        # retorna datos para crear una sesion activa
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # verifica la existencia del usuario
            cursor = conexion.cursor()
            verificar = "SELECT id_usuario, rol, usuario FROM usuarios_login WHERE email = %s AND password = %s"
            cursor.execute(verificar, (email,password))
            resultado = cursor.fetchone()
            # retorna una tupla, ver si puede crearse una clase para simplificar
            if resultado == True:
                return {
                    "id": resultado[0],
                    "rol": resultado[1],
                    "usuario": resultado[2]
                }    
            else:
            # retorno una tupla vacia    
                return {
                    "id": "",
                    "rol": "",
                    "usuario": ""
                } 
        except Exception as e:
            print(f'error al consultar el email y password, error: {e}')
            # retorno una tupla vacia    
            return {
                    "id": "",
                    "rol": "",
                    "usuario": ""
                } 
        finally:
            if cursor:
                cursor.close()
                conexion.close()

    def consultar_username(self , u, password):
        """este metodo pertenece a la clase Clase_mysql y requiere 3 argumentos: el self del constructor, el nombre de usuario y la contraseña.
           este metodo devuelve una lista porque sus elementos son de distinto tipo de dato (int , str) que luego seran desestructurados fuera de este metodo
           la lista retornada contiene id, rol (id) y nombre de usuario segun la consulta sql abajo detallada        
        """       
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        id = 0
        rol = 0
        usuario = ""
        try:
            # verifica la existencia del usuario
            cursor = conexion.cursor()
            # la consulta retorna 3 campos
            
            verificar = "SELECT id_usuario, rol, usuario FROM usuarios_login WHERE usuario = %s AND password_usuario = %s"
            cursor.execute(verificar, (u ,password))
            # el metodo fetchone devuelve una tupla
            resultado = cursor.fetchone()            
            id , rol, usuario = resultado
            if id > 0 and usuario != "" and rol > 0:
                res = [id, rol, usuario]                
                return res
            else:
                id =""                                               
                res = [id, rol, usuario]               
                return res  
        except Exception as e:
            print(f'su usuario o contraseña son incorrectos intente nuevamente')
            # retorno una tupla vacia
            id = ""    
            res = [id, rol, usuario]                
            return res 
        finally:
            if cursor:
                cursor.close()
                conexion.close()

    def ver_usuarios(self):
        # trae un resultado con todos los usuarios del sistema considerando que es un resultado pequeño, no requiere argumentos
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # instancio un objeto cursor con todos los metodos para interactuar con la bd
            cursor = conexion.cursor()
            consulta = " SELECT id_usuario, usuario, nombre, apellido, email, rol FROM usuarios_login; "
            cursor.execute(consulta)
            # el metodo fetchone devuelve una tupla
            resultado = cursor.fetchall()
            # utilizo una clase sesion para manejar los datos
            if resultado: 
                return resultado            
            else:
            # retorno una tupla vacia    
                return "sin resultados"
        except Exception as e:
            print(f'error al efectuar la consulta: {e}')
            # retorno una tupla vacia    
            return resultado 
        finally:
            if cursor:
                cursor.close()
                conexion.close() 

    def mis_datos(self, id:int):
        print(id)
        # trae mis datos de usuario, el argumento requerido es mi id
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # instancio un objeto cursos con todos los metodos para interactuar con la bd
            cursor = conexion.cursor()
            # consulta de mis datos de ambas tablas
            verificar = "SELECT id_usuario, usuario, rol, nombre, apellido, email  FROM usuarios_login WHERE id_usuario = %s;"
            cursor.execute(verificar, (id,))
            # el metodo fetchone devuelve una sola tupla
            resultado = cursor.fetchone()            
            if resultado: 
                return resultado            
            else:
            # retorno una tupla vacia    
                return "sin resultados"
        except Exception as e:
            print(f'error al efectuar la consulta: {e}')
            # retorno una tupla vacia    
            return "sin resultados"
        finally:
            if cursor:
                cursor.close()
                conexion.close()

    def eliminar_usuario_id(self, id_usuario):        
        operacion = False        
        # retorna un aviso de borrado exitoso
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # instancio un objeto cursor
            cursor = conexion.cursor()
            # la consulta retorna 1 valor (del id eliminado)
            borrar = f"DELETE FROM usuarios_login WHERE id_usuario = {id_usuario}"
            cursor.execute(borrar)
            # el metodo lastrowid
            resultado = cursor.lastrowid()           
            if resultado > 0:
                print(f"id: {resultado} con exito")
                operacion = True                
                return operacion 
            else:
            # retorno el id resultado fallido
            # operacion fallida
                print("no se pudo eliminar el id, intente nuevamente con un id diferente")    
                return operacion
        except Exception as e:
            print(f'no se pudo eliminar el usuario con id: {id_usuario} y el error es el siguiente: {e}')
            return operacion            
        finally:
            if cursor:
                cursor.close()
                conexion.close() 

    def editar_usuario(self, nombre, apellido, email, usuario, password_usuario, rol, id_usuario):
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # instancio un objeto cursor
            cursor = conexion.cursor()
            # la consulta retorna 1 valor (del id editado)
            editar = (f"UPDATE usuarios_login SET nombre = %s, apellido = %s, email = %s, usuario = %s , password_usuario = %s, rol = %s WHERE id_usuario = %s")           
            cursor.execute(editar, (nombre, apellido, email, usuario, password_usuario, rol, id_usuario,))
            # el metodo lastrowid
            resultado = cursor.lastrowid()           
            if resultado < 0:
                print(f"id: {resultado} con exito")                                
                return True
            else:
            # retorno el id resultado fallido
            # operacion fallida
                print("no se pudo editar el id, intente nuevamente con un id diferente")    
                return False
        except Exception as e:
            print(f'no se pudo editar el usuario con id: {id_usuario} y el error es el siguiente: {e}')
            return False           
        finally:
            if cursor:
                cursor.close()
                conexion.close()                

# creo un objeto de la clase Clase_mysql
conexion_instanciada = Conexion_mysql()
"""utilizo el metodo para configurar el objeto:
    host: el ip o localhost
    database: nombre de la base de datos
    user: es el usuario de la base de datos
    password: es la contraseña para acceder a la base de datos
"""
# metodo para configurar valores
conexion_instanciada.mysql_configurar(host,database,user,password)                 