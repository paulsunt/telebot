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
<<<<<<< HEAD
    bot.send_message(message.chat.id, "Привет, я бот! Выберите, что вас интересует:")
    # Отправить кнопки
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton(text="Политика", color="blue"))
    keyboard.add(telebot.types.KeyboardButton(text="Спорт", color="green"))

    # Отправить клавиатуру
    bot.send_message(message.chat.id, "", reply_markup=keyboard)
=======
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
>>>>>>> 1f56d94877bedffb345b8d9b2b153267666ec532

# Запустить бота
bot.polling()
