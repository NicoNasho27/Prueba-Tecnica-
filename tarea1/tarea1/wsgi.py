# Archivo de rutas de la aplicación, utilizado más que nada para mostrar los datos que vienen desde el modulo Request
# En la pantalla del navegador

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarea1.settings')

application = get_wsgi_application()
