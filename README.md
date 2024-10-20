
# Prueba de gestion de empleados
---

**DESCRIPCIÓN:**
Este proyecto para la gstión de empleados utiliza **FastAPI** y **MySQL**.

---
### Herramientas de Desarrollo

![FASTAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white) ![MYSQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


### Entorno de Desarrollo
Para poder ejecutar este proyecto es nesesario instalar las siguientes aplicaciones:

- [Visual Studio Code](https://code.visualstudio.com/download)
- [Postman](https://www.postman.com/downloads/)
- [Python](https://www.python.org/downloads/)
- [MySql Workbench](https://dev.mysql.com/downloads/workbench/)
---
## Correr Localmente

Clonar el projecto

```bash
  git clone https://github.com/EmilioMendozaCortes/PruebaBack.git
```

Abre el projecto

```bash
  cd PruebaBack
```

Instalar dependencias

```bash
   pip install -r requirements.txt
```

Activación del entorno de trabajo
```bash
   employees\Scripts\activate
```

Creación de la Base de Datos en MySql Workbench
```bash
   create database if not exists employees;
   use employees;
```

Configuración para la conexión de la API a Workbench que se encuentra en **/config/db.py/**
```bash
   SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://tuUsuario:tuContraseña@localhost:tuPuerto/employees'

```



Prende el servidor

```bash
   python -m uvicorn app:app --reload
```
---
### Diagrama Entidad-Relación
<p align="center">
  <img src="img/image.png" alt="Sublime's custom image"/>
</p>

---
### Colección de Postman
#### Agregar un nuevo empleado empleado

```http
  POST http://127.0.0.1:8000/employees/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Nombre` | `string` | El o los nombres del empleaso|
| `Primer_Apellido` | `string` | Su primer apellido|
| `Segundo_Apellido` | `string` | Su segundo apellido |
| `CURP` | `string` | Clace Unica de Registro de Población |
| `Puesto` | `string` | Puesto de trabajo(opcional) |
| `Calle` | `string` | Nombre de la calle |
| `NoExterior` | `int` | No. exterior de la casa |
| `NoInterior` | `int` |No. interior de la casa(opcional) |
| `Colonia` | `string` | Colonia a la que pertenece |
| `Municipio` | `string` | Municipio donde se encuentra |
| `Estado` | `string` | Estado donde vive |
| `Pais` | `string` | Pais donde esta |
| `Clave_Jefe_Inmediato` | `string` | Su supervisor(opcional) |
| `subordinados` | `list` | Lista de los subordinados a su cargo |

<p align="center">
  <img src="img/image-1.png" alt="Sublime's custom image"/>
</p>

#### Obtener los registros

```http
  GET /http://127.0.0.1:8000/employees/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

<p align="center">
  <img src="img/image-2.png" alt="Sublime's custom image"/>
</p>

---

### Base de Datos
 de la api mediante el uso de Postman
Se adjunto la BD que se ocupo par hacer las pruebas en el archivo **DataBase.sql**

---

## AUTOR
Elaborado por: [@Emilio Mendoza Cortes](https://github.com/EmilioMendozaCortes)
