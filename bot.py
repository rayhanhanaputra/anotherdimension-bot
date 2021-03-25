import telebot
import pyqrcode
import time

token="1776988419:AAF4xYEKQUcupQ3J7IKCqxyARF75H5PfpO0"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Selamat datang di Ticket Booth PENTAS SENI 2021 - Another Dimension.\nKetik /daftar untuk mendapatkan tiket sekarang juga!')

@bot.message_handler(commands=['daftar'])
def qr_code_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_message(message.chat.id, "Masukkan NPM abang/mba: ")
    bot.register_next_step_handler(sent, qrcode)

def qrcode(message):
    if(len(message)!=10 and messange.isdigit()):
	url=pyqrcode.create(message.text)
	url.png('TICKET-QR-CODE.png',scale=15)
	bot.send_chat_action(message.chat.id, 'upload_document')
	bot.send_document(message.chat.id,open('TICKET-QR-CODE.png','rb' ))
    else:
	bot.send_message(message.chat.id, "Input salah :(")
    
while True:
	bot.polling()
	time.sleep(1)
