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

rpPath = '/storage/sdcard0/DarkyBot/rpCmds'
nickPath = '/storage/sdcard0/DarkyBot/nicknames'
try:
	os.mkdir(rpPath)
except:
	pass
try:
	os.mkdir(nickPath)
except:
	pass

i = 0
outMess = ''
pathMess = '/storage/sdcard0/DarkyBot/mess'
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
		rpComm1 = rpComm1.lower()
		try:
			with open(rpPath + '/' + str(rpId) + '/' + rpComm1 + '.ini') as rpRead:
				rpAct = rpRead.read()
				rpRead.close()
			rpFrom = event.obj.message['from_id']
			try:
				with open(nickPath + '/' + str(rpId) + '/' + str(rpFrom) + '.ini') as nicknameFromUser:
					nickFrUsr = nicknameFromUser.read()
					nicknameFromUser.close()
				nickFrUsr = nickFrUsr.split('-')
				nickFrUsr = nickFrUsr[1]
				nickFromUser = 1
			except:
				pass
			chatMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
			n = 0
			while not chatMembers['profiles'][n]['id'] == rpFrom:
				n = n + 1
			if nickFromUser == 0:
				rpFromUser = '[id' + str(rpFrom) + '|' + chatMembers['profiles'][n]['first_name'] + ' ' + chatMembers['profiles'][n]['last_name'] + ']'
			if nickFromUser == 1:
				rpFromUser = '[id' + str(rpFrom) + '|' + nickFrUsr + ']'
			rpAct = rpAct.lstrip("['")
			rpAct = rpAct.rstrip("']")
			rpAct = rpAct.split("', '")
			if chatMembers['profiles'][n]['sex'] == 1:
				rpAct = rpAct[1]
			if chatMembers['profiles'][n]['sex'] == 2:
				rpAct = rpAct[0]
			rpTo = rpComm[1]
			try:
				rpTo = rpTo.lstrip('[id0123456789')
				rpTo = rpTo.lstrip('|@')
				rpTo = rpTo.rstrip(']')
				n = 0
				while not chatMembers['profiles'][n]['screen_name'] == rpTo:
					n = n + 1
				try:
					with open(nickPath + '/' + str(rpId) + '/' + str(chatMembers['profiles'][n]['id']) + '.ini') as userNick:
						userNickname = userNick.read()
						userNick.close()
					userNickname = userNickname.split('-')
					userNickname = userNickname[1]
					rpToUser1 = '[' + rpTo + '|' + userNickname + ']'
					nickToUser = 1
				except:
					pass
				try:
					rpToUser0 = '[' + rpTo + '|' + chatMembers['profiles'][n]['first_name'] + ' ' + chatMembers['profiles'][n]['last_name'] + ']'
				except:
					pass
			except:
				pass
			try:
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
								print(nrp)
						except:
							n = n + 1
							pass
				except:
					if nickUser == 0:
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
    
