from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот!")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(token="6111746050:AAFjtnecLVu_Z1CcEOhHb3LHIv1Csu568Hw", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
