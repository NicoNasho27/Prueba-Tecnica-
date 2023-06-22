#Aplicación de prueba de extracción de datos de una tabla según parametros dados en el test
#No es una versión funcional ya que es dificil interactuar con la página por razones que desconozco, el error más común es que no encuentra
#Los elementos select con los que se debe interactuar
#Sin embargo, esto puede servir de base para la interacción con los elementos y el procesado de los datos

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

#Se crea la función encargada de realizar la interacción con la página y el recopilado de los datos
def tarea2():

    #Se inicializa el driver que interactuará con la página
    driver = webdriver.Chrome()
    #Se maximiza la pantalla
    driver.maximize_window()
    #Se especifica la página con la que se va a interactuar
    driver.get("https://www.concesionesmaritimas.cl/")
    time.sleep(3)
   
    #Se crea una instancia para esperar a que se cumplan ciertas condiciones antes de que el script falle y se cierre
    wait = WebDriverWait(driver, 20)

    # Debido a que la pagina tiene distintos frames, esto puede dificultar la interacción con los elementos
    # Con esto, nos aseguramos de utilizar el frame correcto, en el cual están los elementos que necesitamos ocupar 
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "centro_sigmar")))
    # Buscamos el primer Select, en este caso el de regiones, utilizando la ruta de html donde está ubicado
    select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/font/form/center/table[1]/tbody/tr[2]/td[1]/select')))
    
    # Se convierte a una instancia de tipo Select, para poder ocupar los métodos propios de este tipo de instancias
    select = Select(select_element)
    # Se selecciona la opción 2, ya que es la que corresponde a la segunda región
    select.select_by_value(2)

    # Mismo proceso de antes
    select_element2 = wait.until(EC.presence_of_element_located((By.NAME, "variableGobmar")))
    select2 = Select(select_element2)
    select2.select_by_value(12)

    # Nuevamente y por última vez realizamos la misma operación
    select_element3 = wait.until(EC.presence_of_element_located((By.NAME, "variableCapuerto")))
    select3 = Select(select_element3)
    select3.select_by_value(13)

    # Ahora esperamos a que la tabla resultante de datos a partir de los filtros anteriores sea visible
    wait.until(EC.element_located_to_be_selected((By.XPATH), "/html/body/font/form/div/center/table"))

    # Almacenamos esta tabla en una variable
    table = driver.find_element(By.XPATH, "/html/body/font/form/div/center/table")

    # Utilizamos la propiedad text de la variable table para obtener toda la información que esta posea
    data = table.text

    # Despues de esto quedaria organizar los datos en formato json y escribirlos en un archivo de esta misma extensión
    # Seguidamente se cambiaría de página de la tabla utilizando el driver de selenium 
    # Y se volvería a hacer el mismo proceso por cada página hasta llegar al final
    
    driver.quit()

tarea2()