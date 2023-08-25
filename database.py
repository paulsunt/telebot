import sqlite3

# Создать таблицу в базе данных, если её нет
def create_table():
    conn = sqlite3.connect("scraper.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scraped_links (id INTEGER PRIMARY KEY, date TEXT, url TEXT)")
    conn.commit()
    cursor.close()
    conn.close()

# Вставить ИД, дату и ссылку в файл БД
def insert_link(date, url):
    conn = sqlite3.connect("scraper.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scraped_links (date, url) VALUES (?, ?)", (date, url))
    conn.commit()
    cursor.close()
    conn.close()