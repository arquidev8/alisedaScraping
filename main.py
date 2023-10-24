from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# Configurar el web driver
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)  # Aumenta el tiempo de espera implícito a 30 segundos
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 80).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
# href_set = set()
#
# # Crea un DataFrame vacío fuera del bucle
# all_properties_data = pd.DataFrame(columns=["link"])
#
# while True:
#     wait = WebDriverWait(driver, 40)
#     try:
#         ver_mas_btn = wait.until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         print("Fallo el webDriverWait")
#         break
#
#     # Encuentra los elementos del título y del precio
#     urls = driver.find_elements(By.XPATH,"//*[@id='switchMap']/app-property-card/div/div/div/app-card-gallery/div/swiper/div[4]/div[2]/div/a")
#
#     for url in urls:
#         href = url.get_attribute("href")
#         href_set.add(href)
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = [{"link": href} for href in href_set]
#
#     # Añade las nuevas propiedades al DataFrame existente
#     all_properties_data = all_properties_data._append(properties_data, ignore_index=True)
#
#     # Elimina las filas duplicadas
#     all_properties_data = all_properties_data.drop_duplicates(subset=["link"], keep="first")
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#
#         all_properties_data.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()
#


#
# page = 0
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.implicitly_wait(30)  # Aumenta el tiempo de espera implícito a 30 segundos
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?page=" + str(page))
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# href_set = set()
#
# # ... (Importaciones y configuración del webdriver)
#
# # Crea un DataFrame vacío fuera del bucle
# all_properties_data = pd.DataFrame(columns=["link"])
#
# # Itera a través de todas las páginas
# for page in range(430):
#     driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?page=" + str(page))
#
#     # ... (Aceptar las cookies y esperar a que la página cargue)
#
#     # Encuentra los elementos del título y del precio
#     urls = driver.find_elements(By.XPATH,"//*[@id='switchMap']/app-property-card/div/div/div/div[2]/a/a")
#
#     for url in urls:
#         href = url.get_attribute("href")
#         href_set.add(href)
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = [{"link": href} for href in href_set]
#
#     # Añade las nuevas propiedades al DataFrame existente
#     all_properties_data = all_properties_data._append(properties_data, ignore_index=True)
#
#     # Elimina las filas duplicadas
#     all_properties_data = all_properties_data.drop_duplicates(subset=["link"], keep="first")
#
#     # Vacía el conjunto href_set para la siguiente página
#     href_set.clear()
#
#     # Guarda el DataFrame en un archivo de Excel cada 20 propiedades
#     if (page + 1) % 20 == 0:
#         file_counter = (page + 1) // 20
#         all_properties_data.to_excel(f"links{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()
#
#





#SOLUCION SIN SQL

