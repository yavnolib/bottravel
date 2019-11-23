import telebot
import random
import time, re
import time
import pyowm
import requests
from mqtt import *
import datetime
import reader
import os
from dotenv import load_dotenv
import codecs

token=load_dotenv()
token = os.getenv('TOKEN')
print(token)

f = codecs.open( 'taxinumbers.txt', "r", "utf_8_sig" )
taxicities = f.read()
taxicities = taxicities.split('\r\n')[:-1]
taxidict = dict()

for i in taxicities:
    key = i[:i.index(';')]
    taxidict[key] = i[i.index(';') + 2:]

commandlist = {'/start': 'start_message(message)', '/help' : 'help_message(message)', '/findtickets' : 'tickets_message(message)', '/route' : 'tickets_message(message)', '/weather' : 'weather_message(message)', '/music' : 'music_message(message)', '/developers' : 'developers_message(message)', '/taxi' : 'taxi_message(message)'}
commandlist_ru = {'старт': 'start_message(message)', 'помощь' : 'help_message(message)', 'маршрут' : 'tickets_message(message)', 'погода' : 'weather_message(message)', 'музыка' : 'music_message(message)', 'разработчики' : 'developers_message(message)', 'такси' : 'taxi_message(message)'}
lovestickerpack = ['CAADAgAD2QADVp29CtGSZtLSYweoFgQ', 'CAADAgAD0gADVp29Cg4FcjZ1gzWKFgQ', 'CAADAgAD0wADVp29CvUyj5fVEvk9FgQ', 'CAADAgAD2AADVp29CokJ3b9L8RQnFgQ', 'CAADAgAD3gADVp29CqXvdzhVgxXEFgQ', 'CAADAgADFQADwDZPE81WpjthnmTnFgQ', 'CAADAgADBQADwDZPE_lqX5qCa011FgQ', 'CAADAgADDQADwDZPE6T54fTUeI1TFgQ', 'CAADAgADHQADwDZPE17YptxBPd5IFgQ', 'CAADAgAD4QcAAnlc4gndRsN-Tyzk1xYE', 'CAADAgAD3wcAAnlc4gmeYgfVO_CEsxYE', 'CAADAgAD4AcAAnlc4gmXqeueTbWXlRYE', ]
questionstickerpack = ['CAADAgAD4wADVp29Cg_4Isytpgs3FgQ', 'CAADAgADEgADwDZPEzO8ngEulQc3FgQ', 'CAADAgADEAADwDZPE-qBiinxHwLoFgQ', 'CAADAgADIAADwDZPE_QPK7o-X_TPFgQ', 'CAADAgAD2wcAAnlc4gkSqCLudDgLbhYE', 'CAADAgADzwcAAnlc4gnrZCnufdBTahYE', 'CAADAgAD2QcAAnlc4gn3Ww8qzk3S3BYE', 'CAADAgAD0gcAAnlc4gmLqZ82yF4OlxYE']
angrystickerpack = ['CAADAgAD3AADVp29Cpy9Gm5Tg192FgQ', 'CAADAgAD2wADVp29Clxn-p9taVttFgQ', 'CAADAgADywADVp29CllGpcs9gzQoFgQ']
loadstickerpack = ['CAADAgADGAADwDZPE9b6J7-cahj4FgQ', 'CAADAgAD1QADVp29CveXwRdcmk7nFgQ', 'CAADAgADwAADVp29Ct1dnTI9q-YvFgQ', 'CAADAgAD4QADVp29ClvBlItA-NOgFgQ', 'CAADAgAD5QADVp29CggLFmSVBdGKFgQ']
developerslist = ['рустам', 'ярослав', 'владимир', 'даниэль', 'игорь']
nongratlist = ['арина', 'ариша']
gratlist = ['алия']

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('start', 'help', 'weather', 'developers')
keyboard1.row('music', 'findtickets', 'taxi')

tok=load_dotenv()
tok=os.getenv("owm")
print(tok)
owm = pyowm.OWM(tok, language = 'ru')
bot = telebot.TeleBot(token)

fromplace = str()
toplace = str()
dateregistration = str()
status = ''

@bot.message_handler(commands=['taxi'])
def taxi_message(message):
	bot.send_message(message.chat.id, 'Введите город, в котором вы хотели бы заказать такси')
	bot.register_next_step_handler(message, taxi_telephone_numbers_message)
	
def taxi_telephone_numbers_message(message):
	if message.text.lower() in commandlist:
		exec(commandlist[message.text.lower()])
	elif message.text.lower() in commandlist_ru:
		exec(commandlist_ru[message.text.lower()])
	elif '/' + message.text.lower() in commandlist:
		exec(commandlist['/' + message.text.lower()])
	else:
		global taxidict
		ttnumbers = taxidict[message.text.lower()]
		ttnumbers = ttnumbers.split('. ')
		ttnumbers = '\n'.join(ttnumbers)
		bot.send_message(message.chat.id, ttnumbers)
	
