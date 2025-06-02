/* revisar */ 
CREATE TABLE usuarios_login ( 
                        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        usuario VARCHAR(255) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL,
                        rol VARCHAR(20) DEFAULT 'usuario_estandar',
                        id_datos_sesibles INT NOT NULL REFERENCES datos_sensibles(id_datos) );

CREATE TABLE datos_sensibles (
                        id_datos INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(255) NOT NULL,
                        apellido VARCHAR(255) NOT NULL,
                        dni VARCHAR(50) DEFAULT 'sin completar');

                                               