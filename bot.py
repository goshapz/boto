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
    keyboard.row("По дате", "Сегодня")
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
        if q == 'Нет':
            q = "1 - нет.\n"
        else:
            q = ('1 - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "2 - нет.\n"
        else:
            w = ('2 - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "3 - нет.\n"
        else:
            e = ('3 - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "4 - нет.\n"
        else:
            r = ('4 - ' + str(r) + '.\n')
        t = str('Расписание на сегодня: \n' + q + w + e + r)
        bot.send_message(message.chat.id, t)

    if message.text.lower() == 'завтра':
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = (date(now()) + integer '1');")
        records = list(cursor.fetchall())
        q = records[0][1]
        w = records[1][1]
        e = records[2][1]
        r = records[3][1]
        if q == 'Нет':
            q = "1 - нет.\n"
        else:
            q = ('1 - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "2 - нет.\n"
        else:
            w = ('2 - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "3 - нет.\n"
        else:
            e = ('3 - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "4 - нет.\n"
        else:
            r = ('4 - ' + str(r) + '.\n')
        t = str('Расписание на завтра: \n' + q + w + e + r)
        bot.send_message(message.chat.id, t)
        print(message.text)

    if message.text.lower() == 'вчера':
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = (date(now()) - integer '1');")
        records = list(cursor.fetchall())
        q = records[0][1]
        w = records[1][1]
        e = records[2][1]
        r = records[3][1]
        if q == 'Нет':
            q = "1 - нет.\n"
        else:
            q = ('1 - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "2 - нет.\n"
        else:
            w = ('2 - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "3 - нет.\n"
        else:
            e = ('3 - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "4 - нет.\n"
        else:
            r = ('4 - ' + str(r) + '.\n')
        t = str('Вчерашнее расписание: \n' + q + w + e + r)
        bot.send_message(message.chat.id, t)



    if message.text.lower() == 'по дате':
        bot.send_message(message.chat.id, 'Введите число в формате ГГГГ-ММ-ДД \n Например: 2021-01-01')

    if message.text.__contains__('2021'):
        date1 = str(message.text)
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = '{0}'".format(date1))
        records = list(cursor.fetchall())
        if records ==[]:
            bot.send_message(message.chat.id, 'Пока расписания на это число нет, введите другую дату.')
        else:
            q = records[0][1]
            w = records[1][1]
            e = records[2][1]
            r = records[3][1]
            if q == 'Нет':
                q = "1 - нет.\n"
            else:
                q = ('1 - ' + str(q) + '.\n')
            if w == 'Нет':
                w = "2 - нет.\n"
            else:
                w = ('2 - ' + str(w) + '.\n')
            if e == 'Нет':
                e = "3 - нет.\n"
            else:
                e = ('3 - ' + str(e) + '.\n')
            if r == 'Нет':
                r = "4 - нет.\n"
            else:
                r = ('4 - ' + str(r) + '.\n')
            t = str('Расписание на ' + date1 + ':\n' + q + w + e + r)
            bot.send_message(message.chat.id, t)







bot.infinity_polling()
