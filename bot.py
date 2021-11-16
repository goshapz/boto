import telebot
import psycopg2
from telebot import TeleBot

conn = psycopg2.connect(database="service",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


token = '2135145672:AAGKUt03amS6MOrfcQpORDFRDWHwz4K073E'

bot: TeleBot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Сейчас", "Сегодня")
    keyboard.row("Завтра", "Вчера")
    bot.send_message(message.chat.id, "Привет, с удовльствием скажу что у тебя по расписанию!", reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'я умею....всё')



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'сегодня':
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = date(now());")
        records = list(cursor.fetchall())
        q = records[0][1]
        w = records[1][1]
        e = records[2][1]
        r = records[3][1]
        print(q)
        if q == 'Нет':
            q = "Первой пары у тебя нет!\n"
        else:
            q = ('Первая пара у тебя - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "Второй пары у тебя нет!\n"
        else:
            w = ('Вторая пара у тебя - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "Третьей пары у тебя нет!\n"
        else:
            e = ('Третья пара у тебя - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "Четвертой пары у тебя нет!\n"
        else:
            r = ('Четвертая у тебя - ' + str(r) + '.\n')
        t = str(q + w + e + r + 'Изи пизи!!')
        bot.send_message(message.chat.id, t)


       # bot.send_message(message.chat.id, records)
        print(records)
    elif message.text.lower() == 'не хочу' or message.text.lower() == 'нет':
        bot.send_message(message.chat.id, ":(")
    else:
        bot.send_message(message.chat.id, "Не понял")






bot.infinity_polling()
