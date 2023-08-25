import sqlite3
import re
from selenium import webdriver
import time

from database import create_table, insert_link

# Инициализация Chrome WebDriver
driver = webdriver.Chrome()

# Откройте нужный URL
url = "https://www.mil.gov.ua/news/"
driver.get(url)

# Подождите, чтобы страница полностью загрузилась
time.sleep(2)

# Находим блок с id="aticle-content"
article_content = driver.find_element("id", "aticle-content")

# Находим все вложенные ul элементы
ul_elements = article_content.find_elements("css selector", "ul ul")

# Создаем список для сохранения данных

# Проходимся по каждому ul элементу
for ul_element in ul_elements:
    # Находим все элементы li внутри ul элемента
    link_elements = ul_element.find_elements("css selector", "li")

    # Извлекаем и добавляем данные в список
    for link_element in link_elements:
        try:
            link = link_element.find_element("css selector", "a").get_attribute("href")
            # Достаем текст, который находится в блоках li
            link_time = link_element.text

            # Извлекаем из текста в блоке li время с помощью re
            time_match = re.search(r'(\d{2}:\d{2})', link_time)
            formatted_time = time_match.group(1)

            # Извлекаем дату из самой ссылки, которую мы нашли по атрибуту href, используя re
            date = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', link).group(3, 2, 1)
            formatted_date = "{0}.{1}.{2}".format(*date)

            # Добавляем элемент(в виде словаря) в пустой список
            insert_link(formatted_date, formatted_time, link)
            print(f"Добавлены данные: дата={formatted_date}, время={formatted_time}, ссылка={link}")
        except:
            pass

# Закрываем браузер после использования
driver.quit()