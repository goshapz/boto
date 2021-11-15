import telebot
from telebot import TeleBot

token = '2135145672:AAGKUt03amS6MOrfcQpORDFRDWHwz4K073E'

bot: TeleBot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    #starter = telebot.types.ReplyKeyboardMarkup()
    keyboard = telebot.types.ReplyKeyboardMarkup()
    #starter.row('/start')
    #bot.send_message(message.chat.id,' ', reply_markup=starter)
    keyboard.row("Хочу", "Не хочу")
    keyboard.row("Да", "Нет")
    bot.send_message(message.chat.id, "Hello! Хочешь узнать что нибудь?", reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'я умею....всё')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'хочу'or message.text.lower() == 'да':
        bot.send_message(message.chat.id, "Пиши тогда сюда: vk.com/gosha1253")
    elif message.text.lower() == 'не хочу' or message.text.lower() == 'нет':
        bot.send_message(message.chat.id, ":(")
    else:
        bot.send_message(message.chat.id, "Не понял")






bot.infinity_polling()
