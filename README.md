# MonoRepo de aplicacion bancaria basica solicitada como test.

Esta aplicacion sencilla permite realizar varias operaciones contra un backend levantado en Python + Flash , corre sobre render como un webservice.
El frontend corre sobre un lamp BASICO , la BDD es MySQL y corre en un servidor remoto 

NOTA:
1) EL servidor donde se aloja es gratuito por lo que los tiempos de respuesta pueden ser lentos en cada peticion
2) EL backend ( python) se encuentra en un plan de render gratuito por lo que entra en suspension y se requiere ejecutar la primera orden y regresa ( 10 s)
3) No incorpora certificado SSL por ser un proyecto de prueba .
   

Link para testing: http://davoramirez.online/

#Arquitectura 
Frontend (LAMP Server):

Tecnologías:
Linux (OS)
Apache (Web Server)
MySQL (Database)
PHP (Server-side scripting)
Funcionalidad:
Sirve páginas web dinámicas.
Interactúa con el microservicio a través de solicitudes HTTP.
Microservicio (Python Flask):

#Tecnologías:
Python Lenguaje
Flask (Web Framework)
SQL Alchemy (ORM para interactuar con la BDD)

#Funcionalidad:
Ofrece servicios específicos del backend.
Se conecta a la base de datos MySQL usando SQL Alchemy para realizar operaciones CRUD.
Recibe solicitudes HTTP desde el frontend y responde con datos o realiza acciones en la base de datos.
Base de Datos:MySQL

#Diagrama de la Arquitectura 
+-----------------+        +------------------+       +----------------------+
|                 | HTTP   |                  | SQL   |                      |
|   Frontend      +-------->  Microservicio   +------->      Base de Datos   |
|  (LAMP Server)  |        |   (Python Flask) |       |      (MySQL)         |
|                 |        |                  |       |                      |
+-----------------+        +------------------+       +----------------------+





-----------------------------Pruebas desde Postman--------------------------------------------
#1.Crear un nuevo usuario:
Endpoint: POST http://localhost:5000/create_user
jsonCopy code{ "nombres": "Nombre Ejemplo", "email": "correo@ejemplo.com", "username": "usuario_ejemplo", "password": "contraseña", "cuenta": "1234567890", "saldo": 1000.0}

#2. Actualizar un usuario existente:
Endpoint: PUT http://localhost:5000/update_user/ (reemplaza con el ID del usuario que deseas actualizar)
jsonCopy code{ "nombres": "Nuevo Nombre", "email": "nuevo_correo@ejemplo.com", "saldo": 1500.0}

#3. Eliminar un usuario:
Endpoint: DELETE http://localhost:5000/delete_user/ (reemplaza con el ID del usuario que deseas eliminar)

#4. Obtener información de un usuario:
Endpoint: GET http://localhost:5000/get_user/ (reemplaza con el ID del usuario que deseas obtener)

#5. Listar todos los usuarios:
Endpoint: GET http://localhost:5000/list_users/ (reemplaza con el ID del usuario que deseas obtener)

#6. Simular una transferencia :
Endpoint: POST http://127.0.0.1:5000/transfer_balance/
  { "remitente_username": "edgarr2ss3", "beneficiario_username": "usuario_2", "amount": 100.0}

#7. Simular un depósito en cuenta por parte del cajero
Endpoint: POST http://127.0.0.1:5000/deposit
  { "username": "edgarr2ss3", "amount": 100.0}






