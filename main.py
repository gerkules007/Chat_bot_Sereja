from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from comands import answer

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

with open("token.txt", "r") as token:
    updater = Updater(token.read())

updater.dispatcher.add_handler(CommandHandler('hello', hello))
# добавить команду help, которая появляется сразу после старта
# добавить команду для добавления ошибок и разговора
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))

updater.start_polling()
updater.idle()