@bot.message_handler(commands=['developers'])
def developers_message(message):
	print('пока в разработке')


@bot.message_handler(commands=['findtickets', 'route'])

def tickets_message(message):
	bot.send_message(message.chat.id, 'Введите город отправления')
	bot.register_next_step_handler(message, fromplace_registration)
	
def fromplace_registration(message):
	global commandlist
	global fromplace
	if message.text.lower() in commandlist:
		exec(commandlist[message.text.lower()])
	elif message.text.lower() in commandlist_ru:
		exec(commandlist_ru[message.text.lower()])
	elif '/' + message.text.lower() in commandlist:
		exec(commandlist['/' + message.text.lower()])
	else:
		fromplace = message.text.lower()
		bot.send_message(message.chat.id, 'Введите город назначения')
		bot.register_next_step_handler(message, toplace_registration)
def toplace_registration(message):
	global commandlist
	global toplace
	if message.text.lower() in commandlist:
		exec(commandlist[message.text.lower()])
	elif message.text.lower() in commandlist_ru:
		exec(commandlist_ru[message.text.lower()])
	elif '/' + message.text.lower() in commandlist:
		exec(commandlist['/' + message.text.lower()])
	else:
		toplace = message.text.lower()
		bot.send_message(message.chat.id, 'Введите дату отправления')#rzd
		bot.register_next_step_handler(message, date_registration)
def date_registration(message):
	global commandlist
	global fromplace
	global toplace
	global dateregistration
	global loadsticerpack
	if message.text.lower() in commandlist:
		exec(commandlist[message.text.lower()])
	elif message.text.lower() in commandlist_ru:
		exec(commandlist_ru[message.text.lower()])
	elif '/' + message.text.lower() in commandlist:
		exec(commandlist['/' + message.text.lower()])
	else:
		dateregistration = message.text.lower()
		print(fromplace)
		print(toplace)
		print(dateregistration)
		Sendler(fromInput=fromplace,fromOutput=toplace,date=dateregistration).send()
		bot.send_message(message.chat.id, 'Ищу билеты по выбранному направлению')
		bot.send_sticker(message.chat.id, random.choice(loadstickerpack))
		bot.send_message(message.chat.id, 'Билеты по маршруту {0} - {1} на {2} '.format(fromplace, toplace, dateregistration) + "\n" + reader.read())   
    
    
@bot.message_handler(commands=['start'])

def start_message(message):
	global weatherinformation
	global lovestickerpack
	bot.send_message(message.chat.id, 'Привет!\nМеня зовут Travellta!....John Travellta!Да, я знаю, у меня красивое имя..;) \nВот список моих функций на данный момент:\n1./start\n2./weather\n3./help\n4./music', reply_markup=keyboard1)
	bot.send_sticker(message.chat.id, random.choice(lovestickerpack))
    
@bot.message_handler(commands=['weather'])

def weather_message(message):
	bot.send_message(message.chat.id, 'Напишите город, погодные условия которого вы хотели бы узнать')
	bot.register_next_step_handler(message, weather_information)
def weather_information(message):
	place=''
	global status
	global angrystickerpack
	if message.text.lower() in commandlist:
		exec(commandlist[message.text.lower()])
	elif message.text.lower() in commandlist_ru:
		exec(commandlist_ru[message.text.lower()])
	elif '/' + message.text.lower() in commandlist:
		exec(commandlist['/' + message.text.lower()])
	else:
		try:
			place = message.text.lower()
			observation = owm.weather_at_place(place)
			weather = observation.get_weather()
			status = weather.get_detailed_status()
			temp = weather.get_temperature('celsius')['temp']
			wind = weather.get_wind()['speed']
			print(weather)
			weathercity = message.text[0].upper() + message.text.lower()[1:]
			bot.send_message(message.chat.id, "Погода города " + weathercity + "\nТемпература: " + str(temp) + "°C" + "\nНа улице: " + str.title(status) + "\nСкорость Ветра: " + str(wind) + "м/c")
			if temp >= 15:
				bot.send_message(message.chat.id, "Погода-mood: Cамое-то ")
			elif 15 > temp  and temp > 0:
				bot.send_message(message.chat.id, "Погода-mood: Накинь что нибудь на себя ")
			elif temp < 0 and -25 < temp:
				bot.send_message(message.chat.id, "Погода-mood: Одевайся мать, пора воевать ")
			elif temp <= -25:
				bot.send_message(message.chat.id, "Погода-mood: Ты умрёшь, если уйдёшь")
		except pyowm.exceptions.api_response_error.NotFoundError:
			bot.reply_to(message, 'Врешь, такого города нет на картах')
			bot.send_sticker(message.chat.id, random.choice(angrystickerpack))
    