def init_message_from_chat(message):#определение сообщения из беседы
	global i
	global outMess
	roleplayCommands(event.obj.message['text'])
	if message == 'Дарки, позови всех' or message == 'Дарки позови всех':
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
		try:
			with open(rpPath + '/' + str(rpId) + '/' + rpNew + '.ini', 'a') as rpNewComm:
				rpNewComm.close()
			send_message_to_chat('Команда создана')
		except:
			send_message_to_chat('Не удалось создать команду')
	elif message.startswith('Дарки, удали рп команду') or message.startswith('Дарки удали рп команду'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		if message.startswith('Дарки, удали'):
			rpDel = message.lstrip('Дарки, ')
		if message.startswith('Дарки удали'):
			rpDel = message.lstrip('Дарки ')
		rpDel = rpDel.lstrip('удали ')
		rpDel = rpDel.lstrip('рп ')
		rpDel = rpDel.lstrip('команду')
		rpDel = rpDel.lstrip(' ')
		roDel = rpDel.lower()
		try:
			os.remove(rpPath + '/' + str(rpId) + '/' + rpDel + '.ini')
			send_message_to_chat('Команда удалена')
		except:
			send_message_to_chat('Команда не удалена, возможно вы ошиблись в её названии')
	elif message.startswith('Дарки, установи рп действие') or message.startswith('Дарки установи рп действие'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
					send_message_to_chat('Запрос должен выглядеть так: "Дарки, установи рп действие <название команды>, <действие для этой команды вида "укусил-укусила">"')
				try:
					with open(rpPath + '/' + str(rpId) + '/' + rpComm + '.ini', 'w') as rpActionComm:
						rpActionComm.write(str(rpAction))
						rpActionComm.close()
					send_message_to_chat('Действие установлено')
				except:
					send_message_to_chat('Не удалось установить действие для команды, возможно её не существует')
			else:
				send_message_to_chat('Запрос должен выглядеть так: "Дарки, установи рп действие <название команды>, <действие для этой команды вида "укусил-укусила">"')
		except:
			send_message_to_chat('Действие не установлено')
	elif message.startswith("Дарки, установи мой ник на") or message.startswith("Дарки, установи мой ник на"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
			newNickOut = '[id' + usernameId + '|Ваш] никнейм теперь - ' + nicknameNew
			send_message_to_chat(newNickOut)
		except:
			pass
	elif message.startswith("Дарки, удали мой никнейм") or message.startswith('Дарки удали мой никнейм'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		try:
			with open(nickPath + '/' + str(rpId) + '/' + str(event.obj.message['from_id']) + '.ini') as userIdFromNick:
				nickId = userIdFromNick.read()
				userIdFromNick.close()
			nickId = nickId.split('-')
			nickId = nickId[0]
			if nickId == str(event.obj.message['from_id']):
				os.remove(nickPath + '/' + str(rpId) + '/' + str(event.obj.message['from_id']) + '.ini')
				send_message_to_chat('Никнейм удалён')
		except:
			send_message_to_chat('Не удалось удалить, возможно вы ошиблись при написании никнейма')
	elif message.startswith('Дарки, перечисли рп команды') or message.startswith('Дарки перечисли рп команды'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		rpCommands = os.listdir(rpPath + '/' + str(rpId))
		rpCommandsLen = len(rpCommands)
		rpCommandsOut = ''
		currCommNum = 1
		currComm = 0
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
	elif message.startswith("Дарки, перечисли никнеймы") or message.startswith('Дарки перечисли никнеймы'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		nicknames = os.listdir(nickPath + '/' + str(rpId))
		nicknamesLen = len(nicknames)
		nicknamesOut = ''
		currNickNum = 1
		currNick = 0
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
	elif message.startswith('Дарки, команды управления рп командами') or message.startswith('Дарки команды управления рп командами'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Все доступные на данный момент команды, управляющие ролевыми командами:\n1. Дарки, создай рп команду <название>\n2. Дарки, удали рп команду <название>\n3. Дарки, установи рп действие')
	elif message.startswith('Привет, Дарки') or message.startswith('Преет, Дарки') or message.startswith('Преет Дарки') or message.startswith('Привет Дарки') or message.startswith('Привки, Дарки') or message.startswith('Здрасте, Дарки') or message.startswith('Здравствуй, Дарки') or message.startswith('Здравствуйте, Дарки') or message.startswith('Преть, Дарки') or message.startswith('Привки Дарки') or message.startswith('Здрасте Дарки') or message.startswith('Здравствуй Дарки') or message.startswith('Здравствуйте Дарки') or message.startswith('Преть Дарки') or message.startswith('Здрастете, Дарки') or message.startswith('Здрастете Дарки') or message.startswith('Ку Дарки') or message.startswith('Ку, Дарки') or message.startswith('Куку Дарки') or message.startswith('Куку, Дарки') or message.startswith('Прувет, Дарки') or message.startswith('Прувет Дарки'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		hiMessage = ['Преть', 'Привет']
		hiRand = random.randint(0, len(hiMessage))
		send_message_to_chat(hiMessage[hiRand - 1])
	elif "Спокойной ночи" in message or "спокойной ночи" in message or "споки" in message or "Споки" in message or "споки" in message or "Споки" in message:
		print('chat:', event.chat_id, ':', message)
		sleepMessage = ['Споки', 'Добрых снов', 'Спокойной', 'Спокойной ночи', 'Ночки', 'Сладких снов']
		sleepRand = random.randint(0, len(sleepMessage))
		send_message_to_chat(sleepMessage[sleepRand - 1]
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
	elif message.startswith('Дарки, помощь') or message.startswith('Дарки помощь'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Раз вы вызвали помощь, значит вам нужна помощь, а значит я могу помочь^^\nЕсли вы хотите узнать кто я - введите "Дарки, расскажи о себе"\nЕсли вы хотите узнать мои команды - введите "Дарки, команды"')
	elif message.startswith('Дарки, команды') or message.startswith('Дарки команды'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Доступные на данный момент команды:\n1. Привет, Дарки\n2. Дарки, расскажи о себе\n3. Дарки, история обновлений\n4. Дарки, помощь\n5. Дарки, выбери <варианты через или>\n6. Дарки, вероятность <предложение>\n7. Дарки, попытка <действие>\n8. Дарки, голос\n9. Дарки, сброс собранных данных\n10. Дарки, команды управления рп командами\n11. Дарки, установи мой ник на <никнейм>\n12. Дарки, удали мой никнейм\n13. Дарки, перечисли рп команды\n14. Дарки, перечисли никнеймы\n15. Спокойной ночи')
	elif "test" in event.obj.message['text'] or "тест" in event.obj.message['text'] or "Тест" in event.obj.message['text'] or "Test" in event.obj.message['text']:
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		if "test2310" in event.obj.message['text'] or "тест2310" in event.obj.message['text'] or "Тест2310" in event.obj.message['text'] or "Test2310" in event.obj.message['text']:
			send_message_to_chat("Вы получили секрет! Ссылка на тестовый сервер")
			send_message_to_chat("Вот ваша ссылка: https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp")
		else:
			send_message_to_chat('Вы почти у цели, введите вдобавок к "тест/test" дату рождения моего создателя в формате ДДММ\nПример:тест0206')
	elif message.startswith("Дарки выбери") or message.startswith("Дарки, выбери"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
		send_message_to_chat('Я выбираю ' + chooseResult)
	elif message.startswith('Дарки, вероятность') or message.startswith('Дарки вероятность'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		probabilityMess = event.obj.message['text']
		if message.startswith('Дарки, вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки, ')
		if message.startswith('Дарки вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки ')
		probabilityStr = probabilityStr.lstrip('вероятность')
		probabilityRandom = random.randint(0, 100)
		probabilityResult = str(probabilityRandom) + '%'
		send_message_to_chat('Вероятность того, что' + probabilityStr + ' составляет ' + probabilityResult)
	elif message.startswith('Дарки, попытка') or message.startswith('Дарки попытка'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		tryMess = event.obj.message['text']
		if message.startswith('Дарки, попытка'):
			tryStr = tryMess.lstrip('Дарки, ')
		if message.startswith('Дарки попытка'):
			tryStr = tryMess.lstrip('Дарки ')
		tryStr = tryStr.lstrip('попытка')
		tryRandom = random.randint(0, 1)
		if tryRandom == 0:
			send_message_to_chat('Попытка' + tryStr + ' вышла неудачной')
		if tryRandom == 1:
			send_message_to_chat('Попытка' + tryStr + ' вышла удачной')
	elif message.startswith('Дарки запустись') or message.startswith('Дарки. запустись') or message.startswith('Дарки перезапустись') or message.startswith('Дарки. перезапустись') or message.startswith('Дарки выключись') or message.startswith('Дарки. выключись') or message.startswith('Дарки проверь наличие своих файлов') or message.startswith('Дарки. проверь наличие своих файлов') or message.startswith('Дарки обновись') or message.startswith('Дарки. обновись')  or message.startswith('Дарки обнови главный скрипт') or message.startswith('Дарки. обнови главный скрипт'):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Данная команда не работает в беседе')
	elif message.startswith("Дарки, голос") or message.startswith("Дарки голос"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Очищаю собранные данные об этом диалоге...')
		with open(pathMess + '/' + str(event.chat_id) + '.ini', 'w') as messEarse:
			messEarse.close()
		send_message_to_chat('Данные очищены')
	elif message.startswith("Дарки, размер собранных данных") or message.startswith("Дарки размер собранных данных"):
		print('chat:', event.chat_id, ':', event.obj.message['text'])
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
		print('chat:', event.chat_id, ':', event.obj.message['text'])
		send_message_to_chat('Обидно ;с')

print('done')
while True:
	try:
		for event in botlongpoll.listen(): #своеобразное прослушивание новых сообщений
			if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
				messageText = event.obj.message['text']
				rpId = event.chat_id
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
	except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
        requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		pass
