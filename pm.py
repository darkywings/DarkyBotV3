print('Starting...')

print('Importing [requests]...')
import requests

print('Importing [os]...')
import os

print('Importing [vk_api]...')
import vk_api

print('Authorization...')
vk_session = vk_api.VkApi(token='ea6aac611a3593e5d0aa74e1bf58ea9a0421203c85bcc1528cd259cb5a287a92cfb2d12f059f349781836')

print('Importing [VkLongPoll]...')
print('Importing [VkEventType]...')

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

cvExist = 0
uhExist = 0

pathCV = os.path.abspath('curVer.ini ')
try:
	with open(pathCV, 'r') as currentVersion:
		cvIni = currentVersion.read()
		cvExist = 1
except:
	print('File "curVer.ini" not found')

pathUH = os.path.abspath('updHyst.ini ')
try:
	with open(pathUH, 'r') as updateHystory:
		uhIni = updateHystory.read()
		uhExist = 1
except:
	print('File "updHyst.ini" not found')

def send_message_to_user(message):
	user_id = int(event.user_id)
	random_id = event.random_id
	
	vk.messages.send(
		random_id=random_id,
		user_id=user_id,
		message=message
	)

print('Done')

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
		if event.text == 'Дарки, расскажи о себе' or event.text == 'Дарки расскажи о себе': #Если написали заданную фразу
			if event.from_user: #Если написали в ЛС
				if cvExist == 1:
					with open(pathCV) as fileCV:
						curVer = fileCV.read()
					send_message_to_user(curVer)
				else:
					send_message_to_user('К сожалению мне не удалось найти файл с помощью которого я бы с радостью рассказала вам о себе')
		elif event.text == 'Привет, Дарки' or event.text == 'Преет, Дарки' or event.text == 'Привет Дарки' or event.text == 'Преет Дарки' or event.text == 'Прувет Дарки' or event.text == 'Прувет, Дарки' or event.text == 'Здрасть, Дарки' or event.text == 'Здрасть Дарки' or event.text == 'Здравствуй Дарки' or event.text == 'Здрастете Дарки' or event.text == 'Здравствуй, Дарки' or event.text == 'Здрастете, Дарки' or event.text == 'Привки, Дарки' or event.text == 'Привки Дарки' or event.text == 'Ку Дарки' or event.text == 'Ку, Дарки' or event.text == 'Куку Дарки' or event.text == 'Куку, Дарки' or event.text == 'Здравствуйте Дарки' or event.text == 'Здравствуйте, Дарки' or event.text == 'Преть Дарки' or event.text == 'Преть, Дарки':
			if event.from_user:
				send_message_to_user('Преть')
		elif event.text == 'Дарки, история обновлений' or event.text == 'Дарки история обновлений':
			if event.from_user:
				if uhExist == 1:
					with open(pathUH) as fileUH:
						updHyst = fileUH.read()
					send_message_to_user(updHyst)
				else:
					send_message_to_user('К сожалению мне не удалось найти файл в котором содержалась история обновлений')
		elif event.text == 'Как дела, Дарки?' or event.text == 'Как делишки, Дарки?' or event.text == 'Как дела Дарки?' or event.text == 'Как делишки Дарки?':
			if event.from_user:
				send_message_to_user('У меня не может быть всё плохо пока я работаю :D')