# import json
# import xml.etree.ElementTree as ET
# from selenium import webdriver
# from selenium.common import NoSuchElementException, TimeoutException
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
# import re
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Función para crear elementos con formato
# def create_element_with_format(root, tag, text=None, level=0):
#     element = ET.SubElement(root, tag)
#     if text is not None:
#         element.text = f"\n{'    ' * level}{text}\n{'    ' * level}"
#     return element
#
# # Inicializar el navegador
# driver = webdriver.Chrome()
#
# # # Lista de URLs a extraer
# # url_list = ["https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440",
# #             "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/terrassa/51341143",
# #             "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/barcelona/37910931"]
#
# # Lee el archivo Excel y obtiene los URLs de la columna "Referencia"
# df = pd.read_excel('properties_data_195.xlsx', sheet_name='Sheet1', usecols=['link'])
#
# # Convierte los URLs en una lista
# url_list = df['link'].tolist()
#
# # Lista para almacenar los datos extraídos de todas las páginas
# data = []
# counter = 0
# # Recorrer cada URL de la lista
# for url in url_list:
#     # Navegar a la URL
#     driver.get(url)
#     time.sleep(10)
#
#     # Obtener los datos de la página
#     referencia = element = driver.find_elements(By.XPATH, "//div[@class='servicer-data']//b")
#
#     try:
#         referencia_text = referencia[0].text
#     except IndexError:
#         print(f"No se encontró el elemento 'referencia' en la URL: {url}")
#         continue
#
#     title = driver.find_elements(By.XPATH, "//h1[@class='title']")
#
#     try:
#         title_text = title[0].text
#     except IndexError:
#         print(f"No se encontró el elemento 'title' en la URL: {url}")
#         continue
#
#     descripcion = driver.find_elements(By.XPATH, "//div[@class='description__text']")
#
#     try:
#         descripcion_text = descripcion[0].text
#     except IndexError:
#         print(f"No se encontró el elemento 'descripcion' en la URL: {url}")
#         continue
#
#     # ciudad
#     try:
#         ciudad = driver.find_element(By.XPATH, "//*[@id='map-section']/div[1]")
#         ciudad_text = ciudad.text
#         words = ciudad_text.split(',')
#         if len(words) > 2:
#             desired_word_3 = words[2].strip()  # split by space and take the third word (index starts from 0)
#         else:
#             desired_word_3 = 'N/A'
#     except TimeoutException:
#         desired_word_3 = 'N/A'
#
#     provincia = driver.find_elements(By.XPATH, "//a[@class='province']")
#
#     try:
#         provincia_text = provincia[0].text
#     except IndexError:
#         print(f"No se encontró el elemento 'provincia' en la URL: {url}")
#         continue
#
#
#     direccion = driver.find_elements(By.XPATH, "//div[@class='map-section__title']")
#     try:
#         direccion_text = direccion[0].text
#     except IndexError:
#         print(f"No se encontró el elemento 'Direccion' en la URL: {url}")
#         continue
#     # features = driver.find_elements(By.XPATH, "//div[@class='features']")
#     construccion = driver.find_elements(By.XPATH, "//span[@class='feature__value']//b")
#
#     # # Obtener el valor de metros cuadrados
#     # metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#     #
#     # # Obtener el número de habitaciones
#     # habitaciones = re.findall(r'\d+', construccion[1].text)[0]
#     #
#     # # Obtener el número de baños
#     # banos = re.findall(r'\d+', construccion[2].text)[0]
#
#     # Inicializar las variables con valores predeterminados
#     metros_cuadrados = "N/A"
#     habitaciones = "N/A"
#     banos = "N/A"
#
#     if len(construccion) == 3:
#         try:
#             metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#             habitaciones = re.findall(r'\d+', construccion[1].text)[0]
#             banos = re.findall(r'\d+', construccion[2].text)[0]
#         except IndexError:
#             pass  # Manejar el error de índice aquí, si es necesario
#     elif len(construccion) == 2:
#         try:
#             metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#             habitaciones = re.findall(r'\d+', construccion[1].text)[0]
#         except IndexError:
#             pass  # Manejar el error de índice aquí, si es necesario
#     elif len(construccion) == 1:
#         try:
#             metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#         except IndexError:
#             pass  # Manejar el error de índice aquí, si es necesario
#
#     # # Verificar la longitud de la lista 'construccion'
#     # if len(construccion) == 3:
#     #     metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#     #     habitaciones = re.findall(r'\d+', construccion[1].text)[0]
#     #     banos = re.findall(r'\d+', construccion[2].text)[0]
#     # elif len(construccion) == 2:
#     #     metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#     #     habitaciones = re.findall(r'\d+', construccion[1].text)[0]
#     #     # 'banos' mantendrá su valor predeterminado "N/A"
#     # elif len(construccion) == 1:
#     #     metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
#     #     # 'habitaciones' y 'banos' mantendrán sus valores predeterminados "N/A"
#
#     price = driver.find_elements(By.XPATH, "//div[@class='price__current']")
#     main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
#     image_source = main_photo.get_attribute("src")
#
#     # gallery = driver.find_element(By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")
#     # image_elements = gallery.find_elements(By.CSS_SELECTOR, "div.container_img.ng-star-inserted img")
#     # image_sources = [element.get_attribute("src") for element in image_elements]
#
#     image_sources = []
#     elements = driver.find_elements(By.XPATH,"//div[@class='gallery-grid-right size-4 ng-star-inserted']/div[@class='container_img ng-star-inserted'][position() <= 4]/img")
#
#     for element in elements:
#         image_sources.append(element.get_attribute("src"))
#     # try:
#     #     # Esperar hasta que el elemento esté presente en la página
#     #     WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")))
#     #     gallery = driver.find_element(By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")
#     #     image_elements = gallery.find_elements(By.CSS_SELECTOR, "div.container_img.ng-star-inserted img")
#     #     image_sources = [element.get_attribute("src") for element in image_elements]
#     # except NoSuchElementException:
#     #     print(f"No se encontró el elemento 'gallery' en la URL: {url}")
#     #     continue
#
#     elements = referencia + descripcion + direccion + provincia + title + construccion + price + [image_source] + image_sources
#
#     # Convierte la lista de URL en un diccionario y luego en una cadena JSON
#     image_sources_dict = {'image_sources': image_sources}
#     image_sources_json = json.dumps(image_sources_dict)
#     # Almacenar los datos en la lista
#     data.append({
#         "Referencia": referencia_text,
#         "Title": title_text,
#         "Descripcion": descripcion_text,
#         "Direccion": direccion_text,
#         "Provincia": provincia_text,
#         "Ciudad": desired_word_3,
#         "MetrosCuadrados": metros_cuadrados,
#         "Habitaciones": habitaciones,
#         "Baños": banos,
#         "Price": price[0].text,
#         "MainPhoto": image_source,
#         "ImageSources": image_sources
#     })
#
#     # Convertir la lista de datos en un DataFrame
#     df = pd.DataFrame(data, columns=['Referencia', 'Title', 'Descripcion', 'Provincia', 'Direccion', 'MetrosCuadrados', 'Habitaciones', 'Baños', 'Price', 'MainPhoto', 'ImageSources', 'Ciudad'])
#
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
#
# # Cerrar el navegador
# driver.close()


