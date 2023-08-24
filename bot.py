import telebot

# Получить токен бота у @BotFather

TOKEN = "6111746050:AAFjtnecLVu_Z1CcEOhHb3LHIv1Csu568Hw"

# Создать объект бота

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start

@bot.message_handler(commands=["start"])
def start(message):
    # Отправить сообщение
    bot.send_message(message.chat.id, "Привет, я бот!")

# Запустить бота

bot.polling()