print('importing modules...')
import requests
import os
import vk_api
from accessToken import accessToken
from vk_api.longpoll import VkLongPoll, VkEventType

print('Authorization...')
vk_session = vk_api.VkApi(token=accessToken)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

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
	if "Прив" in event.text or "прив" in event.text or "Преет" in event.text or "преет" in event.text or "Ку" in event.text or "ку" in event.text or "Здрасте" in event.text or "здрасте" in event.text or "Здравствуй" in event.text or "здравствуй" in event.text or "Даров" in event.text or "даров" in event.text or "Дороу" in event.text or "дороу" in event.text or "Преть" in event.text or "преть" in event.text or "Прувет" in event.text or "прувет" in event.text or "Здрасть" in event.text or "здрасть" in event.text:
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Преть')
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
		send_message_to_user('Доступные на данный момент команды:\n1. Привет\n2. Расскажи о себе\n3. История обновлений\n4. Помощь')
	elif "test" in event.text or "тест" in event.text or "Тест" in event.text or "Test" in event.text:
		print('user:', event.user_id, ':', event.text)
		if "test2310" in event.text or "тест2310" in event.text or "Тест2310" in event.text or "Test2310" in event.text:
			send_message_to_user("Вы получили секрет! Ссылка на тестовый сервер")
			send_message_to_user("Вот ваша ссылка: https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp")
		else:
			send_message_to_user('Вы почти у цели, введите вдобавок к "тест/test" дату рождения моего создателя в формате ДДММ\nПример:тест0206')
	elif "Дарки" in event.text:
		print('user:', event.user_id, ':', event.text)
		send_message_to_user('Я к вашим услугам')

print('Done')
while True:
	try:
		for event in longpoll.listen(): #своеобразное прослушивание новых сообщений
 		   if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
  		      init_message_from_user(event.text)
	except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
        requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		print('<<timeout>>')
