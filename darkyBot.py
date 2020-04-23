print('importing modules...')
from vk_api.utils import get_random_id
import vk_api
import requests
import os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from accessToken import accessToken
import random
import fnmatch

print('authorization...')
group_id = 192784148
vk_session = vk_api.VkApi(token=accessToken)
botlongpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

i = 0
outMess = ''
	
print('loading functions...')

os.chdir('/storage/emulated/0')

neededFoundedFiles = []
neededFoundedDirs = []

def checkFilesExist(pattern, pathToFile):
	global neededFoundedFiles
	foundedFiles = []
	for root, dirs, files in os.walk(pathToFile):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				foundedFiles.append(os.path.join(root, name))
	n = 0
	neededFoundedFiles = []
	while not n == len(foundedFiles):
		if foundedFiles[n].endswith('/DarkyBot/' + pattern.lstrip('*')):
			neededFoundedFiles.append(foundedFiles[n])
		n = n + 1
		
def checkDirsExist(pattern, pathToDir):
	global neededFoundedDirs
	foundedDirs = []
	for root, dirs, files in os.walk(pathToDir):
		for name in dirs:
			if fnmatch.fnmatch(name, pattern):
				foundedDirs.append(os.path.join(root, name))
	n = 0
	neededFoundedDirs = []
	while not n == len(foundedDirs):
		if foundedDirs[n].endswith('/DarkyBot/' + pattern.lstrip('*')):
			neededFoundedDirs.append(foundedDirs[n])
		n = n + 1

def send_message_to_chat(message): #функция отвечающая за отправку сообщений в беседу
	vk.messages.send(chat_id = event.chat_id, random_id = get_random_id(), message = message)

def send_message_to_user(message): #функция отвечающая за отправку сообщений пользователю
	vk.messages.send(user_id = event.obj.message['from_id'], random_id = get_random_id(), message = message)

