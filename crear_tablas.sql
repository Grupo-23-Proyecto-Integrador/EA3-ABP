/* cumplimiento de la 3FN (TERCERA FORMA NORMAL) */ 

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

                                             