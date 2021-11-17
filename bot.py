import telebot
import psycopg2
from telebot import TeleBot
import random
# import schedule
import datetime

conn = psycopg2.connect(database="service",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

token = '2135145672:AAGKUt03amS6MOrfcQpORDFRDWHwz4K073E'

bot: TeleBot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', '/назад.....'])
def start(message):
    print(message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("По дате", "Сегодня")
    keyboard.row("Завтра", "Вчера")
    keyboard.row('/анекдот', '/help')

    bot.send_message(message.chat.id, "Привет, с удовльствием скажу что у тебя по расписанию!", reply_markup=keyboard)
    print(datetime.datetime.now().time())


@bot.message_handler(commands=['анекдот'])
def start(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.row('ахАХАХахаХАХ11))0)')
    keyboard1.row('/назад.....')
    a = random.randint(1, 10062)
    cursor.execute("SELECT text FROM anek WHERE id = '{0}'".format(a))
    records = list(cursor.fetchall())
    b = str(records)
    a = '\\n'
    b = b.replace(a, ' ')
    b = b.replace('\\', '\n ')
    b = b.replace('[(\'', ' ')
    b = b.replace('\',)]', ' ')
    bot.send_message(message.chat.id, b, reply_markup=keyboard1)


''' 
тестовая функция
def budilnik():
    print("Спокойной ночи")

    schedule.every(10).minutes.do(budilnik)
    schedule.every().hour.do(budilnik)
    schedule.every().monday.at("9:30").do(budilnik)
    schedule.every().tuesday.at('9:30').do(budilnik)
    schedule.every().wednesday.at("13:10").do(budilnik)
    schedule.every().tuesday.at("21:30").do(budilnik)
'''


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
            q = "9:30-11:05 - нет.\n"
        else:
            q = ('9:30-11:05 - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "11:20-12:55 - нет.\n"
        else:
            w = ('11:20-12:55 - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "13:10-14:45 - нет.\n"
        else:
            e = ('13:10-14:45 - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "15:25-17:00 - нет.\n"
        else:
            r = ('15:25-17:00 - ' + str(r) + '.\n')
        t = str('Расписание на сегодня: \n' + q + w + e + r)
        bot.send_message(message.chat.id, t)

    if message.text.lower() == 'завтра':
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = (date(now()) + integer '1');")
        records = list(cursor.fetchall())
        print(records)
        q = records[0][1]
        w = records[1][1]
        e = records[2][1]
        r = records[3][1]
        if q == 'Нет':
            q = "9:30-11:05 - нет.\n"
        else:
            q = ('9:30-11:05 - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "11:20-12:55 - нет.\n"
        else:
            w = ('11:20-12:55 - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "13:10-14:45 - нет.\n"
        else:
            e = ('13:10-14:45 - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "15:25-17:00 - нет.\n"
        else:
            r = ('15:25-17:00 - ' + str(r) + '.\n')
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
            q = "9:30-11:05 - нет.\n"
        else:
            q = ('9:30-11:05 - ' + str(q) + '.\n')
        if w == 'Нет':
            w = "11:20-12:55 - нет.\n"
        else:
            w = ('11:20-12:55 - ' + str(w) + '.\n')
        if e == 'Нет':
            e = "13:10-14:45 - нет.\n"
        else:
            e = ('13:10-14:45 - ' + str(e) + '.\n')
        if r == 'Нет':
            r = "15:25-17:00 - нет.\n"
        else:
            r = ('15:25-17:00 - ' + str(r) + '.\n')
        t = str('Вчерашнее расписание: \n' + q + w + e + r)
        bot.send_message(message.chat.id, t)

    if message.text.lower() == 'по дате':
        bot.send_message(message.chat.id, 'Введите число в формате ГГГГ-ММ-ДД \n Например: 2021-01-01')

    if message.text.__contains__('2021'):
        date1 = str(message.text)
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = '{0}'".format(date1))
        records = list(cursor.fetchall())
        if not records:
            bot.send_message(message.chat.id, 'Пока расписания на это число нет, введите другую дату.')
        else:
            q = records[0][1]
            w = records[1][1]
            e = records[2][1]
            r = records[3][1]
            if q == 'Нет':
                q = "9:30-11:05 - нет.\n"
            else:
                q = ('9:30-11:05 - ' + str(q) + '.\n')
            if w == 'Нет':
                w = "11:20-12:55 - нет.\n"
            else:
                w = ('11:20-12:55 - ' + str(w) + '.\n')
            if e == 'Нет':
                e = "13:10-14:45 - нет.\n"
            else:
                e = ('13:10-14:45 - ' + str(e) + '.\n')
            if r == 'Нет':
                r = "15:25-17:00 - нет.\n"
            else:
                r = ('15:25-17:00 - ' + str(r) + '.\n')
            t = str('Расписание на ' + date1 + ':\n' + q + w + e + r)
            bot.send_message(message.chat.id, t)

    if message.text.lower() == 'ахахахахахах11))0)':
        a = random.randint(1, 10062)
        cursor.execute("SELECT text FROM anek WHERE id = '{0}'".format(a))
        records = list(cursor.fetchall())
        b = str(records)
        a = '\\n'
        b = b.replace(a, ' ')
        b = b.replace('\\', '\n ')
        b = b.replace('[(\'', ' ')
        b = b.replace('\',)]', ' ')
        bot.send_message(message.chat.id, b)

    if message.text.lower() == '/агила':
        bot.send_message(message.chat.id, 'https://vk.com/doc257116315_619803'
                                          '977?hash=b5f4c0d3'
                                          '7ede824274&dl=1ce00b0970a769ae03')
    if message.text.lower() == '/математика':
        bot.send_message(message.chat.id, 'https://vk.com/doc494484715_469501555?ha'
                                          'sh=a49d028229b4105392&dl=d4cd6a1e1fa8faee13')
    if message.text.lower() == '/английский язык':
        bot.send_message(message.chat.id, 'https://vk.com/away.php?to=https%3A%2F'
                                          '%2Fwww.book.ru%2Fbook%2F926036&cc_key=')
    if message.text.lower() == '/help':
        bot.send_message(message.chat.id, '/start \n /анекдот - Отправляет рандомный анекдот из огромной базы. '
                                          '\n /агила - Учебник по алгебре.\n /математика - Берман сборник.'
                                          ' \n  /английский язык - учебник по английскому.'
                                          ' \n Команды будут добавляться :)')


bot.infinity_polling()