def roleplayCommands(message):
	nickFromUser = 0
	nickToUser = 0
	nickUser = 0
	try:
		rpComm = message.split(' ')
		try:
			rpComm = rpComm.split(',')
		except:
			pass
		rpComm1 = rpComm[0]
		rpComm1 = rpComm1.lower() #определение ролевой команды
		try:
			with open(rpPath + '/' + str(rpId) + '/' + rpComm1 + '.ini') as rpRead: #поиск ролевой команды среди созданных
				rpAct = rpRead.read()
				rpRead.close()
			rpFrom = event.obj.message['from_id']
			try:
				with open(nickPath + '/' + str(rpId) + '/' + str(rpFrom) + '.ini') as nicknameFromUser: #поиск никнейма пользователя который использовал команду по айди
					nickFrUsr = nicknameFromUser.read()
					nicknameFromUser.close()
				nickFrUsr = nickFrUsr.split('-')
				nickFrUsr = nickFrUsr[1]
				nickFromUser = 1
			except:
				pass
			chatMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
			n = 0
			while not chatMembers['profiles'][n]['id'] == rpFrom: #определение пользователя который использовал команду среди всех участников беседы
				n = n + 1
			if nickFromUser == 0: #если никнейм не был обнаружен то пишется Имя Фамилия взятые со страницы пользователя
				rpFromUser = '[id' + str(rpFrom) + '|' + chatMembers['profiles'][n]['first_name'] + ' ' + chatMembers['profiles'][n]['last_name'] + ']'
			if nickFromUser == 1: #если же никнейм был обнаружен, выводится никнейм
				rpFromUser = '[id' + str(rpFrom) + '|' + nickFrUsr + ']'
			rpAct = rpAct.lstrip("['")
			rpAct = rpAct.rstrip("']")
			rpAct = rpAct.split("', '")
			if chatMembers['profiles'][n]['sex'] == 1: #определение пола пользователя использовавший команду и исходя от него - определяется род действия
				rpAct = rpAct[1]
			if chatMembers['profiles'][n]['sex'] == 2:
				rpAct = rpAct[0]
			rpTo = rpComm[1] #кому назначена команда в виде упоминания
			try:
				rpTo = rpTo.lstrip('[id0123456789') #удаление лишнего
				rpTo = rpTo.lstrip('|@')
				rpTo = rpTo.rstrip(']')
				n = 0
				while not chatMembers['profiles'][n]['screen_name'] == rpTo: #поиск этого человека среди участников беседы
					n = n + 1
				try:
					with open(nickPath + '/' + str(rpId) + '/' + str(chatMembers['profiles'][n]['id']) + '.ini') as userNick: #поиск никнейма среди сохраненных и в случае удачи его вывод
						userNickname = userNick.read()
						userNick.close()
					userNickname = userNickname.split('-')
					userNickname = userNickname[1]
					rpToUser1 = '[' + rpTo + '|' + userNickname + ']'
					nickToUser = 1
				except:
					pass
				try: #если никнейма не обнаружено - указание Имени Фамилии со страницы человека
					rpToUser0 = '[' + rpTo + '|' + chatMembers['profiles'][n]['first_name'] + ' ' + chatMembers['profiles'][n]['last_name'] + ']'
				except:
					pass
			except:
				pass
			try: #определение был ли указан никнейм в команде и существует ли человек с таким никнеймом
				n = 0
				try:
					while not n == chatMembers['count'] and nickUser == 0:
						uid = str(chatMembers['profiles'][n]['id'])
						try:
							with open(nickPath + '/' + str(rpId) + '/' + uid + '.ini') as userNick:
								userNickname = userNick.read()
								userNick.close()
								userNickname = userNickname.split('-')
							userNickname = userNickname[1]
							if userNickname == rpTo:
								rpToUser = '[id' + str(uid) + '|' + userNickname + ']'
								nickUser = 1
								print(nrp)
							else:
								n = n + 1
								print(nrp) #не знаю как и почему, но с вызовом исключения всё работает
						except:
							n = n + 1
							pass
				except:
					if nickUser == 0: #если никнейм не найден, говорим об этом
						send_message_to_chat('В беседе нет человека с таким никнеймом')
				if not n == 0 and nickUser == 0 and nickToUser == 0:
					send_mess_to_chat('В беседе нет человека с таким никнеймом')
				else:
					pass
			except:
				pass
			if nickToUser == 0 and nickUser == 0:
				rpToUser = str(rpToUser0)
			if nickToUser == 1 and nickUser == 0:
				rpToUser = str(rpToUser1)
			else:
				pass
			rpOut = rpFromUser + ' ' + rpAct + ' ' + rpToUser
			send_message_to_chat(rpOut)
		except:
			pass
	except:
		pass
		
def distortMessage(distortMess):
	distortMessageOut = ''
	distortMessageInt = 0
	distortMessageSymbols = ['█', '▒', '□', '?', '⊠', '[]']
	distortMessageLen = len(distortMess)
	while not distortMessageInt == distortMessageLen:
		distortRandomSymbol = random.randint(1, 20)
		if distortRandomSymbol < 7:
			distortMessageOut = distortMessageOut + distortMessageSymbols[distortRandomSymbol - 1]
			distortMessageInt = distortMessageInt + 1
		else:
			distortMessageOut = distortMessageOut + distortMess[distortMessageInt]
			distortMessageInt = distortMessageInt + 1
	send_message_to_chat(distortMessageOut)
    
