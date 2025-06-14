# EA3-ABP
Módulo Iniciación a la Programación y Bases de Datos: Gestor de usuarios (registro e inicio de sesion)

### 👥 Integrantes

#### Candelaria Jazmín Barjollo 
- DNI: 41378648	
- CORREO: candebarjollo@gmail.com	
- GITHUB: candebar

#### Matilde Maidana Sandoval 
- DNI: 33948480	
- CORREO: dis.matilde.m@gmail.com
- GITHUB: Matilde-ms

#### Julio Fernando Lepore 
- DNI: 30267847
- CORREO: juliofernandolepore@gmail.com
- GITHUB: juliofernandolepore
- Stack: full stack (react js - golang - postgresql)

### Consignas

Actividades Integradoras del Módulo

Actividad Integradora N° 3

Programación I
Basándose en los objetivos y requerimientos no funcionales, se solicita:
1. Realizar el Diagrama de Clases, para ello:
a. Identificar las clases del sistema, atributos y métodos y las relaciones entre ellas.
b. Nombrar las clases, atributos y métodos en base a la nomenclatura acordada con el equipo.
c. Realizar el diagrama de clases mediante herramientas como draw.io, lucidchart, creately, miro u otro.

2. Realizar un programa de consola que cumpla con los requerimientos generales del programa que son:
a. Registro de usuarios e inicio de sesión.
b. Si el usuario inició sesión satisfactoriamente, el programa debe proporcionar un menú a los usuarios según el rol como sigue:
i. Usuario estándar. Para acceder sólo a sus datos personales.
ii. Admin. Para visualizar el listado de usuarios registrados, cambiar el rol de un usuario y eliminar usuarios.

Sugerencias para la escritura del código fuente (convenciones de nomenclatura estándar - comunidad de Python):
● Archivos y Directorios
○ Archivos Python: Utilizar el formato snake_case en minusculas. Ejemplo: main.py, module1.py. ○ Directorios: Utilizar nombres en minúsculas sin espacios ni caracteres especiales. Ejemplo: docs, src.

3. Funciones
● Funciones. Utilizar el formato snake_case en minúsculas comenzando la primera palabra con un verbo en infinitivo. Ejemplo: obtener_usuario, actualizar_datos.
● Variables. Utilizar el formato snake_case. Ejemplo: contador,nombre_usuario.
● Constantes. Utilizar el formato snake_case en mayúsculas. Ejemplo: MAX_INTENTOS.

Base de Datos
1. Identificar las entidades principales del sistema.
2. Definir los atributos para cada entidad, considerando los datos necesarios para cumplir con las funcionalidades especificadas.
3. Establecer las relaciones entre las entidades identificadas.
4. Aplicar el proceso de normalización a las entidades y sus atributos para eliminar redundancias y dependencias funcionales. Se debe alcanzar la Tercera Forma Normal (3FN).
5. Crear el modelo relacional resultante de la normalización, representando las entidades como tablas con sus respectivos atributos y relaciones. Definir las
claves primarias y foráneas necesarias para establecer las relaciones entre las tablas.
6. Documentar el diseño de la base de datos, incluyendo una pequeña descripción de cada tabla. Y las aclaraciones que creas necesarias en cada una de ellas. Por ejemplo si se realizó una suposición de algo que no estaba en el enunciado y eso determinó que una relación es uno a muchos, cuando se podría haber interpretado por una ambigüedad que podía ser muchos a
muchos, dejar asentada tal suposición.
7. Definir las consultas necesarias en SQL para implementar el CRUD del usuario, y el script ejecutable.
Notas: En esta etapa, no es necesario desarrollar consultas SQL. El enfoque está en el diseño y estructura de la base de datos. Se recomienda utilizar una herramienta de
modelado de bases de datos, como draw.io, para crear el diagrama del modelo relacional.

### INSTALACIONES NECESARIAS como drivers o librerias en python

pip install python-dotenv

pip install mysql-connector-python

### INSTALACION EXTERNA REQUERIDA

instalar docker desktop o docker cli dependiendo del sistema operativo

ejecucion en terminal del comando "docker compose up" para levantar contenedores con las 2 imagenes