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


@bot.message_handler(commands=['start', 'назад.....'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("По дате", "Сегодня")
    keyboard.row("Завтра", "Вчера")
    keyboard.row('/anekdot', '/help')
    bot.send_message(message.chat.id, 'Привет!\nИспользуй /help, '
                                      'чтобы узнать список доступных команд! \nТак же можешь узнать рас'
                                      'писание на интересующий день.', reply_markup=keyboard)
    print(datetime.datetime.now().time())


@bot.message_handler(commands=['anekdot'])
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
    print(datetime.datetime.now().time())
    userf = message.from_user.first_name
    users = message.from_user.last_name
    username = (userf + ' ' + users)
    print(username + ' ' + 'читает анекдот')
    cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
    records = list(cursor.fetchall())
    if not records:
        cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                       (str(message.chat.id), str(username)))
        conn.commit()


# тестовая функция
@bot.message_handler(commands=['timetable'])
def start(message):
    # cursor.execute("SELECT * from category WHERE id_category = 10;")
    # records = list(cursor.fetchall())
    # a = records[0][2]
    bot.send_photo(message.chat.id, open('/home/georgy/Документы/1.png', 'rb'))
    bot.send_photo(message.chat.id, open('/home/georgy/Документы/2.png', 'rb'))
    bot.send_photo(message.chat.id, open('/home/georgy/Документы/3.png', 'rb'))
    bot.send_photo(message.chat.id, open('/home/georgy/Документы/4.png', 'rb'))
    bot.send_photo(message.chat.id, open('/home/georgy/Документы/5.png', 'rb'))
    print(datetime.datetime.now().time())
    userf = message.from_user.first_name
    users = message.from_user.last_name
    username = (userf + ' ' + users)
    print(username + ' ' + 'смотрит расписание')
    cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
    records = list(cursor.fetchall())
    if not records:
        cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                       (str(message.chat.id), str(username)))
        conn.commit()


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
        print(datetime.datetime.now().time())
        userf = message.from_user.first_name
        users = message.from_user.last_name
        username = (userf + ' ' + users)
        print(username + ' ' + 'расписание на сегодня')
        cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                           (str(message.chat.id), str(username)))
            conn.commit()

    if message.text.lower() == 'завтра':
        cursor.execute("SELECT num, lesson FROM Timetable WHERE date = (date(now()) + integer '1');")
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
        t = str('Расписание на завтра: \n' + q + w + e + r)
        bot.send_message(message.chat.id, t)
        print(datetime.datetime.now().time())
        userf = message.from_user.first_name
        users = message.from_user.last_name
        username = (userf + ' ' + users)
        print(username + ' ' + 'расписание на завтра')
        cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                           (str(message.chat.id), str(username)))
            conn.commit()

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
        print(datetime.datetime.now().time())
        userf = message.from_user.first_name
        users = message.from_user.last_name
        username = (userf + ' ' + users)
        print(username + ' ' + 'расписание на вчера')
        cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                           (str(message.chat.id), str(username)))
            conn.commit()

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
        print(datetime.datetime.now().time())
        userf = message.from_user.first_name
        users = message.from_user.last_name
        username = (userf + ' ' + users)
        print(username + ' ' + 'расписание по дате')
        cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                           (str(message.chat.id), str(username)))
            conn.commit()

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
        print(datetime.datetime.now().time())
        userf = message.from_user.first_name
        users = message.from_user.last_name
        username = (userf + ' ' + users)
        print(username + ' ' + 'читает анекдот')
        cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                           (str(message.chat.id), str(username)))
            conn.commit()

    if message.text.lower() == '/agila':
        bot.send_message(message.chat.id, 'https://vk.com/doc257116315_619803'
                                          '977?hash=b5f4c0d3'
                                          '7ede824274&dl=1ce00b0970a769ae03')
    if message.text.lower() == '/maths':
        bot.send_message(message.chat.id, 'https://vk.com/doc494484715_469501555?ha'
                                          'sh=a49d028229b4105392&dl=d4cd6a1e1fa8faee13')
    if message.text.lower() == '/english':
        bot.send_message(message.chat.id, 'https://vk.com/away.php?to=https%3A%2F'
                                          '%2Fwww.book.ru%2Fbook%2F926036&cc_key=')
    if message.text.lower() == '/help':
        bot.send_message(message.chat.id, '/start \n  /anekdot - Отправляет рандомный анекдот из огромной базы. '
                                          '\n  /agila - Учебник по алгебре.\n  /maths - Берман сборник.'
                                          ' \n   /english - учебник по английскому.'
                                          '\n  /timetable - расписание с сайта МТУСИ.'
                                          ' \n Команды будут добавляться :)')
        print(datetime.datetime.now().time())
        userf = message.from_user.first_name
        users = message.from_user.last_name
        username = (userf + ' ' + users)
        print(username + ' ' + 'смотрит список команд')
        cursor.execute("SELECT * from telusers WHERE chat_id =%s", (str(message.chat.id),))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('insert into telusers(chat_id, username) VALUES (%s, %s);',
                           (str(message.chat.id), str(username)))
            conn.commit()


bot.infinity_polling()