def init_message_from_chat(message): #определение сообщения из беседы
	global i
	global outMess
	roleplayCommands(event.obj.message['text'])
	if message == 'Дарки, позови всех' or message == 'Дарки позови всех':
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		out = ''
		chatMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
		countOfMembers = chatMembers['count']
		out = 'Всего участников: ' + str(countOfMembers) + '\n'
		n = 0
		curProf = 1
		while n < countOfMembers:
			nou = 0
			try:
				domain = chatMembers['profiles'][n]['screen_name']
				first_name = chatMembers['profiles'][n]['first_name']
				last_name = chatMembers['profiles'][n]['last_name']
				currProf = str(curProf) + '. [' + str(domain) + '|' + str(first_name) + ' ' + str(last_name) + ']' + '\n'
			except:
				n = 0
				break
			out = out + currProf
			curProf = curProf + 1
			n = n + 1
		while n < countOfMembers:
			try:
				name = chatMembers ['groups'][n]['name']
				currGroup = str(curProf) + '. ' + str(name) + '\n'
			except:
				break
			out = out + currGroup
			curProf = curProf + 1
			n = n + 1
		send_message_to_chat(out)
	elif message.startswith('Дарки, создай рп команду') or message.startswith('Дарки создай рп команду'):
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		allMembersOfChat = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
		accssRP = 0
		while not event.obj.message['from_id'] == allMembersOfChat['items'][accssRP]['member_id']:
			accssRP = accssRP + 1
		try:
			userIsAdmin = allMembersOfChat['items'][accssRP]['is_admin']
		except:
			userIsAdmin = False
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
			if message.startswith('Дарки, создай'):
				rpNew = message.lstrip('Дарки, ')
			if message.startswith('Дарки создай'):
				rpNew = message.lstrip('Дарки ')
			rpNew = rpNew.lstrip('создай ')
			rpNew = rpNew.lstrip('рп ')
			rpNew = rpNew.lstrip('команду')
			rpNew = rpNew.lstrip(' ')
			rpNew = rpNew.lower()
			try:
				os.mkdir(rpPath + '/' + str(rpId))
			except:
				pass
			if not rpNew == '':
				try:
					with open(rpPath + '/' + str(rpId) + '/' + rpNew + '.ini', 'a') as rpNewComm:
						rpNewComm.close()
					send_message_to_chat('✅Команда создана')
				except:
					send_message_to_chat('❌Не удалось создать команду')
			else:
				send_message_to_chat('⚠️Невозможно создать команду с пустым названием')
		else:
			send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором')
	elif message.startswith('Дарки, удали рп команду') or message.startswith('Дарки удали рп команду'):
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		allMembersOfChat = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
		accssRP = 0
		while not event.obj.message['from_id'] == allMembersOfChat['items'][accssRP]['member_id']:
			accssRP = accssRP + 1
		try:
			userIsAdmin = allMembersOfChat['items'][accssRP]['is_admin']
		except:
			userIsAdmin = False
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
			if message.startswith('Дарки, удали'):
				rpDel = message.lstrip('Дарки, ')
			if message.startswith('Дарки удали'):
				rpDel = message.lstrip('Дарки ')
			rpDel = rpDel.lstrip('удали ')
			rpDel = rpDel.lstrip('рп ')
			rpDel = rpDel.lstrip('команду')
			rpDel = rpDel.lstrip(' ')
			rpDel = rpDel.lower()
			if not rpDel == '':
				try:
					os.remove(rpPath + '/' + str(rpId) + '/' + rpDel + '.ini')
					send_message_to_chat('✅Команда удалена')
				except:
					send_message_to_chat('⚠️Команда не удалена, возможно вы ошиблись в её названии')
			else:
				send_message_to_chat('⚠️Невозможно удалить команду с пустым названием')
		else:
			send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором')
	elif message.startswith('Дарки, установи рп действие') or message.startswith('Дарки установи рп действие'):
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		allMembersOfChat = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
		accssRP = 0
		while not event.obj.message['from_id'] == allMembersOfChat['items'][accssRP]['member_id']:
			accssRP = accssRP + 1
		try:
			userIsAdmin = allMembersOfChat['items'][accssRP]['is_admin']
		except:
			userIsAdmin = False
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
			if message.startswith('Дарки, установи'):
				rpAction = message.lstrip('Дарки, ')
			if message.startswith('Дарки установи'):
				rpAction = message.lstrip('Дарки ')
			rpAction = rpAction.lstrip('установи ')
			rpAction = rpAction.lstrip('рп ')
			rpAction = rpAction.lstrip('действие')
			rpAction = rpAction.lstrip(' ')
			try:
				try:
					rpAction = rpAction.split(', ')
				except:
					pass
				if len(rpAction) < 3 and len(rpAction) > 1:
					rpComm = rpAction[0]
					rpComm = rpComm.lower()
					rpAction = rpAction[1]
					rpAction = rpAction.lower()
					try:
						rpAction = rpAction.split('-')
					except:
						send_message_to_chat('⚠️Запрос должен выглядеть так: "Дарки, установи рп действие <название команды>, <действие для этой команды вида "укусил-укусила">"')
					try:
						with open(rpPath + '/' + str(rpId) + '/' + rpComm + '.ini', 'w') as rpActionComm:
							rpActionComm.write(str(rpAction))
							rpActionComm.close()
						send_message_to_chat('✅Действие установлено')
					except:
						send_message_to_chat('❌Не удалось установить действие для команды, возможно её не существует')
				else:
					send_message_to_chat('⚠️Запрос должен выглядеть так: "Дарки, установи рп действие <название команды>, <действие для этой команды вида "укусил-укусила">"')
			except:
				send_message_to_chat('❌Действие не установлено')
		else:
			send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором')
	elif message.startswith("Дарки, установи мой ник на") or message.startswith("Дарки установи мой ник на"):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки, установи'):
			nicknameNew = message.lstrip('Дарки, ')
		if message.startswith('Дарки установи'):
			nicknameNew = message.lstrip('Дарки ')
		nicknameNew = nicknameNew.lstrip('установи ')
		nicknameNew = nicknameNew.lstrip('мой ')
		nicknameNew = nicknameNew.lstrip('ник ')
		nicknameNew = nicknameNew.lstrip('на')
		nicknameNew = nicknameNew.lstrip(' ')
		print(nicknameNew)
		try:
			os.mkdir(nickPath + '/' + str(rpId))
		except:
			pass
		try:
			with open(nickPath + '/' + str(rpId) + '/' + str(event.obj.message['from_id']) + '.ini', 'a') as newUserNick:
				usernameId = str(event.obj.message['from_id'])
				newUserNick.write(usernameId + '-' + nicknameNew)
				newUserNick.close()
			newNickOut = '✅[id' + usernameId + '|Ваш] никнейм теперь - ' + nicknameNew
			send_message_to_chat(newNickOut)
		except:
			pass
	elif message.startswith("Дарки, удали мой никнейм") or message.startswith('Дарки удали мой никнейм'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		try:
			with open(nickPath + '/' + str(rpId) + '/' + str(event.obj.message['from_id']) + '.ini') as userIdFromNick:
				nickId = userIdFromNick.read()
				userIdFromNick.close()
			nickId = nickId.split('-')
			nickId = nickId[0]
			if nickId == str(event.obj.message['from_id']):
				os.remove(nickPath + '/' + str(rpId) + '/' + str(event.obj.message['from_id']) + '.ini')
				send_message_to_chat('✅Никнейм удалён')
		except:
			send_message_to_chat('❌Не удалось удалить, возможно вы ошиблись при написании никнейма')
	elif message.startswith('Дарки, перечисли рп команды') or message.startswith('Дарки перечисли рп команды'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		rpCommands = os.listdir(rpPath + '/' + str(rpId))
		rpCommandsLen = len(rpCommands)
		rpCommandsOut = ''
		currCommNum = 1
		currComm = 0
		if rpCommandsLen > 0:
			while currComm < rpCommandsLen:
				currCommandName = rpCommands[currComm]
				currCommandName = currCommandName.rstrip('ini')
				currCommandName = currCommandName.rstrip('.')
				currCommandName = currCommandName.capitalize()
				rpCommandsOut = rpCommandsOut + '\n' + str(currCommNum) + '. ' + currCommandName
				currComm = currComm + 1
				currCommNum = currCommNum + 1
			allRPCommands = 'РП-Команды:' + rpCommandsOut
			send_message_to_chat(allRPCommands)
		else:
			send_message_to_chat('⚠️В этой беседе пока что нет рп команд')
	elif message.startswith("Дарки, перечисли никнеймы") or message.startswith('Дарки перечисли никнеймы'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		nicknames = os.listdir(nickPath + '/' + str(rpId))
		nicknamesLen = len(nicknames)
		nicknamesOut = ''
		currNickNum = 1
		currNick = 0
		if nicknamesLen > 0:
			while currNick < nicknamesLen:
				currNickname = nicknames[currNick]
				currNickname = currNickname.rstrip('ini')
				currNickname = currNickname.rstrip('.')
				with open(nickPath + '/' + str(rpId) + '/' + currNickname + '.ini') as currNickId:
					currNickContent = currNickId.read()
					currNickId.close()
				currNickContent = currNickContent.split('-')
				currNickUserId = currNickContent[0]
				currNickNameId = currNickContent[1]
				nicknamesOut = nicknamesOut + '\n' + str(currNickNum) + '. [id' + currNickUserId + '|' + currNickNameId + ']'
				currNick = currNick + 1
				currNickNum = currNickNum + 1
			allNicknames = 'Все никнеймы:' + nicknamesOut
			send_message_to_chat(allNicknames)
		else:
			send_message_to_chat('⚠️В этой беседе нет сохранённых никнеймов')
	elif message.startswith('Дарки, команды управления рп командами') or message.startswith('Дарки команды управления рп командами'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Все доступные на данный момент команды, управляющие ролевыми командами:\n1. Дарки, создай рп команду <название>\n2. Дарки, удали рп команду <название>\n3. Дарки, установи рп действие')
	elif message.startswith('Привет, Дарки') or message.startswith('Преет, Дарки') or message.startswith('Преет Дарки') or message.startswith('Привет Дарки') or message.startswith('Привки, Дарки') or message.startswith('Здрасте, Дарки') or message.startswith('Здравствуй, Дарки') or message.startswith('Здравствуйте, Дарки') or message.startswith('Преть, Дарки') or message.startswith('Привки Дарки') or message.startswith('Здрасте Дарки') or message.startswith('Здравствуй Дарки') or message.startswith('Здравствуйте Дарки') or message.startswith('Преть Дарки') or message.startswith('Здрастете, Дарки') or message.startswith('Здрастете Дарки') or message.startswith('Ку Дарки') or message.startswith('Ку, Дарки') or message.startswith('Куку Дарки') or message.startswith('Куку, Дарки') or message.startswith('Прувет, Дарки') or message.startswith('Прувет Дарки'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		hiMessage = ['Преть', 'Привет']
		hiRand = random.randint(0, len(hiMessage))
		send_message_to_chat(hiMessage[hiRand - 1])
	elif "Спокойной ночи" in message or "спокойной ночи" in message or "споки" in message or "Споки" in message or "споке" in message or "Споке" in message:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		sleepMessage = ['Споки', 'Добрых снов', 'Спокойной', 'Спокойной ночи', 'Ночки', 'Сладких снов']
		sleepRand = random.randint(0, len(sleepMessage))
		send_message_to_chat(sleepMessage[sleepRand - 1])
	elif message.startswith('Дарки, расскажи о себе') or message.startswith('Дарки расскажи о себе'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		with open(pathCV) as file:
			curVer = file.read()
		send_message_to_chat(curVer)
	elif message.startswith('Дарки, история обновлений') or message.startswith('Дарки история обновлений'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		with open(pathUH) as file:
			updHyst = file.read()
		send_message_to_chat(updHyst)
	elif message.startswith('Дарки, помощь') or message.startswith('Дарки помощь'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Раз вы вызвали помощь, значит вам нужна помощь, а значит я могу помочь^^\nЕсли вы хотите узнать кто я - введите "Дарки, расскажи о себе"\nЕсли вы хотите узнать мои команды - введите "Дарки, команды"')
	elif message.startswith('Дарки, команды') or message.startswith('Дарки команды'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Доступные на данный момент команды:\n1. Привет, Дарки\n2. Дарки, расскажи о себе\n3. Дарки, история обновлений\n4. Дарки, помощь\n5. Дарки, выбери <варианты через или>\n6. Дарки, вероятность <предложение>\n7. Дарки, попытка <действие>\n8. Дарки, голос\n9. Дарки, сброс собранных данных\n10. Дарки, команды управления рп командами\n11. Дарки, установи мой ник на <никнейм>\n12. Дарки, удали мой никнейм\n13. Дарки, перечисли рп команды\n14. Дарки, перечисли никнеймы\n15. Спокойной ночи\n16. Дарки, искази текст: <текст>\n17. Дарки, скажи <текст>\n18. Дарки, брось кубик')
	elif "test" in event.obj.message['text'] or "тест" in event.obj.message['text'] or "Тест" in event.obj.message['text'] or "Test" in event.obj.message['text']:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if "test0206" in message or "тест0206" in message or "Тест0206" in message or "Test0206" in message:
			send_message_to_chat('Очень умно. Подумайте лучше')
		if "test2310" in event.obj.message['text'] or "тест2310" in event.obj.message['text'] or "Тест2310" in event.obj.message['text'] or "Test2310" in event.obj.message['text']:
			send_message_to_chat("Вы получили секрет! Ссылка на тестовый сервер")
			send_message_to_chat("Вот ваша ссылка: https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp")
		else:
			send_message_to_chat('Вы почти у цели, введите вдобавок к "тест/test" дату рождения моего создателя в формате ДДММ\nПример:тест0206')
	elif message.startswith("Дарки выбери") or message.startswith("Дарки, выбери"):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		choosingMess = event.obj.message['text']
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
		if chooseListLen > 1:
			send_message_to_chat('Я выбираю ' + chooseResult)
		else:
			send_message_to_chat('⚠️Я не могу выбрать что-либо поскольку мне дали один вариант ответа, либо мне не дали варианты ответа вообще')
	elif message.startswith('Дарки, вероятность') or message.startswith('Дарки вероятность'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		probabilityMess = event.obj.message['text']
		if message.startswith('Дарки, вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки, ')
		if message.startswith('Дарки вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки ')
		probabilityStr = probabilityStr.lstrip('вероятность')
		probabilityRandom = random.randint(0, 100)
		probabilityResult = str(probabilityRandom) + '%'
		if not probabilityStr == '':
			send_message_to_chat('Вероятность того, что' + probabilityStr + ' составляет ' + probabilityResult)
		else:
			send_message_to_chat('⚠️Не могу просчитать вероятность, пожалуйста введите предложение после "Дарки, вероятность"')
	elif message.startswith('Дарки, попытка') or message.startswith('Дарки попытка'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		tryMess = event.obj.message['text']
		if message.startswith('Дарки, попытка'):
			tryStr = tryMess.lstrip('Дарки, ')
		if message.startswith('Дарки попытка'):
			tryStr = tryMess.lstrip('Дарки ')
		tryStr = tryStr.lstrip('попытка')
		tryRandom = random.randint(0, 1)
		if tryRandom == 0 and not tryStr == '':
			send_message_to_chat('❌Попытка' + tryStr + ' вышла неудачной')
		elif tryRandom == 1 and not tryStr == '':
			send_message_to_chat('✅Попытка' + tryStr + ' вышла удачной')
		else:
			send_message_to_chat('Пожалуйста укажите действие, дабы я решила, было ли оно удачным или же наоборот')
	elif message.startswith('Дарки, искази текст: ') or message.startswith('Дарки искази текст: '):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки, '):
			distortMess = message.lstrip('Дарки, ')
		if message.startswith('Дарки '):
			distortMess = message.lstrip('Дарки ')
		distortMess = distortMess.lstrip('искази ')
		distortMess = distortMess.lstrip('текст: ')
		distortMess = list(distortMess)
		distortMessage(distortMess)
	elif message.startswith('Дарки, скажи') or message.startswith('Дарки скажи'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки, '):
			repeatMess = message.lstrip('Дарки, ')
		if message.startswith('Дарки '):
			repeatMess = message.lstrip('Дарки ')
		repeatMess = repeatMess.lstrip('скажи ')
		send_message_to_chat(repeatMess)
	elif message.startswith('Дарки, брось кубик') or message.startswith('Дарки брось кубик'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		diceRandom = random.randint(1, 6)
		send_message_to_chat('🎲На кубике выпало число: ' + str(diceRandom))
	elif message.startswith("Дарки, голос") or message.startswith("Дарки голос"):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		randSendLen = random.randint(2, 15)
		with open(pathMess + '/' + str(event.chat_id) + '.ini') as messRead:
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
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Очищаю собранные данные об этом диалоге...')
		with open(pathMess + '/' + str(event.chat_id) + '.ini', 'w') as messEarse:
			messEarse.close()
		send_message_to_chat('✅Данные очищены')
	elif message.startswith("Дарки, размер собранных данных") or message.startswith("Дарки размер собранных данных"):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		sizePath = pathMess + '/' + str(event.chat_id) + '.ini'
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
		fSize = round(fSize, 2)
		send_message_to_chat('Размер собранных данных об этом диалоге составляет: ' + str(fSize) + ' ' + sizeTypeStr)
	elif "Дурки" in message or "боты тупые" in message.lower() or "боты не имеют мозгов" in message.lower():
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Обидно ;с')
		
print('checking needed files and directories...')

checkFilesExist('*darkyBot.py', os.getcwd())
if len(neededFoundedFiles) < 1:
	print('main directory "DarkyBot" not found')
	print('crashed!')
	raise SystemExit
else:
	mainPathDB = neededFoundedFiles[0]
	mainPathDB = mainPathDB.rstrip('darkyBot.py')
	print(mainPathDB + ' - founded')
checkDirsExist('*mess', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'mess')
		print(mainPathDB + 'mess - created')
		checkDirsExist('*mess', os.getcwd())
		pathMess = neededFoundedDirs[0]
		print(pathMess + ' - founded')
	except:
		pass
else:
	pathMess = neededFoundedDirs[0]
	print(pathMess + ' - founded')
checkDirsExist('*rpCmds', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'rpCmds')
		print(mainPathDB + 'rpCmds - created')
		checkDirsExist('*rpCmds', os.getcwd())
		rpPath = neededFoundedDirs[0]
		print(rpPath + ' - founded')
	except:
		pass
else:
	rpPath = neededFoundedDirs[0]
	print(rpPath + ' - founded')
checkDirsExist('*nicknames', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'nicknames')
		print(mainPathDB + 'nicknames - created')
		checkDirsExist('*nicknames', os.getcwd())
		nickPath = neededFoundedDirs[0]
		print(nickPath + ' - founded')
	except:
		pass
else:
	nickPath = neededFoundedDirs[0]
	print(nickPath + ' - founded')
checkFilesExist('*curVer.ini', os.getcwd())
if not len(neededFoundedFiles) == 0:
	pathCV = neededFoundedFiles[0]
	print(pathCV + ' - founded')
else:
	print('file "curVer.ini" not found!')
checkFilesExist('*updHyst.ini', os.getcwd())
if not len(neededFoundedFiles) == 0:
	pathUH = neededFoundedFiles[0]
	print(pathUH + ' - founded')
else:
	print('file "updHyst.ini" not found!')
checkFilesExist('*adminUsers.ini', os.getcwd())
if not len(neededFoundedFiles) == 0:
	pathAU = neededFoundedFiles[0]
	print(pathAU + ' - founded')
else:
	print('file "adminUsers.ini" not found!')
	
print('files and directories are checked!')

with open(mainPathDB + 'startUp.ini', 'w') as startUpInfo:
	startUpInfo.close()
print('done(v3.0.0)')
while True:
	try:
		for event in botlongpoll.listen(): #своеобразное прослушивание новых сообщений
			if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
				messageText = event.obj.message['text']
				rpId = event.chat_id
				try:
					os.mkdir(rpPath + '/' + str(rpId))
				except:
					pass
				try:
					os.mkdir(nickPath + '/' + str(rpId))
				except:
					pass
				try:
					with open(pathMess + '/' + str(event.chat_id) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				except:
					with open(pathMess + '/' + str(event.chat_id) + '.ini', 'w') as messFile:
						messFile.close()
					with open(pathMess + '/' + str(event.chat_id) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				init_message_from_chat(event.obj.message['text'])
			elif event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
				messageText = event.obj.message['text']
				try:
					with open(pathMess + '/' + str(event.obj.message['from_id']) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				except:
					with open(pathMess + '/' + str(event.obj.message['from_id']) + '.ini', 'w') as messFile:
						messFile.close()
					with open(pathMess + '/' + str(event.obj.message['from_id']) + '.ini', 'a') as messWrite:
						messWrite.write(' ' + messageText)
						messWrite.close()
				init_message_from_user(event.obj.message['text'])
	except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		pass