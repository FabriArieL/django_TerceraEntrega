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

Mejoras para la EntregaFinal

Los requerimientos fueron actualizados

Requerimientos
    asgiref==3.8.1
    Django==5.1.4
    pillow==11.0.0
    python-dotenv==1.0.1
    sqlparse==0.5.3
    tzdata==2024.2

Agregamos a la app motos(con la posibilidad de crearlas, ver sobre ellas, editar sus datos, y eliminarlas),

usuarios(ahora solo podemos editar y eliminar celulares o motos, iniciando sesion en un usuario existente, o podemos crear uno nuevo, tambien podemos editarlo, ponerle un avatar x ej, y cambiarle la contraseña)

y un sistema de mensajería(contamos con un apartado nuevo que aparece una vez iniciamos sesion con un usuario, con este apartado podemos elegir a otro usuario al cual mandarle un mensaje, tambien podemos ver el contenido, la fecha, como el emisor y receptor, tanto desde el usuario que mando el mensaje como el que lo recibió)

Estructura del proyecto actualizada

django_TerceraEntrega/
├── inicio/             # Aplicación principal
│   ├── models.py       # Modelos de datos
│   ├── views.py        # Lógica de vistas
│   ├── urls.py         # Rutas principales
│   ├── templates/      # Plantillas HTML
│   ├── static/         # Archivos estáticos (CSS, JS, imágenes)
│   ├── forms.py        # Formularios
│   └── admin.py        # Configuración del panel de administración
│
├── productos/          # Gestión de productos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── usuarios/           # Gestión de usuarios
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── mensajeria/         # Sistema de mensajería
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── db.sqlite3          # Base de datos SQLite
├── manage.py           # Herramienta de gestión Django
└── requirements.txt    # Dependencias del proyecto

Video del proyecto en funcionamiento: https://www.youtube.com/watch?v=ad-n_SF3zbo
