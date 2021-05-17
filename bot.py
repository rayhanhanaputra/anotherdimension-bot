import telebot
import pyqrcode
import time
import csv
import hashlib

token="1776988419:AAF4xYEKQUcupQ3J7IKCqxyARF75H5PfpO0"
bot=telebot.TeleBot(token)

contacts = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        hasil = ""
        for i in range(len(row)):
            if(row[i]>='0' and row[i]<='9'):
                hasil += row[i]
        contacts.append(hasil)


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Selamat datang di Bot Telegram Ticket Generator PENTAS SENI 2021 SEMBAGI ARUTALA Karya Luminous!')
    sent = bot.send_message(msg.chat.id,'Masukkan NPM Abang/Mba untuk mendapatkan tiket sekarang juga!')
    bot.register_next_step_handler(sent, qrcode)
	
def ulang(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    yow = bot.send_message(msg.chat.id,'Mohon izin untuk memasukkan NPM Abang/Mba dengan benar...')
    bot.register_next_step_handler(yow, qrcode)

def qrcode(message):
    kebenaran = 0
    for j in range(len(contacts)):
        if(contacts[j]==message.text):
            kebenaran=1
    if kebenaran==0:
        return ulang(message)
    hash_object = hashlib.sha512(message.text.encode())
    hashnya = hash_object.hexdigest()
    url=pyqrcode.create(message.text)
    url.png(hashnya+'.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open(hashnya+'.png','rb'))
    bot.send_message(message.chat.id,'Tunjukkan QR Code ini saat melakukan absensi!\nTerima kasih Bang/Mba')
    bot.send_message(message.chat.id,'Ketik /start untuk membuat tiket lagi')
    
while True:
	bot.polling()
	time.sleep(1)
