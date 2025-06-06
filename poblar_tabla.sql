/* efectuar un insert con multiples valores.
script o consulta sql requerido en la consigna para poblar o rellenar la tabla con datos simulados para probar la app */

INSERT INTO 
usuarios_login (email, usuario, password_usuario, rol ) 
VALUES 
    ("Matiastejerina94@gmail.com", "MatiasTejerina07", "0123456789", "Admin"),
    ("candebarjollo@gmail.com", "candebar", "0987654321", "Admin"),
    ("dis.matilde.m@gmail.com", "Matilde-ms", "1111111111", "usuario_estandar"),
    ("gerardolauroromero@gmail.com", "GerLR", "0000000000", "usuario_estandar" ),
    ("juliofernandolepore@gmail.com", "ferchu83", "pongoDigitos", "Admin");