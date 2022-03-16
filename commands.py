from telegram import Update
from telegram.ext import CallbackContext
from io_bot import AI_BOT, InputData
import random

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def rand_item(rand_list):
    return random.randint(0, len(rand_list)-1)

def answer(update: Update, context: CallbackContext):
    user_message: str = update.message.text
    user_key = user_message.lower()
    global ab

    try:
        for key in ab.key_talk.items():
            
            if user_key in key[1]:
                update.message.reply_text( \
                    ab.answer[key[0]]
                        [rand_item(ab.answer)])
                return
        else:
            update.message.reply_text( \
                ab.not_answer[ \
                    rand_item(ab.not_answer)])
    except Exception:
        print(Exception)
        return

path_token = 'token.txt'
path_ai_bot = 'talk_library.json'

i_d = InputData()
i_d.get_token(path_token)
i_d.get_ai_bot_json(path_ai_bot)
ab = AI_BOT(i_d.json_dict)