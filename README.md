Loroño Fabrizio Tercer_Entrega

Este proyecto es una aplicación web desarrollada en Django como parte de la Tercera Entrega de Python. La aplicación incluye funcionalidades como la creación, gestión y visualización de datos relacionados con "la gestión de celulares".

Características
    Gestión e implementación de vistas para crear, editar, y listar registros.
    Uso de formularios para la interacción con los usuarios.
    Manejo de datos con modelos Django y una base de datos SQLite por defecto.

Requerimientos
    asgiref==3.8.1
    Django==5.1.4
    sqlparse==0.5.3
    tzdata==2024.2

Instalación y visualización

Clona el repositorio:

git clone https://github.com/FabriArieL/django_TerceraEntrega.git
cd django_TerceraEntrega

Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instala las dependencias:

pip install -r requirements.txt

Realiza las migraciones de la base de datos:

python manage.py migrate

Ejecuta el servidor de desarrollo:

python manage.py runserver

Abre tu navegador y accede a http://localhost:8000.

Estructura del proyecto

django_TerceraEntrega/
├── inicio/             # Aplicación principal del proyecto
├── templates/          # Plantillas HTML
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── db.sqlite3          # Base de datos SQLite
├── manage.py           # Script de gestión de Django
└── requirements.txt    # Dependencias del proyecto
