import telebot
from telebot import types

# Получить токен бота у @BotFather
TOKEN = "6111746050:AAFjtnecLVu_Z1CcEOhHb3LHIv1Csu568Hw"

# Создать объект бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    # Отправить сообщение
    bot.send_message(message.chat.id, "Привет! Хочешь узнать новости о политике или спорте?")
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
        bot.send_message(message.chat.id, "На сегодня новостей нет")
    elif message.text == "Спорт":
        bot.send_message(message.chat.id, "На сегодня новостей нет")

# Запустить бота
bot.polling()
