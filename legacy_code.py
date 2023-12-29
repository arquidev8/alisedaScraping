
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




from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page = 0
# Configurar el web driver
driver = webdriver.Chrome()
driver.implicitly_wait(30)  # Aumenta el tiempo de espera implícito a 30 segundos
driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?page=" + str(page))

# Aceptar las cookies
cookies_accept_btn = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
)
cookies_accept_btn.click()

# Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
counter = 0

href_set = set()

# ... (Importaciones y configuración del webdriver)

# Crea un DataFrame vacío fuera del bucle
all_properties_data = pd.DataFrame(columns=["link"])

# Itera a través de todas las páginas
for page in range(500):
    driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?page=" + str(page))

    # ... (Aceptar las cookies y esperar a que la página cargue)

    # Encuentra los elementos del título y del precio
    urls = driver.find_elements(By.XPATH,"//*[@id='switchMap']/app-property-card/div/div/div/div[2]/a/a")

    for url in urls:
        href = url.get_attribute("href")
        href_set.add(href)

    # Crea una lista para almacenar los datos de las propiedades
    properties_data = [{"link": href} for href in href_set]

    # Añade las nuevas propiedades al DataFrame existente
    all_properties_data = all_properties_data._append(properties_data, ignore_index=True)

    # Elimina las filas duplicadas
    all_properties_data = all_properties_data.drop_duplicates(subset=["link"], keep="first")

    # Vacía el conjunto href_set para la siguiente página
    href_set.clear()

    # Guarda el DataFrame en un archivo de Excel cada 20 propiedades
    if (page + 1) % 20 == 0:
        file_counter = (page + 1) // 20
        all_properties_data.to_excel(f"links{file_counter}.xlsx", index=False, engine="openpyxl")

# Cierra el driver de Selenium
driver.quit()
