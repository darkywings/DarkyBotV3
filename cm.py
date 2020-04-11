print('importing modules...')
from vk_api.utils import get_random_id
import vk_api
import requests
import os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from accessToken import accessToken
import random

print('authorization...')
group_id = 192784148
vk_session = vk_api.VkApi(token=accessToken)
botlongpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

i = 0
outMess = ''
pathMess = 'storage/sdcard0/DarkyBot/mess'
try:
	os.mkdir(pathMess)
except:
	pass

#pathCV = os.path.abspath('curVer.ini ')
pathCV = '/storage/sdcard0/DarkyBot/curVer.ini'
try:
	with open(pathCV, 'r') as currentVersion:
		cvIni = currentVersion.read()
		cvExist = 1
		currentVersion.close()
except:
	print('File "curVer.ini" not found')

#pathUH = os.path.abspath('updHyst.ini ')
pathUH = '/storage/sdcard0/DarkyBot/updHyst.ini'
try:
	with open(pathUH, 'r') as updateHystory:
		uhIni = updateHystory.read()
		uhExist = 1
		updateHystory.close()
except:
	print('File "updHyst.ini" not found')

def send_message_to_chat(message):#функция отвечающая за отправку сообщений в беседу
	random_id = get_random_id(),
	chat_id = int(event.chat_id)

	vk.messages.send(
		random_id=random_id,
		chat_id=chat_id,
		message=message
	)
    
