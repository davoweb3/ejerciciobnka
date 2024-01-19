# MonoRepo de Aplicación Bancaria Básica (Test)

Esta aplicación sencilla permite realizar varias operaciones contra un backend levantado en Python + Flask y corre sobre un servidor en render.com como un webservice. El frontend funciona sobre un LAMP básico, utilizando MySQL como base de datos en un servidor remoto.

**NOTA:**
1. El servidor donde se aloja es gratuito, por lo que los tiempos de respuesta pueden ser lentos en cada petición.Si al realizar una peticion se recibe un error de lectura de base de datos, porfavor regresar y reintentar.
2. El backend (Python) se encuentra en un plan de render gratuito, por lo que entra en suspensión y se requiere ejecutar la primera orden y regresa (10 s).
3. No incorpora certificado SSL por ser un proyecto de prueba.

Link para pruebas: [http://davoramirez.online/](http://davoramirez.online/)
#Una coleccion de postman esta disponible en el monorepo

## Arquitectura

### Frontend (LAMP Server):

**Tecnologías:**
- Linux (OS)
- Apache (Web Server)
- MySQL (Database)
- PHP (Server-side scripting)

**Funcionalidad:**
- Sirve páginas web dinámicas.
- Interactúa con el microservicio a través de solicitudes HTTP.

### Microservicio (Python Flask):

**Tecnologías:**
- Python (Lenguaje)
- Flask (Web Framework)
- SQL Alchemy (ORM para interactuar con la BDD)

**Funcionalidad:**
- Ofrece servicios específicos del backend.
- Se conecta a la base de datos MySQL usando SQL Alchemy para realizar operaciones CRUD.
- Recibe solicitudes HTTP desde el frontend y responde con datos o realiza acciones en la base de datos.

### Base de Datos: MySQL

## Diagrama de la Arquitectura
![image](https://github.com/davoweb3/ejerciciobk/assets/105182325/2d2a2836-aa78-402a-9cac-878f458a6280)

