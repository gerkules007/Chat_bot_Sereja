from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from comands import *

updater = Updater(i_d.token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
# updater.dispatcher.add_handler(CommandHandler('load_man', load_ai_bot_chat))
# добавить команду help, которая появляется сразу после старта
# добавить команду для добавления ошибок и разговора
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))

updater.start_polling()
print("RUN")
updater.idle()