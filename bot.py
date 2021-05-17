import telebot
import pyqrcode
import time
import csv

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
    bot.send_message(msg.chat.id,'Selamat datang di Ticket Booth PENTAS SENI 2021 - Another Dimension.')
    sent = bot.send_message(msg.chat.id,'Masukkan NPM Abang/Mba untuk mendapatkan tiket!')
    bot.register_next_step_handler(sent, qrcode)
	
def ulang(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    yow = bot.send_message(msg.chat.id,'Mohon izin untuk memasukkan NPM Abang/Mba dengan benar!')
    bot.register_next_step_handler(yow, qrcode)

def qrcode(message):
    kebenaran = 0
    for j in range(len(contacts)):
        if(contacts[j]==message.text):
            kebenaran=1
    if kebenaran==0:
        return ulang(message)
    url=pyqrcode.create(message.text)
    url.png('TICKET-QR-CODE.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    pesan = "TICKET-QR-CODE-"+message.text+".png"
    bot.send_document(message.chat.id,open(pesan,'rb' ))
    bot.send_message(message.chat.id,'Tunjukkan QR Code ini saat melakukan absensi!\nTerima kasih Bang/Mba')
    bot.send_message(message.chat.id,'Ketik /start untuk membuat tiket lagi')
    
while True:
	bot.polling()
	time.sleep(1)
