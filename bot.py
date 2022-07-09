import telebot
import pyqrcode
import time
import csv
import hashlib

token=[insert your token here]
bot=telebot.TeleBot(token)

contacts = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        hasil = ""
        for i in range(len(row)):
            if(row[i]!="'"):
                hasil += row[i]
        contacts.append(hasil)


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Selamat datang di Bot Telegram Ticket Generator PENTAS SENI 2021 SEMBAGI ARUTALA Karya Luminous!')
    sent = bot.send_message(msg.chat.id,'Ketik NPM Abang/Mba di kolom chat untuk mendapatkan tiket sekarang juga!')
    bot.register_next_step_handler(sent, qrcode)
	
def ulang(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    yow = bot.send_message(msg.chat.id,'Maaf, kami tidak dapat mengenali NPM tersebut. Mohon izin untuk memasukkan NPM Abang/Mba kembali dengan benar...')
    bot.register_next_step_handler(yow, qrcode)

def qrcode(message):
    c = message.text
    morp = "p"
    morp += c[0]
    morp += c[1]
    morp += 'e'
    morp += c[2]
    morp += c[3]
    morp += 'n'
    morp += c[4]
    morp += c[5]
    morp += 's'
    morp += c[6]
    morp += c[7]
    morp += 'i'
    morp += c[8]
    morp += c[9]
    enkrip_obj = hashlib.sha256(morp.encode())
    enkrip = enkrip_obj.hexdigest()
    kebenaran = 0
    for j in range(len(contacts)):
        if(contacts[j]==enkrip):
            kebenaran=1
    if kebenaran==0:
        return ulang(message)
    hash_object = hashlib.sha224(message.text.encode())
    hashnya = hash_object.hexdigest()
    url=pyqrcode.create(enkrip+"_can_you_beat_me?\nflag{Th3_fl46_15_n0t_h3r3}")
    url.png(hashnya+'.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_message(message.chat.id,'Selamat! Abang/Mba telah berhasil melakukan registrasi pada Pentas Seni Sembagi Arutala.\n Mohon izin untuk mengirimkan tiket Abang/Mba...')
    bot.send_document(message.chat.id,open(hashnya+'.png','rb'))
    bot.send_message(message.chat.id,'Tunjukkan QR Code ini saat melakukan absensi!\nTerima kasih Abang/Mba')
    bot.send_message(message.chat.id,'Ketik /start untuk membuat tiket lagi')
    
while True:
	bot.polling()
	time.sleep(1)
