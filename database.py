import sqlite3

# Создать таблицу в базе данных, если её нет
def create_table():
    conn = sqlite3.connect("scraper.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scraped_links (id INTEGER PRIMARY KEY, url TEXT)")
    conn.commit()
    cursor.close()
    conn.close()

# Вставить ссылку в таблицу базы данных
def insert_link(url):
    conn = sqlite3.connect("scraper.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scraped_links (url) VALUES (?)", (url,))
    conn.commit()
    cursor.close()
    conn.close()