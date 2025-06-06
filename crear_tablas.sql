/* revisar, RELACION 1 A 1, COMPLETO TABLA 1, ME DEVUELVE UN ID Y CON ESE ID HAGO EL INSERT EN LA SIGUIENTE TABLA, PORQUE NO PUEDEN EXISTIR UN USUARIO CON VARIOS REGISTROS
DE DATOS SENSIBLES */ 
CREATE TABLE usuarios_login ( 
                        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        usuario VARCHAR(255) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL,
                        rol VARCHAR(20) DEFAULT 'usuario_estandar' );

CREATE TABLE datos_sensibles (
                        id_datos INT AUTO_INCREMENT PRIMARY KEY,
                        id_usuario INT NOT NULL UNIQUE,
                        nombre VARCHAR(255) NOT NULL,
                        apellido VARCHAR(255) NOT NULL,
                        dni VARCHAR(50) DEFAULT 'sin completar',
                        celular VARCHAR(50) DEFAULT 'vacio',
                        domicilio VARCHAR(255) default 'sin completar',
                        FOREIGN KEY(id_usuario) REFERENCES usuarios_login(id_usuario));

                                               