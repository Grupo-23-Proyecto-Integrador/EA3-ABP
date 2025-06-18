/* cumplimiento de la 3FN (TERCERA FORMA NORMAL)
con este diseño se evita la redundancia de datos, 
si se cambia un dato de la descripcion de roles no hay que modificar de forma repetida en la tabla usuarios_login,
si los datos de rol estuvieran colocados de forma manual en cada uno de los usuarios habria repeticion o desorden con los roles,
no hay atributos no claves  que dependan de atributos no claves, solo hay relacion a traves de llaves primarias y foraneas,
hay separacion de entidades (como objetos con sus propiedades),
 */ 

CREATE TABLE roles (
                    id_rol INT AUTO_INCREMENT PRIMARY KEY,
                    nombre_rol VARCHAR(50) UNIQUE,
                    descripcion_rol VARCHAR(255)
); 

CREATE TABLE usuarios_login ( 
                        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                        rol INT NOT NULL,
                        nombre VARCHAR(255) NOT NULL,
                        apellido VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        usuario VARCHAR(255) NOT NULL UNIQUE,
                        password_usuario VARCHAR(255) NOT NULL,
                        FOREIGN KEY(rol) REFERENCES roles(id_rol));

                                             