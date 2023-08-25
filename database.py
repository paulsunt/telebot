import sqlite3

def create_table():
    # Подключение к базе данных (создаст файл "scraper.db" в папке проекта, если его нет)
    conn = sqlite3.connect('scraper.db')
    cursor = conn.cursor()

    # Создание таблицы, если она еще не существует
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS scraped_links (
            id INTEGER PRIMARY KEY,
            date TEXT,
            time TEXT,
            url TEXT
        )
    '''
    cursor.execute(create_table_query)

    # Закрытие курсора и соединения
    cursor.close()
    conn.close()

def insert_link(date, time, url):
    print(f"Inserting link: date={date}, time={time}, url={url}")  # Отладочное сообщение

    # Подключение к базе данных
    conn = sqlite3.connect('scraper.db')
    cursor = conn.cursor()

    # Вставка спаршенных ссылок в базу данных
    insert_query = '''
        INSERT INTO scraped_links (date, time, url)  -- Заменено "data" на "date"
        VALUES (?, ?, ?)
    '''
    cursor.execute(insert_query, (date, time, url))
    conn.commit()

    # Закрытие курсора и соединения
    cursor.close()
    conn.close()
