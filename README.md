# Prueba-Tecnica
Prueba técnica para obtar al cargo de desarrollador backend

Para la tarea uno, se desarrollaron dos pequeñas funciones,
una que trae la lista de jurisprudencias de la página dada y 
la otra que se encarga de subir la información a la base de datos.
Todo esto utilizando la libreria Requests de python y el framework de 
desarrollo web Django.

Durante el desarrollo de estas funciones, tome algunas consideraciones que voy a detallar:
- No almaceno toda la información obtenida de la página, pues es demasiada y considere que 
no toda era tan relevante.
- El formato de la fecha que se guarda dentro de la base de datos es "YYYY-MM-DD", esto es
por que por defecto Postres utiliza ese formato.
- Cierta información que se obtenía no era muy descriptiva, asi que para facilitar su compresión
dentro de la base de datos, codifique pequeñas porciones de código a fin de que está información se 
almacenara lo más fiel a la página y que sea más descriptiva a la hora de ser visualizada.

Para la ejecución del código se debe:
- Abrir el archivo settings.py utilizando un editor de texto o un editor de código
- Buscar dentro del código la parte referente a la base de datos, esta la deje marcada con un comentario, 
el cual empieza con un "#"
- Cambiar los parametros "USER" y "PASSWORD" a los que correspondan a usted,
en mi caso el usuario es "postgres" y la contraseña es "sql"
- Abrir un terminal.
- Utilizar el comando cd para moverse entre los directorios hasta llegar.
a la carpeta principal de la tarea, en este caso "tarea1".
- Utilizar el comando "python manage.py makemigrations".
- Utilizar el comando "python manage.py migrate", para aplicar los cambios y que 
se cree la base de datos junto con la tabla necesaria para que funcione la aplicación.
- Utilizar el comando "python manage.py runserver".
- Utilizando un navegador, dirigirse a la ruta "http://localhost:8000/.
- Visualizar la información en pantalla.
- Visualizar la base de datos con la información subida. 

Para la tarea dos, se desarrollo un script que si bien no está completo,
supone una base para la interacción y extracción de información de una página web.
Esto se realizó utilizando Selenium Webdriver.

Para ejecutar el código se debe:
- Abrir una terminal y dirigirse a la carpeta de la tarea, en este caso "tarea2".
- Ejecutar el comando "python app.py".
- Ver como funciona el script.

El script no está completo ya que debido a la estructura de la página, se dificulta 
el poder interactuar con los elementos necesarios, es por esto que el script intentará
encontrar ciertos elementos sin tener exito. Intente solucionar esto utilizando varios métodos,
sin tener éxito alguno, sin embargo, creo que el código que está escrito puede llegar a funcionar 
si se descubriera como poder interactuar con los elementos.