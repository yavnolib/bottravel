import telebot
import time
import random

bot = telebot.TeleBot('722305738:AAFjAzSpmuuRQdggqlXSGND8WQyS-zUbpgo')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'sosi')
@bot.message_handler(content_types=['text'])
def start(message):
	if message.text.lower() == 'музыка':
		for i in range(3):
			n=random.randint(1,5)
			audio = open(str(n)+".mp3", mode='rb')
			print("opened "+str(n)+".mp3")
			bot.send_audio(message.from_user.id,audio, timeout=1000)
bot.polling()