@bot.message_handler(commands=['help'])
def help_message(message):
	global lovestickerpack
	bot.send_message(message.chat.id, '1./start - эта функция позволяет Вам сбросить наш диалог и вернуться к исходной точке\n2./weather - позволяет вам узнать состояние погоды в данном месте\n3./help - эта  функция сработала прямо сейчас')
	bot.send_sticker(message.chat.id,random.choice(lovestickerpack))
    
    
@bot.message_handler(commands=['music'])
def music_message(message):
	audiolist = []
	for i in range(3):
		while True:
			n = random.randint(1,11)
			if n not in audiolist:
				break
		audiolist.append(n)
		audio = open(str(n) + ".mp3", mode='rb')
		print("opened " + str(n) + ".mp3")
		bot.send_audio(message.from_user.id, audio, timeout=1000)

@bot.message_handler(content_types=['text'])
def text_analyze(message):
	global lovestickerpack
	global angrystickerpack
	global questionstickerpack
	if 'билеты' in message.text.lower() or 'найти билеты' in message.text.lower():
		bot.register_next_step_handler(message, tickets_message)
	elif '/' + message.text.lower() in commandlist:
		exec(commandlist['/' + message.text.lower()])
	elif message.text.lower() in commandlist_ru:
		exec(commandlist_ru[message.text.lower()])
	elif message.text.lower() in developerslist:
		developername = message.text[0].upper() + message.text.lower[1:]
		bot.reply_to(message, 'в моей системе рейтинга {0} стоит на первом месте'.format(developername))
		bot.send_sticker(message.chat.id, random.choice(lovestickerpack))
	elif message.text.lower() in nongratlist:
		nongratname = message.text[0].upper() + message.text.lower()[1:]
		bot.reply_to(message, '{0}...{0}...звучит как что-то неприятное'.format(nongratname))
		bot.send_sticker(message.chat.id, random.choice(angrystickerpack))
        elif "чемодан" in message.text.lower():
		#bot.reply_to(message, 'RUSSIAN, MOTHERFUCKER, DO YOU SPEAK IT ?')
		bot.send_message(message.chat.id, 'Документы:\nпаспорт: внутренний или загран; документы для ребенка: 1) паспорт, 2) свидетельство о рождении, 3) согласие на выезд из России, если ребенок едет за границу без родителей; наличные деньги; билеты на самолет, поезд, автобус; брони отелей; водительские права; копия паспорта; страховой полис путешественника')
		bot.send_message(message.chat.id, 'Техника и гаджеты в дорогу: \ncмартфон и зарядка; внешний жесткий диск; дорожный утюг; маленький электрический чайник; наушники; ноутбук и зарядка; переходник для розеток; плеер; тройник, удлинитель или сетевой фильтр; фен; фотоаппарат, зарядка, карты памяти, сумка для камеры; штатив, монопод, палка для селфи; электронная книга')
		bot.send_message(message.chat.id, 'Бытовые мелочи и комфорт в поездке: \nсумочка или городской рюкзак для прогулок; блокнот и ручка; вилка, ложка, тарелка, чашка; зонт; карманное зеркало; карта; книга, путеводитель, журнал; маска для сна, беруши, надувная подушка; обычные пакеты; полотенце; разговорник; солнечные очки; туалетная бумага; швейный набор; швейцарский армейский нож')
		bot.send_message(message.chat.id, 'Гигиена и косметика в поездку: \nбритва; дезодорант; зубная паста и щетка; расческа; ватные палочки, ватные диски; Влажные салфетки, бумажные платочки; гигиеническая помада, бальзам для губ; гигиенические прокладки, тампоны; дезинфицирующий гель для рук; зубная нить, зубочистки; крем от солнца; кремы для лица и тела; ножницы и пилочка для ногтей; очки или контактные линзы с контейнером и раствором; парфюм; пена для и после бритья; помада, тушь для ресниц и другая декоративная косметика, средство для снятия макияжа; презервативы; репеллент от комаров; средство для укладки волос; фумигатор; шампунь, кондиционер для волос, мыло, гель для душа, мочалка')

		bot.send_sticker(message.chat.id, random.choice(questionstickerpack))
        elif message.text.lower() in gratlist:
                bot.reply_to(message, "Алия... Алиюша... Звучит как что-то приятное.. ")
                bot.send_sticker(message.chat.id, random.choice(loveatickerpack))
        else:
                pass
bot.polling()
