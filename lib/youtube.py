import telebot
video = 0
video_search = ''
video_search_list = []
@bot.message_handler(content_types=['text'])
def send_text(message):
	global video
	global video_search
	global video_search_list
	if message.text.lower() == "поиск видео":
		bot.send_message(message.chat.id, 'По какому запросу найти видео')
	video = 1
	if video = 1:
		video_search = message.text
		video_search_list = video_search.split()
		video_search = 'https://www.youtube.com/results?search_query='
		for i in range(len(video_search_list)):
			video_search += video_search_list[i]
			video_search += '+'
		video_search = video_search[:-1]
