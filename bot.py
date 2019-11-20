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
keyboard3.row('Петропавловск-Камчатский','Большие Сучья')
keyboard3.row('Другой')
init = 0

# keyboard под работу
keyboard4.row('Нижнекамск','Новосибирск')
keyboard4.row('Кострома','Красноярск')
keyboard4.row('Ханты-Мансийск','Якутск')
keyboard4.row('Другой')

keyboardOk.row("Поиск")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Из какого ты города?', reply_markup=keyboard1)
    # if message.text.lower() ==   'другой':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'москва':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'санкт-петербург':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'казань':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'набережные челны':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'челябинск':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'нижний новгород':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)
    # if message.text.lower() ==   'екатеренбург':
    # 	bot.send_message(message.chat.id, reply_markup=keyboard2)

drugoy1 = ""
drugoy2 = ""
s=1
kusokgovna = 0
otkuda = ""
kuda = ""
kogda = ""
redip = 0
@bot.message_handler(content_types=['text'])
def send_text(message):
	global kogda
	global redip
	global s
	global kuda
	global otkuda
	global drugoy1
	global drugoy2
	global kusokgovna
	if s == 0:
		drugoy1 = message.text
		
		if drugoy1 != "":
			s=1
			bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
	if s == 3:
		drugoy2 = message.text
		if drugoy2 != "":
			s=1
			otkuda = drugoy1
			kuda = drugoy2
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет, мой создатель')
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id, 'Прощай, создатель')
	elif message.text.lower() == 'меня тошнит':
		bot.send_sticker(message.chat.id, 'AAQCAAMUAAPANk8TrWWZ5Lkw9j5A6IUPAAQBAAdtAANInQACFgQ')

	# 	bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
	if message.text.lower() ==   'москва':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		otkuda = message.text
		s=2
		
	if message.text.lower() ==   'санкт-петербург':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		s=2
		otkuda = message.text
	if message.text.lower() ==   'казань':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		s=2
		otkuda = message.text
	if message.text.lower() ==   'набережные челны':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		s=2
		otkuda = message.text
	if message.text.lower() ==   'челябинск':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		s=2
		otkuda = message.text
	if message.text.lower() ==   'нижний новгород':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		s=2
		otkuda = message.text
	if message.text.lower() ==   'екатеринбург':
		bot.send_message(message.chat.id, 'Вы едете на отдых или по работе?', reply_markup=keyboard2)
		s=2


	if message.text.lower() ==   'сочи':
		kuda = message.text
	if message.text.lower() ==   'анапа':
		kuda = message.text
	if message.text.lower() ==   'ялта':
		kuda = message.text
	if message.text.lower() ==   'иркутск':
		kuda = message.text
	if message.text.lower() ==   'якутск':
		kuda = message.text
	if message.text.lower() ==   'петропавловск-камчатский':
		kuda = message.text
	if message.text.lower() ==   'большие сучья':
		kuda = message.text
	if message.text.lower() ==   'красноярск':
		kuda = message.text
	if message.text.lower() ==   'кострома':
		kuda = message.text
	if message.text.lower() ==   'нижнекамск':
		kuda = message.text
	if message.text.lower() ==   'новосибирск':
		kuda = message.text
	if message.text.lower() ==   'ханты-мансийск':
		kuda = message.text
	if message.text.lower() ==   'туризм':
		bot.send_message(message.chat.id, 'В какой город вы едете?', reply_markup=keyboard3)
		s=2
	if message.text.lower() ==   'рабочая поездка':
		bot.send_message(message.chat.id, 'В какой город вы едете?', reply_markup=keyboard4)
		s=2
	if message.text.lower() ==   'другой' and s == 1:
		bot.send_message(message.chat.id, 'Введите Свой город.')
		s=0
	if message.text.lower() ==   'другой' and s > 1:
		bot.send_message(message.chat.id, 'Введите Свой город.')
		s=3
	if kuda != "" and otkuda != "" and kusokgovna == 0:
		bot.send_message(message.chat.id, 'Когда вы едете?')
		
		if message.text !=kuda:
			kusokgovna = 1
			redip = 5
	if redip == 5:
		kogda = message.text
		redip = 7
		bot.send_message(message.chat.id, 'Данные записаны',reply_markup=keyboardOk)

# @bot.message_handler(content_types=['text']
# def send_text2(message):
	if message.text.lower() ==   'поиск':
		bot.send_message(message.chat.id, "Подождите минутку... Сейчас найдём ;)")
		bot.send_message(message.chat.id,"Ж\д маршруты по вашим требованиям:"+(ZD(otkuda,kuda,kogda).poisk()))
		#bot.send_message(message.chat.id,"Авиамаршруты по вашим требованиям:"+(Avia(otkuda,kuda,kogda).poisk()))
		#bot.send_message(message.chat.id,"Наиболее дешёвый поезд:")
		#bot.send_message(message.chat.id,"Наиболее дешёвый авиарейс в"+...+"часов")
		#bot.send_message(message.chat.id,"Затраты на бензин при езде на собственном авто:")





bot.polling()