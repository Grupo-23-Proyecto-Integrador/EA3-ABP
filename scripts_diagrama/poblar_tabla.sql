/* efectuar un insert con multiples valores.
script o consulta sql requerido en la consigna para poblar o rellenar la tabla con datos simulados para probar la app */

INSERT INTO roles (nombre_rol , descripcion_rol) VALUES 
('Admin' , 'persona encargada o con permisos de administrar el sistema'),
('usuario_estandar', 'usuario sin permisos de edicion o solo limitado a la visualizacion de sus propia informacion');

INSERT INTO 
usuarios_login (nombre, apellido, email, usuario, password_usuario, rol ) 
VALUES 
    ("matias", "tejerina", "Matiastejerina94@gmail.com", "MatiasTejerina07", "0123456789", 1),
    ("candelaria", "barjollo","candebarjollo@gmail.com", "candebar", "0987654321", 1),
    ("MATILDE", "sandoval", "dis.matilde.m@gmail.com", "Matilde-ms", "1111111111", 2),
    ("gerardo", "romero","gerardolauroromero@gmail.com", "GerLR", "0000000000", 2 ),
    ("fernando", "lepore","juliofernandolepore@gmail.com", "ferchu83", "pongoDigitos", 2);