print('importing "get_random_id"...')
from vk_api.utils import get_random_id

print('importing "vk_api"...')
import vk_api

print('importing "os"...')
import os

print('importing "VkBotLongPoll" and "VkBotEventType"...')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

print('authorization...')
group_id = 192784148
vk_session = vk_api.VkApi(token='ea6aac611a3593e5d0aa74e1bf58ea9a0421203c85bcc1528cd259cb5a287a92cfb2d12f059f349781836')
botlongpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

pathUpdHyst = os.path.abspath('updHyst.ini')

def send_message_to_chat(message):#функция отвечающая за отправку сообщений в беседу
	random_id = get_random_id(),
	chat_id = int(event.chat_id)

	vk.messages.send(
		random_id=random_id,
		chat_id=chat_id,
		message=message
	)
    
def init_message_from_chat(message):#определение сообщения из беседы
	if message.startswith('Привет, Дарки') or message.startswith('Преет, Дарки') or message.startswith('Преет Дарки') or message.startswith('Привет Дарки') or message.startswith('Привки, Дарки') or message.startswith('Здрасте, Дарки') or message.startswith('Здравствуй, Дарки') or message.startswith('Здравствуйте, Дарки') or message.startswith('Преть, Дарки') or message.startswith('Привки Дарки') or message.startswith('Здрасте Дарки') or message.startswith('Здравствуй Дарки') or message.startswith('Здравствуйте Дарки') or message.startswith('Преть Дарки') or message.startswith('Здрастете, Дарки') or message.startswith('Здрастете Дарки') or message.startswith('Ку Дарки') or message.startswith('Ку, Дарки') or message.startswith('Куку Дарки') or message.startswith('Куку, Дарки') or message.startswith('Прувет, Дарки') or message.startswith('Прувет Дарки'):
		send_message_to_chat('Преть')
	elif message.startswith('Как дела, Дарки?') or message.startswith('Как дела Дарки?') or message.startswith('Как делишки, Дарки?') or message.startswith('Как делишки Дарки?'):
		send_message_to_chat('У меня не может быть всё плохо пока я работаю :D')
	elif message.startswith('Дарки, расскажи о себе') or message.startswith('Дарки расскажи о себе'):
		send_message_to_chat('Я - Дарки-бот v:1.3.8\nНа данный момент имею очень малый функционал, но меня стараются совершенствовать и обновлять каждый день')
	elif message.startswith('Дарки, история обновлений') or message.startswith('Дарки история обновлений'):
		with open(pathUpdHyst) as file:
			updHyst = file.read()
		send_message_to_chat(updHyst)

print('done')
for event in botlongpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
		init_message_from_chat(event.obj.message['text'])