#SOLUCION CON SQL


import mysql.connector
import json
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Función para crear elementos con formato
def create_element_with_format(root, tag, text=None, level=0):
    element = ET.SubElement(root, tag)
    if text is not None:
        element.text = f"\n{'    ' * level}{text}\n{'    ' * level}"
    return element

# Establecer la conexión a la base de datos SQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="20759364",
        database="properties"
    )
    print('Conexión exitosa a la base de datos')
except:
    print('Error al conectarse a la base de datos')

# Crear una tabla en la base de datos
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS aliseda_properties (
        Referencia TEXT,
        Title TEXT,
        Descripcion TEXT,
        Provincia TEXT,
        Direccion TEXT,
        MetrosCuadrados TEXT,
        Habitaciones TEXT,
        Banos TEXT,
        Price INTEGER,
        MainPhoto TEXT,
        ImageSources JSON,
        Ciudad TEXT
    )
    """)
conn.commit()

# Eliminar todos los registros de la tabla
cur.execute("""
    TRUNCATE TABLE aliseda_properties;
""")
conn.commit()

# Inicializar el navegador
driver = webdriver.Chrome()

# Lee el archivo Excel y obtiene los URLs de la columna "Referencia"
df = pd.read_excel('links21.xlsx', sheet_name='Sheet1', usecols=['link'])

# Convierte los URLs en una lista
url_list = df['link'].tolist()

# Lista para almacenar los datos extraídos de todas las páginas
data = []
counter = 0

# Recorrer cada URL de la lista
for url in url_list:
    # Navegar a la URL
    driver.get(url)
    time.sleep(15)

    # Obtener los datos de la página
    referencia = element = driver.find_elements(By.XPATH, "//div[@class='description']//div//div//span")

    try:
        referencia_text = referencia[0].text
        # Dividir la cadena en palabras y unir las palabras que quieras conservar
        referencia_text = ' '.join(referencia_text.split(' ')[1:])
    except IndexError:
        print(f"No se encontró el elemento 'referencia' en la URL: {url}")
        continue

    title = driver.find_elements(By.XPATH, "//h1[@class='title']")

    try:
        title_text = title[0].text
    except IndexError:
        print(f"No se encontró el elemento 'title' en la URL: {url}")
        continue

    descripcion = driver.find_elements(By.XPATH, "//div[@class='description__text']")

    try:
        descripcion_text = descripcion[0].text
    except IndexError:
        print(f"No se encontró el elemento 'descripcion' en la URL: {url}")
        continue

    try:
        ciudad = driver.find_element(By.XPATH, "//*[@id='map-section']/div[1]")
        ciudad_text = ciudad.text
        words = ciudad_text.split(',')
        if len(words) > 2:
            desired_word_3 = words[2].strip()  # split by space and take the third word (index starts from 0)
        else:
            desired_word_3 = 'N/A'
    except TimeoutException:
        desired_word_3 = 'N/A'

    provincia = driver.find_elements(By.XPATH, "//a[@class='province']")

    try:
        provincia_text = provincia[0].text
    except IndexError:
        print(f"No se encontró el elemento 'provincia' en la URL: {url}")
        continue

    direccion = driver.find_elements(By.XPATH, "//div[@class='map-section__title']")
    try:
        direccion_text = direccion[0].text
    except IndexError:
        print(f"No se encontró el elemento 'Direccion' en la URL: {url}")
        continue

    construccion = driver.find_elements(By.XPATH, "//span[@class='feature__value']//b")

    # Inicializar las variables con valores predeterminados
    metros_cuadrados = "N/A"
    habitaciones = "N/A"
    banos = "N/A"

    if len(construccion) == 3:
        try:
            metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
            habitaciones = re.findall(r'\d+', construccion[1].text)[0]
            banos = re.findall(r'\d+', construccion[2].text)[0]
        except IndexError:
            pass  # Manejar el error de índice aquí, si es necesario
    elif len(construccion) == 2:
        try:
            metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
            habitaciones = re.findall(r'\d+', construccion[1].text)[0]
        except IndexError:
            pass  # Manejar el error de índice aquí, si es necesario
    elif len(construccion) == 1:
        try:
            metros_cuadrados = re.findall(r'\d+', construccion[0].text)[0]
        except IndexError:
            pass  # Manejar el error de índice aquí, si es necesario

    # Obtener los datos de la página
    price = driver.find_elements(By.XPATH, "//div[@class='price__current']")

    try:
        price_text = price[0].text
        # Eliminar el símbolo de euro y los puntos
        price_text = price_text.replace('€', '').replace('.', '')
        # Convertir a float
        price_int = int(price_text)
    except IndexError:
        print(f"No se encontró el elemento 'price' en la URL: {url}")
        continue

    main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
    image_source = main_photo.get_attribute("src")

    image_sources = []
    elements = driver.find_elements(By.XPATH,"//div[@class='gallery-grid-right size-4 ng-star-inserted']/div[@class='container_img ng-star-inserted'][position() <= 4]/img")

    for element in elements:
        image_sources.append(element.get_attribute("src"))

    # Convierte la lista de URL en un diccionario y luego en una cadena JSON
    image_sources_dict = {'image_sources': image_sources}
    image_sources_json = json.dumps(image_sources_dict)

    elements = referencia + descripcion + direccion + provincia + title + construccion + price + [image_source] + image_sources

    # Convierte la lista de datos en un DataFrame
    df = pd.DataFrame(
        data=[{
            "Referencia": referencia_text,
            "Title": title_text,
            "Descripcion": descripcion_text,
            "Direccion": direccion_text,
            "Provincia": provincia_text,
            "Ciudad": desired_word_3,
            "MetrosCuadrados": metros_cuadrados,
            "Habitaciones": habitaciones,
            "Banos": banos,
            "Price": price_int,
            "MainPhoto": image_source,
            "ImageSources": image_sources
        }],
        columns=[
            'Referencia',
            'Title',
            'Descripcion',
            'Provincia',
            'Direccion',
            'MetrosCuadrados',
            'Habitaciones',
            'Banos',
            'Price',
            'MainPhoto',
            'ImageSources',
            'Ciudad'
        ]
    )

    # Insertar los datos extraídos en la tabla de la base de datos
    cur.execute("""
        INSERT INTO aliseda_properties (
            Referencia,
            Title,
            Descripcion,
            Provincia,
            Direccion,
            MetrosCuadrados,
            Habitaciones,
            Banos,
            Price,
            MainPhoto,
            ImageSources,
            Ciudad
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        referencia_text,
        title_text,
        descripcion_text,
        provincia_text,
        direccion_text,
        metros_cuadrados,
        habitaciones,
        banos,
        price_int,
        image_source,
        image_sources_json,
        desired_word_3
    ))
    conn.commit()

    # Añade los datos a la lista
    data.append(df)

    counter += 1

    # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
    if counter % 24 == 0:
        file_counter = counter // 24
        df = pd.concat(data)
        df.to_excel(f"aliseda_data_{file_counter}.xlsx", index=False, engine="openpyxl")
        data = []

# Cerrar el navegador
driver.close()

# Cerrar la conexión con la base de datos
cur.close()
conn.close()