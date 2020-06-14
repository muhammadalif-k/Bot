import telebot
import mysql.connector

import mytoken

from datetime import date
from datetime import datetime

TOKEN = mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
database = mysql.connector.connect(host='localhost', user='root', database='db_belajarbot')
sql = database.cursor()
from telebot import apihelper

time = datetime.now()


class MyBot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        photo = open('img/5.jpg', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        text = mytoken.Reply + "\n-- BY : @MuhammadAlif - XI RPL 2 -- " + "\n " \
        "🏳 Pilih /help Untuk Mendapatkan Bantuan Tentang Apa Saja Yang Bisa Kamu Lakukan" + "\n " \
                                    "🕕 Today's Date " + str(time)
        myBot.reply_to(message, text)

    @myBot.message_handler(commands=['help'])
    def bantuan(message):
        help = mytoken.Help + "\n 🏳 Pilih /datasiswa : " + \
               "Jika Kamu Ingin Melihat Datasiswa Kelas XI Pada Jurusan Rekayasa Perangkat Lunak"
        myBot.reply_to(message, help)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "SELECT `nipd`, `nama`, `kelas` FROM `tabel_siswa` "
        sql.execute(query)
        data = sql.fetchall()
        totaldata = sql.rowcount
        kumpuldata = ''
        if (totaldata > 0):
            pass
            # print(data)
        no = 0
        for x in data:
            no += 1
            kumpuldata = kumpuldata + str(x) + '\n'
            print(kumpuldata)
            kumpuldata = kumpuldata.replace('(', '')
            kumpuldata = kumpuldata.replace(')', '')
            kumpuldata = kumpuldata.replace("'", '')
            kumpuldata = kumpuldata.replace(",", '')
        else:
            print('Empty Data')
        text1 = mytoken.Reply1 + "\n"
        myBot.reply_to(message, text1)
        myBot.reply_to(message, str(kumpuldata))

print(database)
print("-- Running --")
myBot.polling(none_stop=True)
