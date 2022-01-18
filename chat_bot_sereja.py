import telebot
import random

token = ""

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку по программе
/add - добавить задачу в список ( газвание задачи запрашиваем у пользователя)
/show - напечатать все добавленые задачи
/random - добавляет случайную задачу на дату"""

RANDOM_TASKS = ["Читать книжечку", "Посмотреть Youtubeчик", "Заварить кофеечек"]

tasks = {}

def add_todo (array, date, task):
  if date in array:
    array[date].append(task)
  else:
    array[date] = [task]

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    splitted_text = message.text.split(maxsplit=2)
    add_todo(tasks, splitted_text[1].lower(), splitted_text[2])
    done_add = "Задача" + splitted_text[2] + "добавлена на дату" + splitted_text[1]
    bot.send_message(message.chat.id, done_add)

@bot.message_handler(commands=["random"])
def random_add(message):
    random_task = random.choice(RANDOM_TASKS)
    add_todo(tasks, "Сегодня", random_task)
    done_add = "Задача " + random_task + " добавлена на дату " + "Сегодня"
    bot.send_message(message.chat.id, done_add)

@bot.message_handler(commands=["show", "print"])
def show(message):
    splitted_text = message.text.split()
    date = splitted_text[1].lower()
    show = ""
    if date in tasks:
        show = date.upper() + "\n"
        for task in tasks[date]:
            show = show + "[]" + task + "\n"
    else:
        show = "Задач на дату нет"
    bot.send_message(message.chat.id, show)

# @bot.message_handler(content_types=["text"]) # улавливание сообщений с форматом text
# def echo(message): # операции ответа на сообщения
#     bot.send_message(message.chat.id, message.text)

# Постоянное обращение к серверам телеграмма
# none_stop - она не перестает работать, даже если получит ошибку
bot.polling(none_stop=True)