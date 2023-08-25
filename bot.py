import telebot
import sqlite3
from telebot import types

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
        conn = sqlite3.connect("scraper.db")
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM scraped_links LIMIT 5")
        links = cursor.fetchall()
        conn.close()

        if links:
            response = "Вот первые пять ссылок:\n"
            for link in links:
                response += link[0] + "\n"
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "На сегодня новостей нет")
    else:
        bot.send_message(message.chat.id, "дохуя спортсмен?")

# Запустить бота
bot.polling()
