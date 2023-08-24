import sqlite3


def create_table():
    # Подключение к базе данных (создаст файл "scraper.db" в папке проекта, если его нет)
    conn = sqlite3.connect('scraper.db')
    cursor = conn.cursor()

    # Создание таблицы, если она еще не существует
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS scraped_links (
            id INTEGER PRIMARY KEY,
            url TEXT
        )
    '''
    cursor.execute(create_table_query)

    # Закрытие курсора и соединения
    cursor.close()
    conn.close()

def insert_link(url):
    # Подключение к базе данных
    conn = sqlite3.connect('scraper.db')
    cursor = conn.cursor()

    # Вставка спаршенных ссылок в базу данных
    insert_query = '''
        INSERT INTO scraped_links (url)
        VALUES (?)
    '''
    cursor.execute(insert_query, (url,))
    conn.commit()

    # Закрытие курсора и соединения
    cursor.close()
    conn.close()
