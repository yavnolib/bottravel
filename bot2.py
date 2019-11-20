import telebot
from parse_rzd import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re
import winsound
import pyautogui
bot = telebot.TeleBot("955705841:AAH2Pj9QrLas4Nk_UFWy4sh5swl05n2AKOU")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardOk= telebot.types.ReplyKeyboardMarkup(True, True)

keyboard1.row('Москва','Санкт-петербург')
keyboard1.row('Казань','Набережные Челны')
keyboard1.row('Челябинск','Нижний Новгород')
keyboard1.row('Другой')

keyboard2.row('Туризм', 'Рабочая поездка')

# keyboard под туризм
keyboard3.row('Сочи','Анапа')
keyboard3.row('Ялта','Иркутск')
keyboard3.row('Петропавловск-Камчатский','Ейск')
keyboard3.row('Другой')
init = 0

# keyboard под работу
keyboard4.row('Нижнекамск','Новосибирск')
keyboard4.row('Кострома','Красноярск')
keyboard4.row('Ханты-Мансийск','Якутск')
keyboard4.row('Другой')

keyboardOk.row("Поиск")

s=0
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Из какого ты города?', reply_markup=keyboard1)
    global s
    s = 1
    print(s)
print(s)
drugoy1 = ""
drugoy2 = ""
kusokgovna = 0
otkuda = ""
kuda = ""
kogda = ""
redip = 0

@bot.message_handler(content_types=["text"])
def send_text(message):
	global kogda
	global redip
	global s
	global kuda
	global otkuda
	global drugoy1
	global drugoy2
	print(s)
	global kusokgovna
	if s == 1 and message.text.lower() == "другой":
		bot.send_message(message.chat.id, 'Введите свой город?')
		s = 11

	elif s == 11:
		otkuda = message.text
		s = 2
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)			
	elif s == 3 and message.text.lower() == "другой":
		bot.send_message(message.chat.id, 'Введите свой город?')
		s = 31
	elif s == 31:
		kuda = message.text
		bot.send_message(message.chat.id, 'Когда вы едете?')
		s = 4		
	elif s == 1:
		otkuda = message.text
		s = 2
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
	elif s == 2 and message.text.lower() == "рабочая поездка":
		bot.send_message(message.chat.id, 'В какой город вы едете?', reply_markup=keyboard4)
		s = 3
	elif s == 2 and message.text.lower() == "туризм":
		bot.send_message(message.chat.id, 'В какой город вы едете?', reply_markup=keyboard3)
		s = 3
	elif s == 3:
		kuda = message.text
		s = 4
		bot.send_message(message.chat.id, 'Когда вы едете?')
	elif s == 4:
		kogda = message.text
		bot.send_message(message.chat.id, message.text,reply_markup=keyboardOk)

		s = 5
	elif s == 5 and message.text.lower() == "поиск":
		bot.send_message(message.chat.id, otkuda)
		bot.send_message(message.chat.id, kuda)
		bot.send_message(message.chat.id, kogda)
		bot.send_message(message.chat.id,"Ж\д маршруты по вашим требованиям "+(ZD(otkuda,kuda,kogda).poisk()))
bot.polling()
