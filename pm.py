print('importing modules...')
import requests
import os
import vk_api
from accessToken import accessToken
from vk_api.longpoll import VkLongPoll, VkEventType
import random

print('Authorization...')
vk_session = vk_api.VkApi(token=accessToken)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

i = 0
outMess = ''
pathMess = '/storage/sdcard0/DarkyBot/mess'
try:
	os.mkdir(pathMess)
except:
	pass

cvExist = 0
uhExist = 0

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
	
print('loading functions...')

def send_message_to_user(message):
	user_id = int(event.user_id)
	random_id = event.random_id
	
	vk.messages.send(
		random_id=random_id,
		user_id=user_id,
		message=message
	)

def init_message_from_user(message): #определяет сообщения от пользователя
	global i
	global outMess
	if message.startswith('Привет, Дарки') or message.startswith('Преет, Дарки') or message.startswith('Преет Дарки') or message.startswith('Привет Дарки') or message.startswith('Привки, Дарки') or message.startswith('Здрасте, Дарки') or message.startswith('Здравствуй, Дарки') or message.startswith('Здравствуйте, Дарки') or message.startswith('Преть, Дарки') or message.startswith('Привки Дарки') or message.startswith('Здрасте Дарки') or message.startswith('Здравствуй Дарки') or message.startswith('Здравствуйте Дарки') or message.startswith('Преть Дарки') or message.startswith('Здрастете, Дарки') or message.startswith('Здрастете Дарки') or message.startswith('Ку Дарки') or message.startswith('Ку, Дарки') or message.startswith('Куку Дарки') or message.startswith('Куку, Дарки') or message.startswith('Прувет, Дарки') or message.startswith('Прувет Дарки') or message.startswith('Прив Дарки'):
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Преть')
	elif message.startswith("Дарки, голос") or message.startswith("Дарки голос"):
		print('user:', event.user_id, ':', event.text)
		randSendLen = random.randint(2, 15)
		with open(pathMess + '/' + str(event.user_id) + '.ini') as messRead:
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
		send_message_to_user(outMess)
		i = 0
		outMess = ''
	elif message.startswith("Дарки, сброс собранных данных") or message.startswith("Дарки сброс собранных данных"):
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Очищаю собранные данные об этом диалоге...')
		with open(pathMess + '/' + str(event.user_id) + '.ini', 'w') as messEarse:
			messEarse.close()
		send_message_to_user('Данные очищены')
	elif message.startswith("Дарки, размер собранных данных") or message.startswith("Дарки размер собранных данных"):
		sizePath = pathMess + '/' + str(event.user_id) + '.ini'
		fSize = os.path.getsize(sizePath)
		sizeType = 0
		while fSize > 1024:
			fSize = fSize / 1024
			sizeType = sizeType + 1
		if sizeType == 0:
			sizeTypeStr = 'Б'
		elif sizeType == 1:
			sizeTypeStr = 'КБ'
		elif sizeType == 2:
			sizeTypeStr = 'МБ'
		elif sizeType == 3:
			sizeTypeStr = 'ГБ'
		send_message_to_user('Размер собранных данных об этом диалоге составляет: ' + fSize + ' ' + sizeTypeStr)
	elif message.startswith("Дарки выбери") or message.startswith("Дарки, выбери"):
		print('user:', event.user_id, ':', event.text)
		choosingMess = event.text
		if message.startswith("Дарки выбери"):
			chooseStr = choosingMess.lstrip('Дарки ')
		if message.startswith("Дарки, выбери"):
			chooseStr = choosingMess.lstrip('Дарки, ')
		chooseStr = chooseStr.lstrip('выбери')
		chooseStr = chooseStr.lstrip(' ')
		chooseList = chooseStr.split(' или ')
		chooseListLen = len(chooseList)
		chooseRandInt = random.randint(0, chooseListLen)
		chooseResult = chooseList[chooseRandInt - 1]
		send_message_to_user('Я выбираю ' + chooseResult)
	elif message.startswith('Дарки, вероятность') or message.startswith('Дарки вероятность'):
		print('user:', event.user_id, ':', event.text)
		probabilityMess = event.text
		if message.startswith('Дарки, вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки, ')
		if message.startswith('Дарки вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки')
		probabilityStr = probabilityStr.lstrip('вероятность')
		probabilityRandom = random.randint(0, 100)
		probabilityResult = str(probabilityRandom) + '%'
		send_message_to_user('Вероятность того, что' + probabilityStr + ' составляет ' + probabilityResult)
	elif message.startswith('Дарки, попытка') or message.startswith('Дарки попытка'):
		print('user:', event.user_id, ':', event.text)
		tryMess = event.text
		if message.startswith('Дарки, попытка'):
			tryStr = tryMess.lstrip('Дарки, ')
		if message.startswith('Дарки попытка'):
			tryStr = tryMess.lstrip('Дарки ')
		tryStr = tryStr.lstrip('попытка')
		tryRandom = random.randint(0, 1)
		if tryRandom == 0:
			send_message_to_user('Попытка' + tryStr + ' вышла неудачной')
		if tryRandom == 1:
			send_message_to_user('Попытка' + tryStr + ' вышла удачной')
	elif "расскажи о себе" in event.text or "Расскажи о себе" in event.text:
		print('user:', event.user_id, ':', event.text)
		if cvExist == 1:
			with open(pathCV) as fileCV:
				curVer = fileCV.read()
			send_message_to_user(curVer)
		else:
			send_message_to_user('К сожалению мне не удалось найти файл с помощью которого я бы с радостью рассказала вам о себе')
	elif "История обновлений" in event.text or "история обновлений" in event.text:
		print('user:', event.user_id, ':', event.text)
		if uhExist == 1:
			with open(pathUH) as fileUH:
				updHyst = fileUH.read()
			send_message_to_user(updHyst)
		else:
			send_message_to_user('К сожалению мне не удалось найти файл в котором содержалась история обновлений')
	elif "Помощь" in event.text or "помощь" in event.text:
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Раз вы вызвали помощь, значит вам нужна помощь, а значит я могу помочь^^\nЕсли вы хотите узнать кто я - введите "Расскажи о себе"\nЕсли вы хотите узнать мои команды - введите "Команды"')
	elif "Команды" in event.text or "команды" in event.text:
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Доступные на данный момент команды:\n1. Привет\n2. Расскажи о себе\n3. История обновлений\n4. Помощь\n5. Дарки выбери <варианты через или>\n6. Дарки, вероятность <предложение>\n7. Дарки, попытка <действие>\n8. Дарки. голос\n9. Дарки, сброс собранных данных')
	elif "test" in event.text or "тест" in event.text or "Тест" in event.text or "Test" in event.text:
		print('user:', event.user_id, ':', event.text)
		if "test2310" in event.text or "тест2310" in event.text or "Тест2310" in event.text or "Test2310" in event.text:
			send_message_to_user("Вы получили секрет! Ссылка на тестовый сервер")
			send_message_to_user("Вот ваша ссылка: https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp")
		else:
			send_message_to_user('Вы почти у цели, введите вдобавок к "тест/test" дату рождения моего создателя в формате ДДММ\nПример:тест0206')
	elif "Дарки" in event.text and not "запустись" in event.text and not "перезапустись" in event.text and not "выключись" in event.text and not "проверь наличие своих файлов" in event.text and not "обновись" in event.text and not "обнови главный скрипт" in event.text:
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Я к вашим услугам')
	elif "Дурки" in event.text:
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Обидно ;с')

print('Done')
while True:
	try:
		for event in longpoll.listen(): #своеобразное прослушивание новых сообщений
			if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
				messageText = event.text
				try:
					with open(pathMess + '/' + str(event.user_id) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				except:
					with open(pathMess + '/' + str(event.user_id) + '.ini', 'w') as messFile:
						messFile.close()
					with open(pathMess + '/' + str(event.user_id) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageTextf)
						messWrite.close()
				init_message_from_user(event.text)
	except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
        requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		print('<<timeout>>')
