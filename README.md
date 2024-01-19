# MonoRepo de Aplicación Bancaria Básica (Test)

Esta aplicación sencilla permite realizar varias operaciones contra un backend levantado en Python + Flask y corre sobre un servidor en render.com como un webservice. El frontend funciona sobre un LAMP básico, utilizando MySQL como base de datos en un servidor remoto.

**NOTA:**
1. Se ha experimentado un lag en la primera peticion cuando el servidor donde se alojan los webservices  se encuentra en inactividad, es normal por el nivel de servicio free que se dispone en este proveedor.
2. El backend (Python) se encuentra en render. www.render.com
3. No incorpora certificado SSL por ser un proyecto de prueba.
4. Por la naturaleza de prueba de esta aplicacion , las conexiones a la BDD estan expuestas. No estan implementadas seguridades 

-Link para pruebas: [https://18.233.158.250/](https://18.233.158.250/)  (AWS LIGHTSAIL)

En caso de no funcionar el primer link, Tambien esta alojado en este servidor [http://davoramirez.online/](http://davoramirez.online/) 
-Una coleccion de postman esta disponible en el monorepo para realizar pruebas directamente contra el backend.

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

## Ejecucion 
-Clonar este repo
-Instalar dependencias 
  -pip install virtualenv
  -virtualenv venv
 - source venv/bin/activate 
 - pip install Flask
 - pip install Flask-SQLAlchemy

#Esctructura de archivos del proyecto

![image](https://github.com/davoweb3/ejerciciobk/assets/105182325/eac0b79c-98e3-4bf2-8eeb-52c090475472)





