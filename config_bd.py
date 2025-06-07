import mysql.connector , sesiones
from mysql.connector import Error

# este modulo cumple la funcion del MODEL o parte del negocio que exclusivamente interactua con la BD, es una representacion porque solo esta declarada la clase con sus metodos

class Clase_mysql:
    # metodo inicial para configurar los datos de la conexion
    def mysql_configurar(self, mysql_host, mysql_database:str, mysql_user:str, mysql_password:str):
        # define conexion mysql
        self.host = mysql_host
        self.database = mysql_database
        self.user = mysql_user
        self.password = mysql_password
        self.estado_conexion = None
    # metodo: Establece y devuelve una conexión a la base de datos MySQL. o devuelvo None
    def conectar(self):                        
        if self.estado_conexion is None or not self.estado_conexion.is_connected():
            try:
                # muy importante aca estoy instanciando un objeto de la libreria mysql(connector.connect)
                # se le pasan los argumentos del metodo __init__
                self.estado_conexion = mysql.connector.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
                if self.estado_conexion.is_connected():
                    # is_connected (es un metodo heredado)
                    print(f"")
                    # el print de mostrar conexion exitosa es opcional, estaba para comprobar que efectivamente funcione
                return self.estado_conexion
                # si la conexión fue exitosa
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
                return None
                #retorna None en caso de no ser exitosa la conexion.
        else:
            return self.estado_conexion
    # Cierra la conexión activa a la base de datos, si existe.
    def cerrar_conexion(self):       
        
        if self.estado_conexion and self.estado_conexion.is_connected():
            self.estado_conexion.close()
            # Conexión mysql cerrada, hago un print si lo veo necesario
    # Creo una consulta Insert (nuevo usuario)
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
            # si de ambas columnas no se encuentran registro procede al sql de insert en tablas separadas            
            # insertar usuario email y password en tabla usuarios_login
            # le pido que me retorne el id generado para hacer el insert en la tabla datos sensibles (relacion 1 a 1)
            consulta = "INSERT INTO usuarios_login (usuario, email, password_usuario) VALUES (%s,%s,%s)"
            cursor.execute(consulta, (usuario, email, password))
            # solucionado, habia puesto una sintaxis de postgres y eso me daba error en el return id
            id_generado = cursor.lastrowid
            self.conectar().commit()
            # insertar nombre y apellido en la tabla datos_sensibles
            # id_usuario es el campo de la llave foranea que manualmente debo insertar (relacion 1 a 1)
            insert = "INSERT INTO datos_sensibles (id_usuario, nombre, apellido) VALUES (%s,%s,%s)"
            cursor.execute(insert,(id_generado, nombre, apellido))            
            self.conectar().commit()
            print(f'registro exitoso del usuario: {usuario} con el email: {email}')
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

    def consultar_username(self , usuario, password):
        # consultar usuario por nombre de usuario y password
        # retorna datos para crear una sesion activa
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # verifica la existencia del usuario
            cursor = conexion.cursor()
            # la consulta retorna 3 campos
            verificar = "SELECT id_usuario, rol, usuario FROM usuarios_login WHERE usuario = %s AND password_usuario = %s"
            cursor.execute(verificar, (usuario,password))
            # el metodo fetchone devuelve una tupla
            resultado = cursor.fetchone()
            # utilizo una clase sesion para manejar los datos
            d = sesiones.Nueva_Sesion()
            id , rol, usuario = resultado
            if id > 0 and usuario != "" and rol != "":
                d.configurar_sesion(id, rol, usuario)
                return d    
            else:
            # retorno una tupla vacia    
                return d
        except Exception as e:
            print(f'su usuario o contraseña son incorrectos intente nuevamente')
            # retorno una tupla vacia    
            return d 
        finally:
            if cursor:
                cursor.close()
                conexion.close()

    def ver_usuarios(self):
        # trae un resultado con todos los usuarios del sistema considerando que es un resultado pequeño
        # no requiere argumentos
        conexion = self.conectar()
        if not conexion:
            print(f'no se pudo establecer conexion con la BD')
            return False
        
        try:
            # instancio un objeto cursos con todos los metodos para interactuar con la bd
            cursor = conexion.cursor()
            # consulta
            consulta = f"""SELECT 
                            u.id_usuario, 
                            u.email, 
                            u.usuario, 
                            u.rol, 
                            ds.nombre, 
                            ds.apellido, 
                            ds.dni, 
                            ds.celular, 
                            ds.domicilio 
                        FROM usuarios_login AS u LEFT JOIN datos_sensibles AS ds ON u.id_usuario = ds.id_usuario;"""
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