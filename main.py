from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el web driver
driver = webdriver.Chrome()
driver.implicitly_wait(30)  # Aumenta el tiempo de espera implícito a 30 segundos
driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic")

# Aceptar las cookies
cookies_accept_btn = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
)
cookies_accept_btn.click()

# Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
counter = 0
href_set = set()

# Crea un DataFrame vacío fuera del bucle
all_properties_data = pd.DataFrame(columns=["link"])

while True:
    try:
        ver_mas_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "nextPage"))
        )
        ver_mas_btn.click()
        time.sleep(18)
        counter += 12
    except:
        break

    # Encuentra los elementos del título y del precio
    urls = driver.find_elements(By.XPATH,"//*[@id='switchMap']/app-property-card/div/div/div/app-card-gallery/div/swiper/div[4]/div[2]/div/a")

    for url in urls:
        href = url.get_attribute("href")
        href_set.add(href)

    # Crea una lista para almacenar los datos de las propiedades
    properties_data = [{"link": href} for href in href_set]

    # Añade las nuevas propiedades al DataFrame existente
    all_properties_data = all_properties_data._append(properties_data, ignore_index=True)

    # Elimina las filas duplicadas
    all_properties_data = all_properties_data.drop_duplicates(subset=["link"], keep="first")

    # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
    if counter % 24 == 0:
        file_counter = counter // 24

        all_properties_data.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")

# Cierra el driver de Selenium
driver.quit()




# import json
# import xml.etree.ElementTree as ET
# from selenium import webdriver
# from selenium.common import NoSuchElementException
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
# df = pd.read_excel('properties_data_245.xlsx', sheet_name='Sheet1', usecols=['link'])
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
#
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
#         "MetrosCuadrados": metros_cuadrados,
#         "Habitaciones": habitaciones,
#         "Baños": banos,
#         "Price": price[0].text,
#         "MainPhoto": image_source,
#         "ImageSources": image_sources
#     })
#
#     # Convertir la lista de datos en un DataFrame
#     df = pd.DataFrame(data, columns=['Referencia', 'Title', 'Descripcion', 'Provincia', 'Direccion', 'MetrosCuadrados', 'Habitaciones', 'Baños', 'Price', 'MainPhoto', 'ImageSources'])
#
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Crear el elemento raíz del archivo XML
# root = ET.Element("Data")
#
# # Recorrer los datos y crear un elemento para cada uno
# for d in data:
#     item = create_element_with_format(root, "Item", level=1)
#     for key, value in d.items():
#         if key == "MainPhoto":
#             # Crear un subelemento para la imagen principal
#             image_element = create_element_with_format(item, "MainPhoto", value, level=2)
#         elif key == "ImageSources":
#             # Crear un subelemento para cada imagen adicional
#             for index, image_source in enumerate(value):
#                 image_element = create_element_with_format(item, f"Picture{index+1}", image_source, level=2)
#         else:
#             create_element_with_format(item, key, value, level=2)
#
# # Crear el árbol XML y guardar el archivo
# tree = ET.ElementTree(root)
# tree.write("data.xml", encoding="utf-8", xml_declaration=True)
#
# # Cerrar el navegador
# driver.close()

