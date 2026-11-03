Extracción y Almacenamiento Seguro de Datos vía API
Descripción
Este proyecto realiza una extracción de datos desde la API pública JSONPlaceholder mediante una petición HTTP GET.

Los datos obtenidos son procesados y almacenados en un archivo JSON estructurado, aplicando buenas prácticas de desarrollo como el uso de variables de entorno y manejo de errores.

Tecnologías utilizadas
Python 3
Requests
Python-dotenv
Estructura del proyecto
api-data-extraccion/
│
├── .env.example
├── .gitignore
├── README.md
├── extract_data.py
└── data_extracted.json
Configuración
Crear un archivo .env basado en .env.example:

API_URL=https://jsonplaceholder.typicode.com/users
Instalación
Instalar las dependencias necesarias:

pip install requests python-dotenv
Ejecución
Ejecutar el script:

python extract_data.py
Funcionalidades implementadas
Consumo de una API pública mediante una petición GET.
Uso de variables de entorno para la configuración.
Transformación básica de los datos obtenidos.
Almacenamiento de resultados en formato JSON.
Manejo de errores mediante bloques try/except.
Archivo de salida
El script genera el archivo:

data_extracted.json
Este archivo contiene información procesada de los usuarios obtenidos desde la API.

API utilizada
JSONPlaceholder

https://jsonplaceholder.typicode.com/users
