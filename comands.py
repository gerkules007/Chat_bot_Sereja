from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import random 
import json

class AI_BOT:
    key_talk = {
        ("привет", "здарова", "здарово", "прив"): "hello",
        ("зачем ты здесь"): "why",
        ("хорошо", "ок"): "OK"
    }
    answer = {
        "hello": ["привет, человек", "привет", "здаров"],
        "why": ["чтобы радовать тебя", "а ты зачем здесь?"],
        "OK": ["к", ""]
    }
    not_answer = [
        "Не понимаю", 
        "Повтори еще раз", 
        "Возможно тебе стоит подучить русский язык", 
        "Спроси что-то попроще"
    ]

def rand_item(rand_list):
    return random.randint(0, len(rand_list)-1)

def answer(update: Update, context: CallbackContext):
    user_message: str = update.message.text.lower()
    ab = AI_BOT()
    user_key = user_message

    try:
        for key in ab.key_talk.items():
            
            if user_key in key[0]:
                update.message.reply_text( \
                    ab.answer[key[1]]
                        [rand_item(ab.answer)])
                return
        else:
            update.message.reply_text( \
                ab.not_answer[ \
                    rand_item(ab.not_answer)])
    except Exception:
        return
