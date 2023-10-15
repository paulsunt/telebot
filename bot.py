import telebot
import sqlite3
from telebot import types
import re

# Получить токен бота у @BotFather
TOKEN = "6111746050:AAFjtnecLVu_Z1CcEOhHb3LHIv1Csu568Hw"

# Создать объект бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    # Отправить сообщение
    bot.send_message(message.chat.id, "Привет, тыкай!")
    # Добавить клавиатуру
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    keyboard.add(types.KeyboardButton("Политика"))
    keyboard.add(types.KeyboardButton("Спорт"))
    # Отправить клавиатуру
    bot.send_message(message.chat.id, "Выбери категорию:", reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "Политика":
        # Предложить пользователю ввести дату
        bot.send_message(message.chat.id, "Введите дату в формате ДД.ММ.ГГГГ:")

        # Установить обработчик на следующее сообщение пользователя
        bot.register_next_step_handler(message, process_date_input)
    else:
        bot.send_message(message.chat.id, "дохуя спортсмен?")

# Обработчик ввода даты
def process_date_input(message):
    date_input = message.text

    # Проверить, соответствует ли введенная дата формату ДД.ММ.ГГГГ
    if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', date_input):
        bot.send_message(message.chat.id, "Пожалуйста, используйте формат ДД.ММ.ГГГГ.")
        return

    conn = sqlite3.connect("scraper.db")
    cursor = conn.cursor()

    # Используйте параметризованный запрос для предотвращения SQL-инъекций
    cursor.execute("SELECT date, url FROM scraped_links WHERE date = ?", (date_input,))
    links = cursor.fetchall()

    conn.close()

    if links:
        response = "Ссылки с датой {}:\n".format(date_input)
        links_to_send = links[:20]  # Ограничим вывод 

        for link in links_to_send:
            response += link[0] + " " + link[1] + "\n"

        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Ссылок на указанную дату не найдено.")


# Запустить бота
bot.polling()