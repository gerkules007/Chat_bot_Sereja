from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import random 

class AI_BOT:
    answer = {
    "привет": "Привет, человек",
    "зачем ты здесь": "чтобы радовать тебя",
    "ок": ""
    }
    talk = [
        "Не понимаю", "Повтори еще раз", "Возможно тебе стоит подучить русский язык"
    ]


def answer(update: Update, context: CallbackContext):
    user_message: str = update.message.text.lower()
    answer_bot = AI_BOT()
    user_key = user_message

    try:
        if user_key in answer_bot.answer.keys():
            update.message.reply_text(answer_bot.answer[user_key])
        else:
            update.message.reply_text( \
                answer_bot.talk[ \
                    random.randint(0, len(answer_bot.talk)-1)])
    except Exception:
        return
