import telebot
import pyqrcode
import time

token="1776988419:AAF4xYEKQUcupQ3J7IKCqxyARF75H5PfpO0"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Selamat datang di Ticket Booth PENTAS SENI 2021 - Another Dimension.')
    sent = bot.send_message(msg.chat.id,'Masukkan NPM Abang/Mba untuk mendapatkan tiket!')
    bot.register_next_step_handler(sent, qrcode)
	
def ulang(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    sent = bot.send_message(msg.chat.id,'Mohon izin untuk memasukkan NPM Abang/Mba dengan benar!')
    bot.register_next_step_handler(sent, qrcode)

def qrcode(message):
    while message.text.isnumeric() == False and len(message.text) != 10:
        bot.register_next_step_handler(message.text, ulang)
    url=pyqrcode.create(message.text)
    url.png('TICKET-QR-CODE.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open('TICKET-QR-CODE.png','rb' ))
    
while True:
	bot.polling()
	time.sleep(1)
