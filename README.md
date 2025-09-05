# 📊 FastAPI CSV Loader for Snowflake

Este proyecto permite subir archivos CSV sin encabezado y realizar inserciones controladas en tablas de Snowflake usando **FastAPI**.  
Está diseñado para manejar grandes volúmenes de datos en bloques de hasta **1000 registros por solicitud**, evitando duplicados y respetando la estructura de cada tabla.

---

## 🚀 Funcionalidades

- 📂 Subida de archivos CSV sin encabezado  
- 🔄 Inserción de hasta 1000 registros por solicitud  
- 🧩 Detección automática del último `id` insertado  
- 🛡️ Evita duplicados por clave primaria  
- 📊 Compatible con las siguientes tablas:
  - `departments`
  - `jobs`
  - `hired_employees`

---

## 📁 Estructura del proyecto

fastapi-snowflake-loader/
│── Main.py # Archivo principal con los endpoints
│── Cargue_batch.py ​​# Lógica de inserción por bloques
│── ConexionDB.py # Conexión a Snowflake
│── Querys.py # End points de consulta
│── requisitos.txt # Dependencias del proyecto
│── README.md # Documentación del proyecto
└── venv/ # Entorno virtual (no subir a GitHub)

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo


2. Instalar las dependencias:

pip install -r requirements.txt


3. Levante el servidor FastAPI:

uvicorn Main:app --reload


4. Acceda a la documentación interactiva:

Interfaz de usuario Swagger → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

## 📦 Requisitos

El archivo requirements.txtincluye dependencias como:

Fastapi

uvicornio

conector de copo de nieve de Python

pandas (si procesas CSV antes de insertarlos)


Autor

Juan Carlos Salamanca