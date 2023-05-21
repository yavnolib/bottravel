import telebot
import time
import random

bot = telebot.TeleBot('bot-token')
@bot.message_handler(content_types=['text'])
def start(message):
	if message.text.lower() == 'музыка':
		for i in range(3):
			n=random.randint(1,5)
			audio = open(str(n)+".mp3", mode='rb')
			print("opened "+str(n)+".mp3")
			bot.send_audio(message.from_user.id,audio, timeout=1000)
bot.polling()