def init_message_from_chat(message):#определение сообщения из беседы
	global i
	global outMess
	if message.startswith('Привет, Дарки') or message.startswith('Преет, Дарки') or message.startswith('Преет Дарки') or message.startswith('Привет Дарки') or message.startswith('Привки, Дарки') or message.startswith('Здрасте, Дарки') or message.startswith('Здравствуй, Дарки') or message.startswith('Здравствуйте, Дарки') or message.startswith('Преть, Дарки') or message.startswith('Привки Дарки') or message.startswith('Здрасте Дарки') or message.startswith('Здравствуй Дарки') or message.startswith('Здравствуйте Дарки') or message.startswith('Преть Дарки') or message.startswith('Здрастете, Дарки') or message.startswith('Здрастете Дарки') or message.startswith('Ку Дарки') or message.startswith('Ку, Дарки') or message.startswith('Куку Дарки') or message.startswith('Куку, Дарки') or message.startswith('Прувет, Дарки') or message.startswith('Прувет Дарки'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Преть')
	elif message.startswith('Дарки, расскажи о себе') or message.startswith('Дарки расскажи о себе'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		with open(pathCV) as file:
			curVer = file.read()
		send_message_to_chat(curVer)
	elif message.startswith('Дарки, история обновлений') or message.startswith('Дарки история обновлений'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		with open(pathUH) as file:
			updHyst = file.read()
		send_message_to_chat(updHyst)
	elif "Помощь" in event.obj.message['text'] or "помощь" in event.obj.message['text']:
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Раз вы вызвали помощь, значит вам нужна помощь, а значит я могу помочь^^\nЕсли вы хотите узнать кто я - введите "Расскажи о себе"\nЕсли вы хотите узнать мои команды - введите "Команды"')
	elif "Команды" in event.obj.message['text'] or "команды" in event.obj.message['text']:
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Доступные на данный момент команды:\n1. Привет, Дарки\n2. Расскажи о себе\n3. История обновлений\n4. Помощь\n5. Дарки выбери <варианты через или>\n6. Дарки, вероятность <предложение>\n7. Дарки, попытка <действие>\n8. Дарки. голос\n9. Дарки, сброс собранных данных')
	elif "test" in event.obj.message['text'] or "тест" in event.obj.message['text'] or "Тест" in event.obj.message['text'] or "Test" in event.obj.message['text']:
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		if "test2310" in event.obj.message['text'] or "тест2310" in event.obj.message['text'] or "Тест2310" in event.obj.message['text'] or "Test2310" in event.obj.message['text']:
			send_message_to_chat("Вы получили секрет! Ссылка на тестовый сервер")
			send_message_to_chat("Вот ваша ссылка: https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp")
		else:
			send_message_to_chat('Вы почти у цели, введите вдобавок к "тест/test" дату рождения моего создателя в формате ДДММ\nПример:тест0206')
	elif message.startswith("Дарки выбери"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		choosingMess = event.obj.message['text']
		chooseStr = choosingMess.lstrip('Дарки ')
		chooseStr = chooseStr.lstrip('выбери')
		chooseList = chooseStr.split(' ')
		chooseList = chooseStr.split(' или')
		chooseListLen = len(chooseList)
		chooseRandInt = random.randint(0, chooseListLen)
		chooseResult = chooseList[chooseRandInt - 1]
		send_message_to_chat('Я выбираю' + chooseResult)
	elif message.startswith('Дарки, вероятность'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		probabilityMess = event.obj.message['text']
		probabilityStr = probabilityMess.lstrip('Дарки, ')
		probabilityStr = probabilityStr.lstrip('вероятность')
		probabilityRandom = random.randint(0, 100)
		probabilityResult = str(probabilityRandom) + '%'
		send_message_to_chat('Вероятность того, что' + probabilityStr + ' составляет ' + probabilityResult)
	elif message.startswith('Дарки, попытка'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		tryMess = event.obj.message['text']
		tryStr = tryMess.lstrip('Дарки, ')
		tryStr = tryStr.lstrip('попытка')
		tryRandom = random.randint(0, 1)
		if tryRandom == 0:
			send_message_to_chat('Ваша попытка ' + tryStr + ' вышла неудачной')
		if tryRandom == 1:
			send_message_to_chat('Ваша попытка ' + tryStr + ' вышла удачной')
	elif message.startswith('Дарки запустись') or message.startswith('Дарки. запустись') or message.startswith('Дарки перезапустись') or message.startswith('Дарки. перезапустись') or message.startswith('Дарки выключись') or message.startswith('Дарки. выключись') or message.startswith('Дарки проверь наличие своих файлов') or message.startswith('Дарки. проверь наличие своих файлов') or message.startswith('Дарки обновись') or message.startswith('Дарки. обновись')  or message.startswith('Дарки обнови главный скрипт') or message.startswith('Дарки. обнови главный скрипт'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Данная команда не работает в беседе')
	elif message.startswith("Дарки, голос") or message.startswith("Дарки голос"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		randSendLen = random.randint(2, 15)
		with open(pathMess + '/' + event.chat_id + '.ini') as messRead:
			allWords = messRead.read()
			messRead.close()
		wordList = allWords.lstrip(' ')
		wordList = wordList.split(' ')
		wordListLen = len(wordList)
		while i < randSendLen:
			randWord = random.randint(1, wordListLen)
			wordOut = wordList[randWord - 1]
			outMess = outMess + ' ' + wordOut
			i = i + 1
		send_message_to_chat(outMess)
		i = 0
		outMess = ''
	elif message.startswith("Дарки, сброс собранных данных") or message.startswith("Дарки сброс собранных данных"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Очищаю собранные данные об этом диалоге...')
		with open(pathMess + '/' + str(event.chat_id) + '.ini', 'w') as messEarse:
			messEarse.close()
		send_message_to_chat('Данные очищены')
	elif "Дурки" in event.obj.message['text']:
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Обидно ;с')

print('done')
while True:
	try:
		for event in botlongpoll.listen(): #своеобразное прослушивание новых сообщений
			if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
				messageText = event.obj.message['text']
				try:
					with open(pathMess + '/' + str(event.chat_id) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				expect:
					with open(pathMess + '/' + str(event.chat_id) + '.ini', 'w') as messFile:
						messFile.close()
					with open(pathMess + '/' + str(event.chat_id) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				init_message_from_chat(event.obj.message['text'])
	except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
        requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		print('<<timeout>>')
