import telebot
import config
from telebot import types  # для указания типов

# /start

# инициировали бота
bot = telebot.TeleBot(config.bot_token)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("👋 Поздороваться")
#     btn2 = types.KeyboardButton("❓ Задать вопрос")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id,
#                      text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
#                          message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if (message.text == "👋 Поздороваться"):
#         bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
#     elif (message.text == "❓ Задать вопрос"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Как меня зовут?")
#         btn2 = types.KeyboardButton("Что я могу?")
#         back = types.KeyboardButton("Вернуться в главное меню")
#         markup.add(btn1, btn2, back)
#         bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
#     elif (message.text == "Как меня зовут?"):
#         bot.send_message(message.chat.id, "У меня нет имени..")
#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")
#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("❓ Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую команду я не запрограммировал..")


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Как Вас зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Не понял Вас, попробуйте /start")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Как твоя фамилия")
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько лет?")
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    while age == 0:  # уточняем менялся ли возвраст
        try:
            age = int(message.text)
        except ValueError:
            bot.send_message(message.from_user.id, "Введите цифры")
            age = 1
            break
    quest = f'Тебе {age} лет, и ты {name} {surname}?'
    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardMarkup(text='Да', callback_data='yes')
    keyboard.add(yes)
    no = types.InlineKeyboardMarkup(text='Да', callback_data='no')
    keyboard.add(no)
    bot.send_message(message.from_user.id, text=quest, reply_markup=keyboard)

@bot.channel_post_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Приятно познакомиться')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Начнем заново... Как тебя зовут?')
        bot.register_next_step_handler(call.message, get_name)


# запустили бота
bot.polling(none_stop=True)