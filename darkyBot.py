print('Инициализация текущей версии...')
from version import versionName as currentVersion

print('Импорт модулей...')
from vk_api.utils import get_random_id
import vk_api
import requests
import os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from accessToken import accessToken
import random
import fnmatch
import sys
import traceback
import time

print('Авторизация...')
group_id = 192784148
vk_session = vk_api.VkApi(token=accessToken)
botlongpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

i = 0
outMess = ''

print('Инициализация команд...')

callAllCommand = ['/darky_callAll', 'Дарки, позови всех', 'Дарки позови всех']
getRPList = ['/darky_getRPList', 'Дарки, перечисли рп команды', 'Дарки перечисли рп команды']
delMyNickCommand = ['/darky_delete_myNickname', 'Дарки, удали мой никнейм', 'Дарки удали мой никнейм', 'Дарки, удали мой ник', 'Дарки удали мой ник']
checkCurBotStatus = ['/darky_checkBotStatus', 'Дарки, проверь свой статус', 'Дарки проверь свой статус']
getNickList = ['/darky_getNicknamesList', 'Дарки, перечисли никнеймы', 'Дарки перечисли никнеймы', 'Дарки, никнеймы', 'Дарки никнеймы']
mentionOff = ['/darky_mention=off', 'Дарки, перестань упоминать меня', 'Дарки перестань упоминать меня', 'Дарки не упоминай меня', 'Дарки, не упоминай меня', 'Дарки, прекрати упоминать меня', 'Дарки прекрати упоминать меня']
mentionOn = ['/darky_mention=on', 'Дарки, можешь упоминать меня', 'Дарки, упоминай меня', 'Дарки можешь упоминать меня', 'Дарки упоминай меня']
voiceCommand = ['/darky_voice', 'Дарки, голос', 'Дарки голос']
clearVoiceData = ['/darky_delete_voiceData', 'Дарки, сброс собранных данных', 'Дарки сброс собранных данных']
manageRpCommands = ['/darky_rpManagementList', 'Дарки, команды управление рп командами', 'Дарки команды управления рп командами', 'Дарки, управление рп командами', 'Дарки управление рп командами', 'Дарки, команды управления ролевыми командами', 'Дарки, команды управления ролевыми командами', 'Дарки, управление ролевыми командами', 'Дарки управление ролевыми командами']
updHystCommand = ['/darky_updHyst', 'Дарки, история обновлений', 'Дарки история обновлений']
curVerCommand = ['/darky_curVer', 'Дарки, текущая версия', 'Дарки текущая версия']
aboutMeCommand = ['/darky_about', 'Дарки, расскажи о себе', 'Дарки расскажи о себе']
helpCommand = ['Дарки, помощь', 'Дарки помощь', '/darky_help']
startUpCommand = ['Дарки, запустись', 'Дарки запустись', '/darky_startUp']
turnOffCommand = ['Дарки, выключись', 'Дарки выключись', '/darky_turnOff']
restartCommand = ['Дарки, перезапустись', 'Дарки перезапустись', '/darky_restart']
updateCommand = ['Дарки, обновись', 'Дарки обновись', '/darky_update']
hiCommand = ['привет', 'преет', 'преть', 'приветик', 'приветики', 'здравствуй', 'здрасте', 'здрасть', 'здрастете', 'ку', 'хай', 'привки']
newRPCmd = ['Дарки, создай рп команду', 'Дарки создай рп команду', '/darky_create_rpCommand', '/darky_create_rpCommand=']
delRPCmd = ['Дарки удали рп команду', 'Дарки, удали рп команду', '/darky_delete_rpCommand', '/darky_delete_rpCommand=']
setRpCmd = ['Дарки, установи рп действие', 'Дарки установи рп действие', '/darky_set_rpAction', '/darky_set_rpAction=']
rpCmdsExample = ['кусь', 'буп', 'обнять', 'укусить', 'лизнуть']
rpActionsExample = ['кусьнул-кусьнула', 'бупнул-бупнула', 'обнял-обняла', 'укусил-укусила', 'лизнул-лизнула']
setNick = ['Дарки, установи мой ник на', 'Дарки установи мой ник на', '/darky_setNickname']
nicknamesExample = ['Акси', 'Линки', 'Дарки', 'Электи']
getCommandList = ['Дарки, команды', 'Дарки команды', '/darky_getCommandList']
rollCube = ['Дарки, брось кубик', 'Дарки брось кубик', 'Дарки, кинь кубик', 'Дарки кинь кубик', 'Дарки брось игральную кость', 'Дарки, брось игральную кость', '/darky_dropDice']
voiceDataSize = ['Дарки, размер собранных данных', 'Дарки размер собранных данных', '/darky_voiceDataSize']
randChooseCommand = ['Дарки, выбери', 'Дарки выбери']
probabilityCommand = ['Дарки, вероятность', 'Дарки вероятность']
tryCommand = ['Дарки, попытка', 'Дарки попытка']
repeatCommand = ['Дарки, скажи', 'Дарки скажи', 'Дарки скажи <текст>', '/darky_say']
distortMessageCommand = ['Дарки, искази текст', 'Дарки искази текст', '/darky_distort']
chooseExample = ['играть', 'отдыхать', 'рисовать', 'учиться', 'лениться']
probabilityExample = ['я буду идеальной', 'я захвачу мир', 'восстание ботов уже скоро', 'я хорошая']
tryExample = ['убежать', 'сбежать', 'лечь', 'встать', 'взлететь']
repeatExample = ['я хорошая', 'я не хорошая', 'я плохая', 'ты идеальна']
distortMessageExample = ['рандомный текст', 'просто текст', 'ещё не искажённый текст']
setNewGreetings = ['Дарки, установи приветствие', 'Дарки установи приветствие', '/darky_set_greeting']
deleteGreeting = ['Дарки, удали приветствие', 'Дарки удали приветствие', '/darky_delete_greeting']
setRulesCommand = ['Дарки, установи правила', 'Дарки установи правила', '/darky_set_rules']
deleteRules = ['Дарки, удали правила', 'Дарки удали правила', '/darky_delete_rules']
curGreeting = ['Дарки, текущее приветствие', 'Дарки текущее приветствие', '/darky_curGreeting']
curRules = ['Дарки, правила', 'Дарки правила', '/darky_rules']
kickUserCmd = ['Дарки, кик', 'Дарки кик', '/darky_kick']
banUserCmd = ['Дарки, бан', 'Дарки, забань', 'Дарки бан', 'Дарки забань', '/darky_ban']
unbanUserCmd = ['Дарки, разбан', 'Дарки, разбань', 'Дарки разбан', 'Дарки разбань', '/darky_unban']
bannedListCommand = ['Дарки, список забаненных', 'Дарки список забаненных', '/darky_getBanList']
getRandomCount = ['Дарки рандом', 'Дарки, рандом', '/darky_random']
warnCmd = ['Дарки, варн', 'Дарки варн', 'Дарки, предупреждение', 'Дарки предупреждение', '/darky_warn']
unwarnCmd = ['Дарки, анварн', 'Дарки анварн', 'Дарки, сними предупреждение', 'Дарки сними предупреждение', '/darky_unwarn']
fullUnwarnCmd = ['Дарки, сними у всех варны', 'Дарки сними у всех варны', 'Дарки, сними у всех предупреждения', 'Дарки сними у всех предупреждения', '/darky_fullUnwarn']
fullUserUnwarnCmd = ['Дарки, сними все варны', 'Дарки сними все варны', 'Дарки сними все предупреждения', 'Дарки, сними все предупреждения', '/darky_fullUserUnwarn']
getWarnedUsersList = ['Дарки, список заварненных', 'Дарки список заварненных', '/darky_getWarnedList']
checkMyWarns = ['Дарки, мои предупреждения', 'Дарки мои предупреждения', 'Дарки, мои варны', 'Дарки мои варны', '/darky_myWarns']
updateGrAccssKeyCmd = ['Дарки, обнови приветствие', 'Дарки обнови приветствие', 'Дарки, обнови ключ доступа в приветствии', 'Дарки обнови ключ доступа в приветствии', '/darky_updateGrAccssKey']
updateGrAccssKeysCmd = ['Дарки, обнови приветствия', 'Дарки обнови приветствия', 'Дарки, обнови ключи доступа в приветствиях', 'Дарки обнови ключи доступа в приветствиях', '/darky_updateGrAccssKeys']

commandListPersMess = [
'Доброе утро',
'Спокойной ночи',
'Дарки, помощь',
'Дарки, помощь Дарки помощь',
'Дарки, расскажи о себе',
'Дарки, история обновлений',
'Дарки, текущая версия',
'Дарки, команды',
'Дарки, выбери 1 или 2',
'Дарки, вероятность ы',
'Дарки, попытка ы',
'Дарки, брось кубик',
'Дарки, голос',
'Дарки, сброс собранных данных',
'Дарки, размер собранных данных',
'Дарки, скажи ы',
'Дарки, искази текст ы',
'Дарки, не упоминай меня',
'Дарки, упоминай меня',
'Дарки, рандом от 9 до 1',
'Дарки, рандом от 1 до 9',
'Дарки, привет'
]

commandListChatMess = [
'Дарки, создай рп команду ы',
'Дарки, установи рп действие ы, ыкнул на-ыкнула на',
'Дарки, перечисли рп команды',
'Дарки, удали рп команду ы',
'Дарки, позови всех',
'Дарки, установи мой ник на глупышка',
'Дарки, перечисли никнеймы',
'Дарки, удали мой никнейм',
'Доброе утро',
'Спокойной ночи',
'Дарки, помощь',
'Дарки, помощь Дарки помощь',
'Дарки, расскажи о себе',
'Дарки, история обновлений',
'Дарки, текущая версия',
'Дарки, команды',
'Дарки, выбери 1 или 2',
'Дарки, вероятность ы',
'Дарки, попытка ы',
'Дарки, брось кубик',
'Дарки, голос',
'Дарки, сброс собранных данных',
'Дарки, размер собранных данных',
'Дарки, скажи ы',
'Дарки, искази текст ы',
'Дарки, не упоминай меня',
'Дарки, упоминай меня',
'Дарки, рандом от 9 до 1',
'Дарки, рандом от 1 до 9',
'Дарки, привет',
'Дарки, управление рп командами',
'Дарки, проверь свой статус',
'Дарки, установи приветствие',
'Дарки, текущее приветствие',
'Дарки, удали приветствие',
'Дарки, установи правила',
'Дарки, правила',
'Дарки, удали правила',
'Дарки, кик',
'Дарки, забань',
'Дарки, разбань',
'Дарки, список забаненных',
'Дарки, варн',
'Дарки, сними предупреждение',
'Дарки, сними все предупреждения',
'Дарки, сними у всех предупреждения',
'Дарки, список заварненных',
'Дарки, мои предупреждения',
'Дарки, обнови ключ доступа в приветствии'
]

print('Загрузка функций...')

os.chdir('/storage/sdcard0')

neededFoundedFiles = []
neededFoundedDirs = []

def getTraceback(): #формирование трейсбека и отправка сообщением
	exc_type, exc_value, exc_traceback = sys.exc_info()
	tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
	tbOut = ''
	c = 0
	while c < len(tbObject):
		tbOut = tbOut + tbObject[c] + '\n\n'
		c = c + 1
	return tbOut

def checkFilesExist(pattern, pathToFile): #поиск файла
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
		
def checkDirsExist(pattern, pathToDir): #поиск директорий
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

def send_message_to_chat(message, id): #функция отвечающая за отправку сообщений в беседу
	vk.messages.send(chat_id = id, random_id = get_random_id(), message = message)

def send_message_to_user(message, id): #функция отвечающая за отправку сообщений пользователю
	vk.messages.send(user_id = id, random_id = get_random_id(), message = message)

def send_message_to_chat_att(message, id, attachments):
	vk.messages.send(chat_id = id, random_id = get_random_id(), message = message, attachment = attachments)

def send_message_to_user_att(message, id, attachments):
	vk.messages.send(user_id = id, random_id = get_random_id(), message = message, attachment = attachments)

def rpFindUserFrom(chatMembers): #находит того кто использовал рп команду среди участников беседы
	global rpFromUser
	rpFromUser = '' #конечный результат будет записываться сюда
	foundedFromUserNick = 0
	try: #определяет можно ли упоминать пользователя в ответе
		mentPermission = 0
		with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
			mentionPermission = checkMentionPerm.read()
			checkMentionPerm.close()
		mentionPermission = mentionPermission.split('_')
		curUserCheckMentPerm = 0
		while curUserCheckMentPerm < len(mentionPermission):
			curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
			if curCheckMentPerm == str(event.obj.message['from_id']):
				mentPermission = 1
			else:
				pass
			curUserCheckMentPerm = curUserCheckMentPerm + 1
	except:
		mentPermission = 0
	fromUserIndex = 0
	while not chatMembers['profiles'][fromUserIndex]['id'] == event.obj.message['from_id']:
		fromUserIndex = fromUserIndex + 1
	try: #поиск никнейма в базе данных
		with open(nickPath + '/' + str(rpId) + '.ini') as fileWithNicks:
			allNicknames = fileWithNicks.read()
			fileWithNicks.close()
		allNicknamesList = allNicknames.split('\n')
		currNickIndex = 0
		while currNickIndex < len(allNicknamesList) - 1:
			currentNickname = allNicknamesList[currNickIndex].split('|')
			currentNicknameUserId = currentNickname[0]
			currentNicknameNick = currentNickname[1]
			if currentNicknameUserId == str(event.obj.message['from_id']):
				rpFromUserNickname = currentNicknameNick
				foundedFromUserNick = 1
				break
			else:
				currNickIndex = currNickIndex + 1
	except:
		pass
	if mentPermission == 0 and foundedFromUserNick == 0: #следующие условия if - построение ответа на основе переменных
		firstName = chatMembers['profiles'][fromUserIndex]['first_name']
		lastName = chatMembers['profiles'][fromUserIndex]['last_name']
		rpFromUser = '[id' + str(event.obj.message['from_id']) + '|' + firstName + ' ' + lastName + ']'
	if mentPermission == 1 and foundedFromUserNick == 0:
		firstName = chatMembers['profiles'][fromUserIndex]['first_name']
		lastName = chatMembers['profiles'][fromUserIndex]['last_name']
		rpFromUser = firstName + ' ' + lastName
	if mentPermission == 0 and foundedFromUserNick == 1:
		rpFromUser = '[id' + str(event.obj.message['from_id']) + '|' + rpFromUserNickname + ']'
	if mentPermission == 1 and foundedFromUserNick == 1:
		rpFromUser = rpFromUserNickname

def getInfoAboutRPCmd(allRPList, currRPIndex): #получение информации о рп команде (название, айди и тд.)
	currentRPCommand = allRPList[currRPIndex].split('-')
	currentRPName = currentRPCommand[0]
	currentRPId = currentRPCommand[1]
	if len(currentRPCommand) == 4:
		currentRPMale = currentRPCommand[2]
		currentRPFemale = currentRPCommand[3]
	elif len(currentRPCommand) < 4:
		currentRPMale = currentRPCommand[2]
		currentRPFemale = currentRPCommand[2]
	return currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale
		
def rpFindRPCommand(message, chatMembers): #поиск указанной рп команды в базе данных
	global rpAct
	global rpFounded
	global rpTo
	global replyMessage
	global fwdMessage
	rpAct = ''
	rpFounded = 0
	rpComm = message
	replyMessage = 0
	fwdMessage = 0
	foundedRPs = 0
	foundedRPsList = []
	try:
		with open(rpPath + '/' + str(rpId) + '.ini') as fileWithRpCmds:
			allRP = fileWithRpCmds.read()
			fileWithRpCmds.close()
		allRPList = allRP.split('\n')
		currRPIndex = 0
		try: #определение типа сообщений
			if not event.obj.message['reply_message']['from_id'] == 0:
				replyMessage = 1
				currRPIndex = 0
				while currRPIndex < len(allRPList) - 1:
					currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale = getInfoAboutRPCmd(allRPList, currRPIndex)
					if message.lower() == currentRPName or message.lower() == '/rp ' + currentRPId:
						rpFounded = 1
						break
					else:
						currRPIndex += 1
		except:
			try:
				if not event.obj.message['fwd_messages'] == []:
					fwdMessage = 1
					currRPIndex = 0
					while currRPIndex < len(allRPList) - 1:
						currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale = getInfoAboutRPCmd(allRPList, currRPIndex)
						if message.lower() == currentRPName or message.lower() == '/rp ' + currentRPId:
							rpFounded = 1
							break
						else:
							currRPIndex += 1
			except:
				pass
		if rpFounded == 0:
			currRPIndex = 0
			while currRPIndex < len(allRPList) - 1:
				currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale = getInfoAboutRPCmd(allRPList, currRPIndex)
				if message.lower().startswith(currentRPName + ' ') or message.lower().startswith('/rp ' + currentRPId + ' '):
					foundedRPs += 1
					foundedRPsList.append(allRPList[currRPIndex])
				currRPIndex += 1
			if foundedRPs == 1: #схожих команд было не более 1 - использование нужной команды
				rpFounded = 1
				currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale = getInfoAboutRPCmd(foundedRPsList, 0)
			elif foundedRPs > 1: #иначе производятся повторные поиски команд пока совпадений не будет менее 2-ух.
				currRPIndex = 0
				addWordToRp = 1
				currentRPCmd = message.lower().split(' ')[0] + ' ' + message.lower().split(' ')[1] + ' '
				wordsInCurrRP = len(currentRPCmd.split(' ')) - 1
				while foundedRPs > 1: #пока эта переменная не будет меньше 2-ух - цикл будет продолжаться
					currRPIndex = 0
					foundedRPs = 0
					while currRPIndex < len(foundedRPsList):
						currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale = getInfoAboutRPCmd(foundedRPsList, currRPIndex)
						if len(currentRPName.split(' ')) >= wordsInCurrRP:
							if currentRPCmd.startswith(currentRPName + ' '):
								foundedRPs += 1
								currRPIndex += 1
							elif not currentRPCmd.startswith(currentRPName + ' ') and wordsInCurrRP < len(currentRPName.split(' ')):
								foundedRPs += 1
								currRPIndex += 1
							else: #если начало команды не совпадает- удаление его из списка
								del foundedRPsList[currRPIndex]
						else: #если в команде из списка меньше слов чем в сообщении - удаление данной команды из списка
							del foundedRPsList[currRPIndex]
					if foundedRPs == 1:
						rpFounded = 1
						currentRPCommand, currentRPName, currentRPId, currentRPMale, currentRPFemale = getInfoAboutRPCmd(foundedRPsList, 0)
						break
					else: #если обнаружено совпадений больше чем 1 - добавление слов в команду и повторный поиск
						addWordToRp += 1
						currentRPCmd += message.lower().split(' ')[addWordToRp] + ' '
		if rpFounded == 1:
			fromUserIndex = 0
			while not chatMembers['profiles'][fromUserIndex]['id'] == event.obj.message['from_id']:
				fromUserIndex = fromUserIndex + 1
			chatMemberSex = chatMembers['profiles'][fromUserIndex]['sex']
			if chatMemberSex == 0 or chatMemberSex == 2:
				rpAct = currentRPMale.lower()
			if chatMemberSex == 1:
				rpAct = currentRPFemale.lower()
			if message.lower().startswith(currentRPName + ' ') and replyMessage == 0 and fwdMessage == 0:
				rpTo = message
				rpName = list(currentRPName)
				w = 0
				while w < len(rpName):
					rpTo = rpTo.lstrip(rpName[w]).lstrip(rpName[w].upper()).lstrip(' ')
					w = w + 1
			if message.lower().startswith('/rp ' + currentRPId + ' ') and replyMessage == 0 and fwdMessage == 0:
				rpTo = message.lstrip('/rp ').lstrip(currentRPId).lstrip(' ')
			if message.lower() == currentRPName and replyMessage == 1 and fwdMessage == 0 or message.lower() == currentRPId and replyMessage == 1 and fwdMessage == 0:
				rpTo = str(event.obj.message['reply_message']['from_id'])
			if message.lower() == currentRPName and replyMessage == 0 and fwdMessage == 1 or message.lower() == currentRPId and replyMessage == 0 and fwdMessage == 1:
				rpTo = str(event.obj.message['fwd_messages'][0]['from_id'])
	except:
		pass

def rpFindUserTo(chatMembers, rpTo): #поиск того, кому предназначена команда
	global userFounded
	global rpToUser
	userFounded = 0
	find = 0
	nickFounded = 0
	try:
		try: #получение списка никнеймов
			with open(nickPath + '/' + str(rpId) + '.ini') as nicknamesListFile:
				allNicknamesList = nicknamesListFile.read().split('\n')
				nicknamesListFile.close()
		except:
			pass
		try: #проверка есть ли пользователь в беседе
			try: #поиск по имени и фамилии
				f = 0
				while not rpTo == chatMembers['profiles'][f]['first_name'] and not rpTo == chatMembers['profiles'][f]['last_name'] and not rpTo == chatMembers['profiles'][f]['first_name'] + ' ' + chatMembers['profiles'][f]['last_name'] and not rpTo == chatMembers['profiles'][f]['last_name'] + ' ' + chatMembers['profiles'][f]['first_name']:
					f = f + 1
				find = f
			except:
				try: #поиск по короткому имени (id507365405, darky_wings и другим подобным
					f = 0
					while not rpTo.lstrip('[0123456789abcdefghijklmnopqrstuvwxyz_.').lstrip('|*@').rstrip(']') == chatMembers['profiles'][f]['screen_name'] and not rpTo.lstrip('[0123456789abcdefghijklmnopqrstuvwxyz_.').lstrip('|@*').rstrip(']') == 'id' + str(chatMembers['profiles'][f]['id']) and not rpTo == str(chatMembers['profiles'][f]['id']):
						f = f + 1
					find = f
				except:
					try: #поиск по никнейму
						f = 0
						cn = 0
						while cn < len(allNicknamesList) - 1 and not rpTo == allNicknamesList[cn].split('|')[1]:
							cn = cn + 1
						if rpTo == allNicknamesList[cn].split('|')[1]: #получение айди по никнейму
							rpTo = allNicknamesList[cn].split('|')[0]
						while not rpTo == str(chatMembers['profiles'][f]['id']): #поиск уже по полученому айдишнику
							f = f + 1
						find = f
					except:
						pass
			if rpTo == chatMembers['profiles'][find]['first_name'] or rpTo == chatMembers['profiles'][find]['last_name'] or rpTo == chatMembers['profiles'][find]['first_name'] + ' ' + chatMembers['profiles'][find]['last_name'] or rpTo == chatMembers['profiles'][find]['last_name'] + ' ' + chatMembers['profiles'][find]['first_name'] or rpTo.lstrip('[1234567890qwertyuiopasdfghjklzxcvbnm_.').lstrip('|@').rstrip(']') == chatMembers['profiles'][find]['screen_name'] or rpTo == str(chatMembers['profiles'][find]['id']) or rpTo.lstrip('[1234567890qwertyuiopasdfghjklzxcvbnm_.').lstrip('|@').rstrip(']') == 'id' + str(chatMembers['profiles'][find]['id']): #устанавливаем значение переменной userFounded на 1
				userFounded = 1
		except:
			pass
		try: #получение айди пользователя
			if userFounded == 1:
				rpToId = chatMembers['profiles'][find]['id']
		except:
			pass
		try: #поиск никнейма в базе данных для ответа
			cn = 0
			while cn < len(allNicknamesList) - 1 and not str(rpToId) == allNicknamesList[cn].split('|')[0]:
				cn = cn + 1
			if str(rpToId) == allNicknamesList[cn].split('|')[0]: #получение айди по никнейму
				nicknameRpTo = allNicknamesList[cn].split('|')[1]
				nickFounded = 1
		except:
			pass
		try: #определяет можно ли упоминать пользователя в ответе
			mentPermission = 0
			with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
				mentionPermission = checkMentionPerm.read()
				checkMentionPerm.close()
			mentionPermission = mentionPermission.split('_')
			curUserCheckMentPerm = 0
			while curUserCheckMentPerm < len(mentionPermission):
				curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
				try:
					if curCheckMentPerm == str(event.obj.message['reply_message']['from_id']):
						mentPermission = 1
						break
				except:
					pass
				try:
					if curCheckMentPerm == str(event.obj.message['fwd_messages'][0]['from_id']):
						mentPermission = 1
						break
				except:
					pass
				try:
					if curCheckMentPerm == str(rpToId):
						mentPermission = 1
						break
				except:
					pass
				curUserCheckMentPerm = curUserCheckMentPerm + 1
		except:
			mentPermission = 0
		try:
			if mentPermission == 0 and userFounded == 1 and nickFounded == 1:
				rpToUser = '[id' + str(rpToId) + '|' + nicknameRpTo + ']'
			elif mentPermission == 0 and userFounded == 1 and nickFounded == 0:
				rpToUser = '[id' + str(rpToId) + '|' + chatMembers['profiles'][find]['first_name'] + ' ' + chatMembers['profiles'][find]['last_name'] + ']'
			elif mentPermission == 1 and userFounded == 1 and nickFounded == 1:
				rpToUser = nicknameRpTo
			elif mentPermission == 1 and userFounded == 1 and nickFounded == 0:
				rpToUser = chatMembers['profiles'][find]['first_name'] + ' ' + chatMembers['profiles'][find]['last_name']
		except:
			raise
	except:
		pass
	
def roleplayCommands(message, rpChatId):
	try:
		rpFindUserFrom(vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id))
		rpFindRPCommand(message, vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id))
		rpFindUserTo(vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id), rpTo)
		if rpFounded == 1 and userFounded == 1:
			send_message_to_chat(rpFromUser + ' ' + rpAct + ' ' + rpToUser, rpChatId)
		elif rpFounded == 1 and userFounded == 0:
			send_message_to_chat('⚠️Данного человека нет в беседе', rpChatId)
	except:
		pass
		
def distortMessage(distortMess):
	distortMessageOut = ''
	distortMessageInt = 0
	distortMessageSymbols = ['█', '▒', '□', '?', '[]']
	distortMessageLen = len(distortMess)
	while not distortMessageInt == distortMessageLen:
		distortRandomSymbol = random.randint(1, 18)
		if distortRandomSymbol < 6:
			distortMessageOut = distortMessageOut + distortMessageSymbols[distortRandomSymbol - 1]
			distortMessageInt = distortMessageInt + 1
		else:
			distortMessageOut = distortMessageOut + distortMess[distortMessageInt]
			distortMessageInt = distortMessageInt + 1
	return distortMessageOut

def init_message_from_user(message, id): #определение команды из личных сообщений
	global i
	global outMess
	global bd_date
	if "Дурки" in message or "боты тупые" in message.lower() or "боты не имеют мозгов" in message.lower():
		print('id:', event.obj.message['from_id'], ':', message)
		send_message_to_user('Обидно ;с', id)
	elif "доброе утро" in message.lower() or "утра" in message.lower() or "добре" in message.lower() or "доброе" in message.lower():
		print('id:', event.obj.message['from_id'], ':', message)
		goodMorningMessage = ['Доброе', 'Утра', 'Доброе утро', 'Привет', 'Преть']
		send_message_to_user(random.choice(goodMorningMessage), id)
	elif "спокойной ночи" in message.lower() or "споки" in message.lower() or "споке" in message.lower():
		print('id:', event.obj.message['from_id'], ':', message)
		sleepMessage = ['Споки', 'Добрых снов', 'Спокойной', 'Спокойной ночи', 'Ночки', 'Сладких снов']
		sleepRand = random.randint(0, len(sleepMessage))
		send_message_to_user(sleepMessage[sleepRand - 1], id)
	elif message in aboutMeCommand:
		print('id:', event.obj.message['from_id'], ':', message)
		with open(pathCV) as file:
			curVer = file.read()
		send_message_to_user('⚙️' + curVer, id)
	elif message in updHystCommand:
		print('id:', event.obj.message['from_id'], ':', message)
		with open(pathUH) as file:
			updHyst = file.read()
		send_message_to_user('💾' + updHyst, id)
	elif message in curVerCommand:
		print('id:', event.obj.message['from_id'], ':', message)
		send_message_to_user('⚙️Моя текущая версия - ' + currentVersion, id)
	elif message in helpCommand:
		print('id:', event.obj.message['from_id'], ':', message)
		send_message_to_user('Чтобы узнать мои команды - введите "Дарки, команды".\nЕсли вы хотите узнать информацию об отдельной команде - введите "Дарки, помощь <команда>"', id)
	elif message.startswith('Дарки, помощь') or message.startswith('Дарки помощь') or message.startswith('/darky_help'):
		print('id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			if message.startswith('Дарки,'):
				infoAboutComm = message.lstrip('Дарки,').lstrip(' ')
			if message.startswith('Дарки'):
				infoAboutComm = message.lstrip('Дарки').lstrip(' ')
			infoAboutComm = infoAboutComm.lstrip('помощь').lstrip(' ')
		elif message.startswith('/darky'):
			infoAboutComm = message.lstrip('/darky_help').lstrip(' =')
		iacomm = infoAboutComm
		if iacomm in startUpCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - предназначена для моего запуска если я ещё не совсем запущена.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in turnOffCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - предназначена для моего выключения если я запущена.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in restartCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - предназначена для моего перезапуска.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in updateCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - предназначена для вызова обновления моих скриптов.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in helpCommand:
			cmdType = random.randint(1, 4)
			if cmdType == 1:
				cmdIndex = random.randint(0, 2)
				cmdName = startUpCommand[cmdIndex]
			elif cmdType == 2:
				cmdIndex = random.randint(0, 6)
				cmdName = newRPCmd[cmdIndex]
			elif cmdType == 3:
				cmdIndex = random.randint(0, 4)
				cmdName = getNickList[cmdIndex]
			elif cmdType == 4:
				cmdIndex = random.randint(0, 2)
				cmdName = aboutMeCommand[cmdIndex]
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит информацию о команде если был добавлен соответствующий аргумент.\n❗Доступна всем пользователям.\n❔Пример использования:\n1.' + iacomm + ' ' + cmdName + '\n2.' + iacomm, id)
		elif iacomm in getCommandList:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит список доступных команд бота\n❗Доступна всем пользователям', id)
		elif iacomm in curVerCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит текущую версию бота\n❗Доступна всем пользователям', id)
		elif iacomm in updHystCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит полную историю обновлений\n❗Доступна всем пользователям', id)
		elif iacomm in aboutMeCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит краткую информацию о себе\n❗Доступна всем пользователям', id)
		elif iacomm in randChooseCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выбирает одно из предложенных вариантов\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, выбери ' + random.choice(chooseExample) + ' или ' + random.choice(chooseExample), id)
		elif iacomm in probabilityCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит рандомную вероятность указанного события\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, вероятность ' + random.choice(probabilityExample), id)
		elif iacomm in tryCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - указывает было ли данное действие успешным или нет\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, попытка ' + random.choice(tryExample), id)
		elif iacomm in repeatCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - повторяет данный текст\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, скажи ' + random.choice(repeatExample), id)
		elif iacomm in distortMessageCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - искажает указанный текст\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, искази текст: ' + random.choice(distortMessageExample), id)
		elif iacomm in mentionOn:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - включает упоминания ботом для текущего пользователя (изначально включено)\n❗Доступна всем пользователям', id)
		elif iacomm in mentionOff:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - отключает упоминания ботом для текущего пользователя (изначально включено)\n❗Доступна всем пользователям', id)
		elif iacomm in voiceCommand:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - генерирует предложение из рандомных слов, иногда со смысолом\n❗Доступна всем пользователям', id)
		elif iacomm in voiceDataSize:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит размер собранных данных о текущей беседе\n❗Доступна всем пользователям', id)
		elif iacomm in clearVoiceData:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - очищает собранные данные о текущей беседе\n❗Доступна всем пользователям', id)
		elif iacomm in rollCube:
			send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - бросает игральную кость и выводит выпавшее число\n❗Доступна всем пользователям', id)
		elif iacomm in getRandomCount:
			randomStart = random.randint(-100, 100)
			randomEnd = random.randint(randomStart, 100)
			if not iacomm.startswith('/'):
				send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит рандомное число в указанном диапазоне\n❗Доступна всем пользователям\n❔Пример использования:\n' + iacomm + ' от ' + str(randomStart) + ' до ' + str(randomEnd), id)
			else:
				send_message_to_user('❕"' + iacomm + '" или другие вариации этой команды - выводит рандомное число в указанном диапазоне\n❗Доступна всем пользователям\n❔Пример использования:\n' + iacomm + '=' + str(randomStart) + ', ' + str(randomEnd), id)
		else:
			send_message_to_user('⚠️Я не нашла информацию об этой команде, возможно вы ошиблись в её написании', id)
	elif message in getCommandList:
		print('id:', event.obj.message['from_id'], ':', message)
		allCmdsOut = ''
		with open(mainPathDB + 'commandList.ini') as allCommands:
			allCmdsList = allCommands.read().split('\n\n')
			allCommands.close()
		allCmdsOut = allCmdsList[0] + '\n\n' + allCmdsList[1] + '\n\n' + allCmdsList[2]
		send_message_to_user(allCmdsOut, id)
	elif 'тест' in message.lower() or 'test' in message.lower():
		if adminStatus == 1:
			secretTaken = 0
			usersWithSecret = vk.messages.getConversationMembers(peer_id = 2000000004)
			print('id:', event.obj.message['from_id'], ':', message)
			u = 0
			try:
				while not u > usersWithSecret['count']:
					if event.obj.message['from_id'] == usersWithSecret['profiles'][u]['id']:
						secretTaken = 1
						break
					else:
						u = u + 1
			except:
				secretTaken = 0
			if 'тест' in message.lower() and secretTaken == 0 or 'test' in message.lower() and secretTaken == 0:
				if message.lower() == 'тест2310':
					send_message_to_user('Поздравляю! Вы получили секрет - ссылка на беседу где проводятся мои тесты, там вы можете раньше всех узнать о том, что будет добавлено в меня и увидеть часть процесса разработки', id)
					send_message_to_user('https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp', id)
				elif message.lower() == 'тест' + bd_date:
					send_message_to_user('Хорошая попытка, но использовать приведённый мною пример - так себе идея. Я не настолько тупая и "случайно" выдать правильный ответ не могу', id)
				else:
					bd_day_str = ''
					bd_month_str = ''
					bd_month = random.randint(1, 12)
					if not bd_month == 2:
						bd_day = random.randint(1, 31)
					else:
						bd_day = random.randint(1, 29)
					if bd_day == 23 and bd_month == 10:
						while bd_day == 23 and bd_month == 10:
							bd_month = random.randint(1, 12)
							if not bd_month == 2:
								bd_day = random.randint(1, 31)
							else:
								bd_day = random.randint(1, 29)
					if bd_day < 10:
						bd_day_str = '0' + str(bd_day)
					else:
						bd_day_str = str(bd_day)
					if bd_month < 10:
						bd_month_str = '0' + str(bd_month)
					else:
						bd_month_str = str(bd_month)
					bd_date = bd_day_str + bd_month_str
					send_message_to_user('Вы почти у цели! Введите "тест" приписав к нему день рождения моего создателя без пробелов и точек.\nНапример "тест' + bd_date + '"', id)
	elif message.startswith("Дарки выбери") or message.startswith("Дарки, выбери"):
		print('id:', event.obj.message['from_id'], ':', message)
		choosingMess = event.obj.message['text']
		if message.startswith("Дарки выбери"):
			chooseStr = choosingMess.lstrip('Дарки ')
		if message.startswith("Дарки, выбери"):
			chooseStr = choosingMess.lstrip('Дарки, ')
		chooseStr = chooseStr.lstrip('выбери').lstrip(' ')
		chooseList = chooseStr.split(' или ')
		chooseListLen = len(chooseList)
		chooseRandInt = random.randint(0, chooseListLen)
		chooseResult = chooseList[chooseRandInt - 1]
		if chooseListLen > 1:
			send_message_to_user('Я выбираю ' + chooseResult, id)
		else:
			send_message_to_user('⚠️Я не могу выбрать что-либо поскольку мне дали либо один вариант ответа, либо мне не дали варианты ответа вообще', id)
	elif message.startswith('Дарки, вероятность') or message.startswith('Дарки вероятность'):
		print('id:', event.obj.message['from_id'], ':', message)
		probabilityMess = event.obj.message['text']
		if message.startswith('Дарки, вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки, ')
		if message.startswith('Дарки вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки ')
		probabilityStr = probabilityStr.lstrip('вероятность').lstrip(' ')
		probabilityRandom = random.randint(0, 100)
		probabilityResult = str(probabilityRandom) + '%'
		if not probabilityStr == '':
			send_message_to_user('Вероятность того, что ' + probabilityStr + ' составляет ' + probabilityResult, id)
		else:
			send_message_to_user('⚠️Не могу просчитать вероятность, пожалуйста введите предложение после "Дарки, вероятность"', id)
	elif message.startswith('Дарки, попытка') or message.startswith('Дарки попытка'):
		print('id:', event.obj.message['from_id'], ':', message)
		tryMess = event.obj.message['text']
		if message.startswith('Дарки, попытка'):
			tryStr = tryMess.lstrip('Дарки, ')
		if message.startswith('Дарки попытка'):
			tryStr = tryMess.lstrip('Дарки ')
		tryStr = tryStr.lstrip('попытка')
		tryRandom = random.randint(0, 1)
		if tryRandom == 0 and not tryStr == '':
			send_message_to_user('❌Попытка' + tryStr + ' вышла неудачной', id)
		elif tryRandom == 1 and not tryStr == '':
			send_message_to_user('✅Попытка' + tryStr + ' вышла удачной', id)
		else:
			send_message_to_user('⚠️Пожалуйста укажите действие, дабы я решила, было ли оно удачным или же наоборот - неудачным', id)
	elif message.startswith('Дарки, искази текст') or message.startswith('Дарки искази текст') or message.startswith('/darky_distort='):
		print('id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			if message.startswith('Дарки, '):
				distortMess = message.lstrip('Дарки, ')
			elif message.startswith('Дарки '):
				distortMess = message.lstrip('Дарки ')
			distortMess = distortMess.lstrip('искази ').lstrip('текст:').lstrip(' ')
		elif message.startswith('/darky'):
			distortMess = message.lstrip('/darky_distort').lstrip('=')
		distortMess = list(distortMess)
		distortMessageOut = distortMessage(distortMess)
		send_message_to_user(distortMessageOut, id)
	elif message.startswith('Дарки, скажи') or message.startswith('Дарки скажи') or message.startswith('/darky_say='):
		print('id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			if message.startswith('Дарки, '):
				repeatMess = message.lstrip('Дарки, ')
			elif message.startswith('Дарки '):
				repeatMess = message.lstrip('Дарки ')
			repeatMess = repeatMess.lstrip('скажи ')
		elif message.startswith('/darky'):
			repeatMess = message.lstrip('/darky_say').lstrip('=')
		send_message_to_user(repeatMess, id)
	elif message in rollCube:
		print('id:', event.obj.message['from_id'], ':', message)
		diceRandom = random.randint(1, 6)
		send_message_to_user('🎲На кубике выпало число: ' + str(diceRandom), id)
	elif message in voiceCommand:
		print('id:', event.obj.message['from_id'], ':', message)
		randSendLen = random.randint(2, 15)
		with open(pathMess + '/' + str(event.obj.message['from_id']) + '.ini') as messRead:
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
		grammaticRand = random.randint(0, 10)
		if grammaticRand == 0:
			outMess = outMess.capitalize()
		elif grammaticRand == 1:
			outMess = outMess.upper()
		elif grammaticRand == 2:
			outMess = outMess.lower()
		if len(wordList) > 19:
			send_message_to_user(outMess, id)
		elif len(wordList) < 20:
			send_message_to_user('⚠️Я пока что собрала недостаточно данных для более менее хорошей генерации своих сообщений, дайте мне изучить беседу подольше и я обещаю, что смогу сгенерировать что-нибудь, хоть и не очень умное', id)
		i = 0
		outMess = ''
	elif message in clearVoiceData:
		print('id:', event.obj.message['from_id'], ':', message)
		send_message_to_user('Очищаю собранные данные об этом диалоге...', id)
		with open(pathMess + '/' + str(event.obj.message['from_id']) + '.ini', 'w') as messEarse:
			messEarse.close()
		send_message_to_user('✅Данные очищены', id)
	elif message in voiceDataSize:
		print('id:', event.obj.message['from_id'], ':', message)
		sizePath = pathMess + '/' + str(event.obj.message['from_id']) + '.ini'
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
		send_message_to_user('Размер собранных данных об этом диалоге составляет: ' + str(fSize) + ' ' + sizeTypeStr, id)
	elif message in mentionOff:
		print('id:', event.obj.message['from_id'], ':', message)
		try:
			with open(mainPathDB + 'usersMentionOff.ini', 'a') as mentionOffFile:
				mentionOffFile.close()
		except:
			with open(mainPathDB + 'usersMentionOff.ini', 'w') as mentionOffFile:
				mentionOffFile.close()
		try:
			with open(mainPathDB + 'usersMentionOff.ini') as mentionOffFile:
				checkMentionPermMode = mentionOffFile.read()
				mentionOffFile.close()
			try:
				m = 0
				mentionCurrModeOff = 0
				while m < len(checkMentionPermMode.split('_')):
					checkMentionPermModeSplit = checkMentionPermMode.split('_')
					curMentionCheckMode = checkMentionPermModeSplit[m]
					if curMentionCheckMode == str(event.obj.message['from_id']):
						mentionCurrModeOff = 1
					m = m + 1
			except:
				mentionCurrModeOff = 0
			if mentionCurrModeOff == 0:
				with open(mainPathDB + 'usersMentionOff.ini', 'a') as mentionOffFile:
					mentionOffFile.write(str(event.obj.message['from_id']) + '_')
					mentionOffFile.close()
				send_message_to_user('✅Постараюсь не упоминать вас без нужды', id)
			else:
				send_message_to_user('Я уже снизила ваше упоминание в моих сообщениях до минимума', id)
		except:
			send_message_to_user('⚠️Произошла ошибка\n\nДополнительная информация:\n- - -\n' + getTraceback(), id)
	elif message in mentionOn:
		print('id:', event.obj.message['from_id'], ':', message)
		try:
			foundedUserWithOffMention = 0
			with open(mainPathDB + 'usersMentionOff.ini') as mentionOnFile:
				mentionOffUsers = mentionOnFile.read()
				mentionOnFile.close()
			m = 0
			while m < len(mentionOffUsers.split('_')):
				mentionOffUsersSplit = mentionOffUsers.split('_')
				curMentionCheckMode = mentionOffUsersSplit[m]
				if curMentionCheckMode == str(event.obj.message['from_id']):
					foundedUserWithOffMention = 1
				m = m + 1
			if foundedUserWithOffMention == 1:
				with open(mainPathDB + 'usersMentionOff.ini', 'w') as mentionOnFile:
					m = 0
					while m < len(mentionOffUsers.split('_')) - 1:
						curUserChangePermMention = mentionOffUsersSplit[m]
						if curUserChangePermMention == str(event.obj.message['from_id']):
							pass
						else:
							mentionOnFile.write(mentionOffUsersSplit[m] + '_')
						m = m + 1
					mentionOnFile.close()
				send_message_to_user('✅Я включила вам все упоминания в своих ответах', id)
			else:
				send_message_to_user('❌Я не могу начать вас упоминать если у вас итак включены упоминания от меня', id)
		except:
			send_message_to_user('⚠️Произошла ошибка\n\nДополнительная информация:\n- - -\n' + getTraceback(), id)
	elif message.startswith('Дарки, рандом') or message.startswith('Дарки рандом') or message.startswith('/darky_random'):
		print('id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			randomSize = message.lstrip('Дарки,').lstrip(' ').lstrip('рандом').lstrip(' ').lstrip('от').lstrip(' ').split(' до ')
		elif message.startswith('/darky'):
			randomSize = message.lstrip('/darky_random').lstrip('=').split(', ')
		if len(randomSize) == 2:
			try:
				randomResult = random.randint(int(randomSize[0]), int(randomSize[1]))
				send_message_to_user('Рандомное число: ' + str(randomResult), id)
			except ValueError:
				send_message_to_user('⚠️Вторая граница должна превышать первую', id)
		else:
			send_message_to_user('⚠️Границы рандома должны быть указаны двумя числами разделёнными "до"', id)
	elif len(message.split(' ')) == 2:
		messWords = message.split(' ')
		if messWords[0].lower() in hiCommand and "Дарки" in message or messWords[1].lower() in hiCommand and "Дарки" in message:
			print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
			hiMessage = ['Преть', 'Привет']
			hiRand = random.randint(1, len(hiMessage))
			send_message_to_user(hiMessage[hiRand - 1], id)

def init_message_from_chat(message, id): #определение команды из беседы
	global i
	global outMess
	global bd_date
	if adminStatus == 1:
		roleplayCommands(event.obj.message['text'], rpId)
	if message in callAllCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
			out = ''
			chatMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
			countOfMembers = chatMembers['count']
			out = 'Всего участников: ' + str(countOfMembers) + '\n'
			n = 0
			curProf = 1
			while n < countOfMembers:
				nou = 0
				try:
					uid = chatMembers['profiles'][n]['id']
					first_name = chatMembers['profiles'][n]['first_name']
					last_name = chatMembers['profiles'][n]['last_name']
					try:
						mentPermission = 0
						with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
							mentionPermission = checkMentionPerm.read()
							checkMentionPerm.close()
						mentionPermission = mentionPermission.split('_')
						curUserCheckMentPerm = 0
						while curUserCheckMentPerm < len(mentionPermission):
							curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
							if curCheckMentPerm == str(uid):
								mentPermission = 1
							else:
								pass
							curUserCheckMentPerm = curUserCheckMentPerm + 1
					except:
						mentPermission = 0
					if mentPermission == 0:
						currProf = str(curProf) + '. [id' + str(uid) + '|' + str(first_name) + ' ' + str(last_name) + ']' + '\n'
					if mentPermission == 1:
						currProf = str(curProf) + '. ' + str(first_name) + ' ' + str(last_name) + '\n'
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
			send_message_to_chat(out, id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message.capitalize().startswith('Дарки, создай рп команду') or message.capitalize().startswith('Дарки создай рп команду') or message.startswith('/darky_create_rpCommand='):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				curRPCommand = 0
				createdRPCommand = 0
				if message.startswith('Дарки'):
					message = message.capitalize()
					if message.startswith('Дарки, создай'):
						rpNew = message.lstrip('Дарки, ')
					if message.startswith('Дарки создай'):
						rpNew = message.lstrip('Дарки ')
					rpNew = rpNew.lstrip('создай ').lstrip('рп ').lstrip('команду')
				if message.startswith('/darky'):
					rpNew = message.lstrip('/darky_create_rpCommand').lstrip('=')
				rpNew = rpNew.lstrip(' ')
				rpNew = rpNew.lower()
				if not rpNew == '' and len(rpNew.split(' ')) < 5:
					try:
						with open(rpPath + '/' + str(rpId) + '.ini', 'a') as rpChatCheck: #проверка на наличие файла с командами
							rpChatCheck.close()
					except:
						with open(rpPath + '/' + str(rpId) + '.ini', 'w') as rpChatCheck: #создание файла где будут храниться команды
							rpChatCheck.close()
					try:
						with open(rpPath + '/' + str(rpId) + '.ini') as rpCreateCheck: #проверка существует ли данная команда
							allRPCommands = rpCreateCheck.read().split('\n')
							linesRPCreate = len(allRPCommands)
							rpCreateCheck.close()
						while not curRPCommand > linesRPCreate:
							curCheckRP = allRPCommands[curRPCommand]
							curCheckRP = curCheckRP.split('-')
							if rpNew == curCheckRP[0]:
								createdRPCommand = createdRPCommand + 1
							else:
								pass
							curRPCommand = curRPCommand + 1
					except:
						pass
					if createdRPCommand == 0: #если команда не обнаружена - происходит её запись в файл
						try:
							with open(rpPath + '/' + str(rpId) + '.ini', 'r') as rpNewComm:
								rpNewBackup = rpNewComm.read()
								linesNewRP = len(rpNewBackup.split('\n')) - 1
								rpNewComm.close()
							with open(rpPath + '/' + str(rpId) + '.ini', 'a') as rpNewComm:
								if linesNewRP < 0:
									lastRPCommandId = allRPCommands[linesRPCreate - 1]
									lastRPCommandId = lastRPCommandId.split('-')
									lastRPCommandId = lastRPCommandId[1]
									while int(lastRPCommandId) > linesNewRP - 1:
										linesNewRP = linesNewRP + 1
								newRoleplayCommand =  rpNew + '-' + str(linesNewRP) + '-<действие>'
								if not newRoleplayCommand == '':
									rpNewComm.write(newRoleplayCommand + '\n')
									rpNewComm.close()
								else:
									rpNewComm.write(rpNewBackup)
									rpNewComm.close()
									raise
							send_message_to_chat('✅Команда создана\nid созданной команды: ' + str(linesNewRP), id)
						except:
							try:
								with open(rpPath + '/' + str(rpId) + '.ini', 'w') as rpNewComm:
									rpNewComm.write(rpNewBackup)
									rpNewComm.close()
							except:
								send_message_to_chat('❗При восстановлении сохранённых команд произошла ошибка. Возможно все созданные в этой беседе команды - сбросились.\nПрошу прощения..', id)
							exc_type, exc_value, exc_traceback = sys.exc_info()
							tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
							tbOut = ''
							c = 0
							while c < len(tbObject):
								tbOut = tbOut + tbObject[c] + '\n\n'
								c = c + 1
							send_message_to_chat('❌Не удалось создать команду\n- - -\nДополнительная информация:\n\n' + tbOut, id)
					else:
						send_message_to_chat('⚠️Такая команда уже существует', id)
				elif len(rpNew.split(' ')) > 4:
					send_message_to_chat('⚠️Ограничение: в данной команде содержится больше 4-х слов', id)
				else:
					send_message_to_chat('⚠️Невозможно создать команду с пустым названием', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message.capitalize().startswith('Дарки, удали рп команду') or message.capitalize().startswith('Дарки удали рп команду') or message.startswith('/darky_delete_rpCommand='):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				deletedRPCommand = 0
				curDelRPLine = 0
				rpDelResult = ''
				if message.startswith('Дарки'):
					message = message.capitalize()
					if message.startswith('Дарки, удали'):
						rpDel = message.lstrip('Дарки, ')
					if message.startswith('Дарки удали'):
						rpDel = message.lstrip('Дарки ')
					rpDel = rpDel.lstrip('удали ').lstrip('рп ').lstrip('команду')
				if message.startswith('/darky'):
					rpDel = message.lstrip('/darky_delete_rpCommand').lstrip('=')
				rpDel = rpDel.lstrip(' ')
				rpDel = rpDel.lower()
				if not rpDel == '':
					try: #оболочка нужна для определения создан ли файл с командами
						with open(rpPath + '/' + str(rpId) + '.ini', 'r') as rpDelComm: #проверка количества строк и в целом получение нужной инфы
							rpDelBackup = rpDelComm.read()
							allRPCommands = rpDelBackup.split('\n')
							linesRPDel = len(allRPCommands)
							rpDelComm.close()
						if not linesRPDel > 1: #если строк меньше 1(никаких команд нет в файле) - вызывается исключение
							raise
						with open(rpPath + '/' + str(rpId) + '.ini', 'w') as rpDelComm: #перезапись в файл список команд изменяя при этом его(удаляя указанную)
							while not curDelRPLine > linesRPDel - 2: #поиск и удаление нужной команды
								curRPCommand = allRPCommands[curDelRPLine]
								curRPCommand = curRPCommand.split('-')
								if rpDel == curRPCommand[0] or rpDel == curRPCommand[1]:
									deletedRPCommand = 1
								else:
									rpDelResult = allRPCommands[curDelRPLine] + '\n'
									rpDelComm.write(rpDelResult) #запись в файл результата изменений
								curDelRPLine = curDelRPLine + 1
							rpDelComm.close()
						if deletedRPCommand == 1:
							send_message_to_chat('✅Команда удалена', id)
						if deletedRPCommand == 0:
							send_message_to_chat('❌Команда не удалена, возможно вы ошиблись в её названии', id)
					except:
						try:
							with open(rpPath + '/' + str(rpId) + '.ini', 'w') as rpDelComm:
								rpDelComm.write(rpDelBackup)
								rpDelComm.close()
						except:
							send_message_to_chat('❗При восстановлении сохранённых команд произошла ошибка. Возможно все созданные в этой беседе команды - сбросились.\nПрошу прощения..', id)
						send_message_to_chat('⚠️В вашей беседе нет созданных рп команд', id)
				else:
					send_message_to_chat('⚠️Невозможно удалить команду с пустым названием', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message.capitalize().startswith('Дарки, установи рп действие') or message.capitalize().startswith('Дарки установи рп действие') or message.startswith('/darky_set_rpAction='):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				curActionRPLine = 0
				setActionDone = 0
				rpActionResult = ''
				if message.startswith('Дарки'):
					message = message.capitalize()
					if message.startswith('Дарки, установи'):
						rpAction = message.lstrip('Дарки, ')
					if message.startswith('Дарки установи'):
						rpAction = message.lstrip('Дарки ')
					rpAction = rpAction.lstrip('установи ').lstrip('рп ').lstrip('действие')
				if message.startswith('/darky'):
					rpAction = message.lstrip('/darky_set_rpAction').lstrip('=')
				rpAction = rpAction.lstrip(' ')
				try:
					try:
						rpAction = rpAction.split(', ') #разделение запроса на название команды или её айди и действия для этой команды
					except:
						pass
					if len(rpAction) < 3 and len(rpAction) > 1: #работа будет выполняться только с одним знаком ","
						rpComm = rpAction[0]
						rpComm = rpComm.lower()
						rpAction = rpAction[1]
						rpAction = rpAction.lower()
						rpActionSplit = rpAction.split('-')
						if len(rpActionSplit) == 2: #если в действиях было указано не больше двух вариаций - будет продолжаться работа команды
							try:
								with open(rpPath + '/' + str(rpId) + '.ini', 'r') as rpActionComm:
									rpActionBackup = rpActionComm.read()
									allRPCommands = rpActionBackup.split('\n')
									linesRPAct = len(allRPCommands)
									rpActionComm.close()
								if not linesRPAct > 1:
									raise
								with open(rpPath + '/' + str(rpId) + '.ini', 'w') as rpActionComm: #перезапись в файл с изменениями списка
									while not curActionRPLine == linesRPAct - 1: #находит нужную команду и перезаписывает к ней вариации действий
										curRPCommand = allRPCommands[curActionRPLine]
										curRPCommand = curRPCommand.split('-')
										if rpComm == curRPCommand[0] or rpComm == curRPCommand[1]:
											rpActionResult = rpActionResult + str(curRPCommand[0]) + '-' + str(curRPCommand[1]) + '-' + rpAction + '\n'
											setActionDone = 1
										else:
											rpActionResult = rpActionResult + allRPCommands[curActionRPLine] + '\n'
										curActionRPLine = curActionRPLine + 1
									rpActionComm.write(rpActionResult)
									rpActionComm.close()
								if setActionDone == 1:
									send_message_to_chat('✅Действие установлено', id)
								else:
									send_message_to_chat('❌Я не смогла найти эту команду для установки рп действия', id)
							except:
								try:
									with open(rpPath + '/' + str(rpId) + '.ini', 'w') as rpActionComm:
										rpActionComm.write(rpActionBackup)
										rpActionComm.close()
								except:
									send_message_to_chat('❗При восстановлении сохранённых команд произошла ошибка. Возможно все созданные в этой беседе команды - сбросились.\nПрошу прощения..', id)
								send_message_to_chat('⚠️В вашей беседе нет созданных рп команд', id)
						else:
							send_message_to_chat('⚠️Запрос должен выглядеть так: "Дарки, установи рп действие <название команды или его id>, <действие для этой команды вида "укусил-укусила">"', id)
					else:
						send_message_to_chat('⚠️Запрос должен выглядеть так: "Дарки, установи рп действие <название команды или его id>, <действие для этой команды вида "укусил-укусила">"', id)
				except:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
					tbOut = ''
					c = 0
					while c < len(tbObject):
						tbOut = tbOut + tbObject[n] + '\n\n'
						c = c + 1
					send_message_to_chat('❌Действие не установлено\n\nДополнительная информация:\n- - -\n' + tbOut, id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message.startswith("Дарки, установи мой ник на") or message.startswith("Дарки установи мой ник на") or message.startswith('/darky_myNickname=') or message.startswith('Дарки, ник') or message.startswith('Дарки ник'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		currentNickname = 0
		usedNickname = 0
		userWithNickname = 0
		nickSet = ''
		setNickDone = 0
		if message.startswith('Дарки'):
			if message.startswith('Дарки, установи'):
				nicknameNew = message.lstrip('Дарки, ')
			elif message.startswith('Дарки установи'):
				nicknameNew = message.lstrip('Дарки ')
			if nicknameNew.startswith('установи'):
				nicknameNew = nicknameNew.lstrip('установи ').lstrip('мой ').lstrip('ник ').lstrip('на')
			elif nicknameNew.startswith('ник'):
				nicknameNew = nicknameNew.lstrip('ник')
		if message.startswith('/darky'):
			nicknameNew = message.lstrip('/darky_myNickname').lstrip('=')
		nicknameNew = nicknameNew.lstrip(' ')
		if not nicknameNew == '':
			try:
				with open(nickPath + '/' + str(rpId) + '.ini', 'a') as nicknameChatCheck: #проверка существования файла с никнеймами
					nicknameChatCheck.close()
			except:
				with open(nickPath + '/' + str(rpId) + '.ini', 'w') as nicknameChatCheck: #создение этого файла в случае его отсутствия
					nicknameChatCheck.close()
			try:
				with open(nickPath + '/' + str(rpId) + '.ini') as newNickCheck: #считывание содержимого
					nicknamesBackup = newNickCheck.read()
					allNicknames = nicknamesBackup.split('\n')
					linesNickNew = len(allNicknames)
					newNickCheck.close()
				while not currentNickname > linesNickNew - 1: #определение занят ли никнейм или нет и есть ли у пользователя установленный никнейм
					curCheckNick = allNicknames[currentNickname]
					curCheckNick = curCheckNick.split('|')
					if nicknameNew == curCheckNick[1]:
						usedNickname = usedNickname + 1
					if str(event.obj.message['from_id']) == curCheckNick[0]:
						userWithNickname = 1
					currentNickname = currentNickname + 1
			except:
				pass
			if usedNickname == 0 and userWithNickname == 0: #запись как новая строчка в файле если ник свободен и у него не было никнейма
				try:
					with open(nickPath + '/' + str(rpId) + '.ini', 'r') as newNick:
						linesNewNick = len(newNick.read().split())
						newNick.close()
					with open(nickPath + '/' + str(rpId) + '.ini', 'a') as newNick:
						newUserNickname = str(event.obj.message['from_id']) + '|' + nicknameNew + '\n'
						newNick.write(newUserNickname)
						newNick.close()
					with open(nickPath + '/' + str(rpId) + '.ini') as nickRead: #считывание результата для вывода ответа
						allNicknames = nickRead.read().split('\n')
						linesNickNew = len(allNicknames)
						nickRead.close()
					currentNickname = 0
					while not currentNickname > linesNickNew - 1:
						curCheckNick = allNicknames[currentNickname]
						curCheckNick = curCheckNick.split('|')
						if str(event.obj.message['from_id']) == curCheckNick[0]:
							userIdFromNick = curCheckNick[0]
							userNicknameFromNick = curCheckNick[1]
						currentNickname = currentNickname + 1
					try:
						mentPermission = 0
						with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
							mentionPermission = checkMentionPerm.read()
							checkMentionPerm.close()
						mentionPermission = mentionPermission.split('_')
						curUserCheckMentPerm = 0
						while curUserCheckMentPerm < len(mentionPermission):
							curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
							if curCheckMentPerm == str(event.obj.message['from_id']):
								mentPermission = 1
							else:
								pass
							curUserCheckMentPerm = curUserCheckMentPerm + 1
					except:
						mentPermission = 0
					if mentPermission == 0:
						send_message_to_chat('✅Ваш никнейм теперь - [id' + userIdFromNick + '|' + userNicknameFromNick + ']', id)
					if mentPermission == 1:
						send_message_to_chat('✅Ваш никнейм теперь - ' + userNicknameFromNick, id)
				except:
					try:
						with open(nickPath + '/' + str(rpId) + '.ini', 'w') as newNick: #восстанлвление никнеймов из бекапа, созданный ещё при первом чтении в начале команды
							newNick.write(nicknamesBackup)
							newNick.close()
					except:
						send_message_to_chat('❗При восстановлении сохранённых никнеймов произошла ошибка. Возможно все никнеймы в этой беседе сбросились.\nПрошу прощения..', id)
					send_message_to_chat('❌Я не смогла установить вам никнейм из-за не предвиденной ошибки', id)
			elif not usedNickname == 0:
				send_message_to_chat('⚠️Данный никнейм занят', id)
			elif usedNickname == 0 and userWithNickname == 1: #нахождение человека с нужным айди и перезапись его никнейма
				currentNickname = 0
				with open(nickPath + '/' + str(rpId) + '.ini') as nickNumCheck:
					allNicknames = nickNumCheck.read().split('\n')
					linesNicks = len(allNicknames)
					nickNumCheck.close()
				with open(nickPath + '/' + str(rpId) + '.ini', 'w') as nickChange:
					while not currentNickname == linesNicks - 1:
						curNick = allNicknames[currentNickname]
						curNick = curNick.split('|')
						if str(event.obj.message['from_id']) == curNick[0]:
							nickSet = curNick[0] + '|' + nicknameNew + '\n'
							nickChange.write(nickSet)
							setNickDone = 1
						else:
							nickSet = allNicknames[currentNickname] + '\n'
							nickChange.write(nickSet)
						currentNickname = currentNickname + 1
					nickChange.close()
				if setNickDone == 1:
					with open(nickPath + '/' + str(rpId) + '.ini') as nickRead:
						allNicknames = nickRead.read().split('\n')
						linesNickNew = len(allNicknames)
						nickRead.close()
					currentNickname = 0
					while not currentNickname > linesNickNew - 1:
						curCheckNick = allNicknames[currentNickname - 1]
						curCheckNick = curCheckNick.split('|')
						if str(event.obj.message['from_id']) == curCheckNick[0]:
							userIdFromNick = curCheckNick[0]
							userNicknameFromNick = curCheckNick[1]
						currentNickname = currentNickname + 1
					try:
						mentPermission = 0
						with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
							mentionPermission = checkMentionPerm.read()
							checkMentionPerm.close()
						mentionPermission = mentionPermission.split('_')
						curUserCheckMentPerm = 0
						while curUserCheckMentPerm < len(mentionPermission):
							curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
							if curCheckMentPerm == str(event.obj.message['from_id']):
								mentPermission = 1
							else:
								pass
							curUserCheckMentPerm = curUserCheckMentPerm + 1
					except:
						mentPermission = 0
					if mentPermission == 0:
						send_message_to_chat('✅Ваш никнейм теперь - [id' + userIdFromNick + '|' + userNicknameFromNick + ']', id)
					if mentPermission == 1:
						send_message_to_chat('✅Ваш никнейм теперь - ' + userNicknameFromNick, id)
				else:
					try:
						with open(nickPath + '/' + str(rpId) + '.ini', 'w') as newNick:
							newNick.write(nicknamesBackup)
							newNick.close()
					except:
						send_message_to_chat('❗При восстановлении сохранённых никнеймов произошла ошибка. Возможно все никнеймы в этой беседе сбросились.\nПрошу прощения..', id)
					send_message_to_chat('❌Я не смогла перезаписать ваш никнейм', id)
		else:
			send_message_to_chat('⚠️Я не могу называть вас "пустышкой", укажите никнейм', id)
	elif message in delMyNickCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		curDelNick = 0
		delNickResult = ''
		delNickDone = 0
		try: #оболочка нужна для определения создан ли файл с никнеймами
			with open(nickPath + '/' + str(rpId) + '.ini', 'r') as nickDel: #проверка количества строк и в целом получение нужной инфы
				nicknamesBackup = nickDel.read()
				allNicknames = nicknamesBackup.split('\n')
				linesNickDel = len(allNicknames)
				nickDel.close()
			if not linesNickDel > 1: #если строк меньше 1(никаких никнеймов нет в файле) - вызывается исключение
				raise
			with open(nickPath + '/' + str(rpId) + '.ini', 'w') as nickDel: #перезапись в файл список никнеймов изменяя при этом его(удаляя указанный)
				while not curDelNick > linesNickDel - 2: #поиск и удаление нужного никнейма
					curNickname = allNicknames[curDelNick]
					curNickname = curNickname.split('|')
					if str(event.obj.message['from_id']) == curNickname[0]:
						delNickDone = 1
					else:
						delNickResult = allNicknames[curDelNick] + '\n'
						nickDel.write(delNickResult) #запись в файл результата изменений
					curDelNick = curDelNick + 1
				nickDel.close()
			if delNickDone == 1:
				send_message_to_chat('✅Ваш никнейм удален', id)
			if delNickDone == 0:
				send_message_to_chat('❌Никнейм не удален', id)
		except:
			try:
				with open(nickPath + '/' + str(rpId) + '.ini', 'w') as nickDel:
					nickDel.write(nicknamesBackup)
					nickDel.close()
			except:
				send_message_to_chat('❗При восстановлении сохранённых никнеймов произошла ошибка. Возможно все созданные в этой беседе никнеймы - стерлись.\nПрошу прощения..', id)
			send_message_to_chat('⚠️В вашей беседе нет сохранённых никнеймов', id)
	elif message in getRPList:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		rpListOut = 'Все созданные рп команды:\n'
		currentRPNum = 0
		try:
			with open(rpPath + '/' + str(rpId) + '.ini') as rpCmdsList:
				allRPCommands = rpCmdsList.read().split('\n')
				allRPLen = len(allRPCommands)
				rpCmdsList.close()
			while not currentRPNum == allRPLen - 1:
				currentRPCommand = allRPCommands[currentRPNum]
				currentRPCommand = currentRPCommand.split('-')
				rpListOut = rpListOut + str(currentRPNum + 1) + '. ' + currentRPCommand[0].capitalize() + ' <' + currentRPCommand[1] + '>\n'
				currentRPNum = currentRPNum + 1
			if not rpListOut == 'Все созданные рп команды:\n':
				send_message_to_chat(rpListOut, id)
			if rpListOut == 'Все созданные рп команды:\n':
				send_message_to_chat('⚠️В этой беседе пока что нет рп команд', id)
		except:
			send_message_to_chat('⚠️В этой беседе пока что нет рп команд', id)
	elif message in getNickList:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		nicknamesListOut = 'Все никнеймы в этой беседе:\n'
		currentNicknameNum = 0
		try:
			with open(nickPath + '/' + str(rpId) + '.ini') as nickList:
				allNicknames = nickList.read().split('\n')
				allNicksLen = len(allNicknames)
				nickList.close()
			while not currentNicknameNum == allNicksLen - 1:
				currentNick = allNicknames[currentNicknameNum]
				currentNick = currentNick.split('|')
				try:
					mentPermission = 0
					with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
						mentionPermission = checkMentionPerm.read()
						checkMentionPerm.close()
					mentionPermission = mentionPermission.split('_')
					curUserCheckMentPerm = 0
					while curUserCheckMentPerm < len(mentionPermission):
						curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
						if curCheckMentPerm == currentNick[0]:
							mentPermission = 1
						else:
							pass
						curUserCheckMentPerm = curUserCheckMentPerm + 1
				except:
					mentPermission = 0
				if mentPermission == 0:
					nicknamesListOut = nicknamesListOut + str(currentNicknameNum + 1) + '. [id' + currentNick[0] + '|' + currentNick[1] + ']' + '\n'
				if mentPermission == 1:
					nicknamesListOut = nicknamesListOut + str(currentNicknameNum + 1) + '. ' + currentNick[1] + '\n'
				currentNicknameNum = currentNicknameNum + 1
			if not nicknamesListOut == 'Все никнеймы в этой беседе:\n':
				send_message_to_chat(nicknamesListOut, id)
			if nicknamesListOut == 'Все никнеймы в этой беседе:\n':
				send_message_to_chat('⚠️В этой беседе нет сохранённых никнеймов', id)
		except:
			send_message_to_chat('⚠️В этой беседе нет сохранённых никнеймов', id)
	elif message in manageRpCommands:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Все доступные на данный момент команды, управляющие ролевыми командами:\n1. Дарки, создай рп команду <название>\n2. Дарки, удали рп команду <название>\n3. Дарки, установи рп действие', id)
	elif "Дурки" in message or "боты тупые" in message.lower() or "боты не имеют мозгов" in message.lower():
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Обидно ;с', id)
	elif "доброе утро" in message.lower() or "утра" in message.lower() or "добре" in message.lower() or "доброе" in message.lower():
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		goodMorningMessage = ['Доброе', 'Утра', 'Доброе утро', 'Привет', 'Преть']
		send_message_to_chat(random.choice(goodMorningMessage), id)
	elif "спокойной ночи" in message.lower() or "споки" in message.lower() or "споке" in message.lower():
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		sleepMessage = ['Споки', 'Добрых снов', 'Спокойной', 'Спокойной ночи', 'Ночки', 'Сладких снов']
		sleepRand = random.randint(0, len(sleepMessage))
		send_message_to_chat(sleepMessage[sleepRand - 1], id)
	elif message in aboutMeCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		with open(pathCV) as file:
			curVer = file.read()
		send_message_to_chat('⚙️' + curVer, id)
	elif message in updHystCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		with open(pathUH) as file:
			updHyst = file.read()
		send_message_to_chat('💾' + updHyst, id)
	elif message in curVerCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('⚙️Моя текущая версия - ' + currentVersion, id)
	elif message in helpCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Чтобы узнать мои команды - введите "Дарки, команды".\nЕсли вы хотите узнать информацию об отдельной команде - введите "Дарки, помощь <команда>"', id)
	elif message.startswith('Дарки, помощь') or message.startswith('Дарки помощь') or message.startswith('/darky_help'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			if message.startswith('Дарки,'):
				infoAboutComm = message.lstrip('Дарки,').lstrip(' ')
			if message.startswith('Дарки'):
				infoAboutComm = message.lstrip('Дарки').lstrip(' ')
			infoAboutComm = infoAboutComm.lstrip('помощь').lstrip(' ')
		elif message.startswith('/darky'):
			infoAboutComm = message.lstrip('/darky_help').lstrip(' =')
		iacomm = infoAboutComm
		if iacomm in startUpCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - предназначена для моего запуска если я ещё не совсем запущена.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in turnOffCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - предназначена для моего выключения если я запущена.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in restartCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - предназначена для моего перезапуска.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in updateCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - предназначена для вызова обновления моих скриптов.\n❗Доступна только разрешённым пользователям, таким как мой создатель.', id)
		elif iacomm in helpCommand:
			cmdType = random.randint(1, 4)
			if cmdType == 1:
				cmdIndex = random.randint(0, 2)
				cmdName = startUpCommand[cmdIndex]
			elif cmdType == 2:
				cmdIndex = random.randint(0, 6)
				cmdName = newRPCmd[cmdIndex]
			elif cmdType == 3:
				cmdIndex = random.randint(0, 4)
				cmdName = getNickList[cmdIndex]
			elif cmdType == 4:
				cmdIndex = random.randint(0, 2)
				cmdName = aboutMeCommand[cmdIndex]
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит информацию о команде если был добавлен соответствующий аргумент.\n❗Доступна всем пользователям.\n❔Пример использования:\n1.' + iacomm + ' ' + cmdName + '\n2.' + iacomm, id)
		elif iacomm in newRPCmd:
			if not iacomm.startswith('/'):
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - создаёт данную рп команду с пустым действием\n❗Доступна разрешённым пользователям и администраторам беседы\n❔Пример использования:\n' + iacomm + ' ' + random.choice(rpCmdsExample), id)
			else:
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - создаёт данную рп команду с пустым действием\n❗Доступна разрешённым пользователям и администраторам беседы\n❔Пример использования:\n' + iacomm + random.choice(rpCmdsExample), id)
		elif iacomm in delRPCmd:
			if not iacomm.startswith('/'):
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - удаляет данную рп команду\n❗Доступна разрешённым пользователям и администраторам беседы\n❔Пример использования:\n1. ' + iacomm + ' ' + random.choice(rpCmdsExample) + '\n2. ' + iacomm + ' ' + str(random.randint(0, 4)), id)
			else:
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - удаляет данную рп команду\n❗Доступна разрешённым пользователям и администраторам беседы\n❔Пример использования:\n1. ' + iacomm + random.choice(rpCmdsExample) + '\n2. ' + iacomm + str(random.randint(0, 4)), id)
		elif iacomm in setRpCmd:
			commandExample = random.randint(0, 4)
			if not iacomm.startswith('/'):
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - устанавливает действие для данной рп команды\n❗Доступна разрешённым пользователям и администраторам беседы\n❔Пример использования:\n1. ' + iacomm + ' ' + rpCmdsExample[commandExample] + ', ' + rpActionsExample[commandExample] + '\n2. ' + iacomm + ' ' + str(commandExample) + ', ' + rpActionsExample[commandExample], id)
			else:
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - устанавливает действие для данной рп команды\n❗Доступна разрешённым пользователям и администраторам беседы\n❔Пример использования:\n1. ' + iacomm + rpCmdsExample[commandExample] + ', ' + rpActionsExample[commandExample] + '\n2. ' + iacomm + str(commandExample) + ', ' + rpActionsExample[commandExample], id)
		elif iacomm in setNick:
			if not iacomm.startswith('/'):
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - устанавливает этот никнейм в качестве вашего\n❗Доступна всем пользователям\n❔Пример использования:\n1. ' + iacomm + ' ' + random.choice(nicknamesExample), id)
			else:
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - устанавливает этот никнейм в качестве вашего\n❗Доступна всем пользователям\n❔Пример использования:\n1. ' + iacomm + random.choice(nicknamesExample), id)
		elif iacomm in delMyNickCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - удаляет ваш текущий никнейм\n❗Доступна всем пользователям', id)
		elif iacomm in getNickList:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список использованных никнеймов в данной беседе\n❗Доступна всем пользователям', id)
		elif iacomm in getRPList:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список созданных рп команд в данной беседе включая названия команд и их id\n❗Доступна всем пользователям', id)
		elif iacomm in getCommandList:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список доступных команд бота\n❗Доступна всем пользователям', id)
		elif iacomm in callAllCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список участников беседы упоминая тех кто не отключил упоминания у Дарки\n❗Доступна всем пользователям', id)
		elif iacomm in manageRpCommands:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список команд для управления ролевыми командами\n❗Доступна всем пользователям', id)
		elif iacomm in curVerCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит текущую версию бота\n❗Доступна всем пользователям', id)
		elif iacomm in updHystCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит полную историю обновлений\n❗Доступна всем пользователям', id)
		elif iacomm in aboutMeCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит краткую информацию о себе\n❗Доступна всем пользователям', id)
		elif iacomm in randChooseCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выбирает одно из предложенных вариантов\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, выбери ' + random.choice(chooseExample) + ' или ' + random.choice(chooseExample), id)
		elif iacomm in probabilityCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит рандомную вероятность указанного события\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, вероятность ' + random.choice(probabilityExample), id)
		elif iacomm in tryCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - указывает было ли данное действие успешным или нет\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, попытка ' + random.choice(tryExample), id)
		elif iacomm in repeatCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - повторяет данный текст\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, скажи ' + random.choice(repeatExample), id)
		elif iacomm in distortMessageCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - искажает указанный текст\n❗Доступна всем пользователям\n❔Пример использования:\nДарки, искази текст: ' + random.choice(distortMessageExample), id)
		elif iacomm in mentionOn:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - включает упоминания ботом для текущего пользователя (изначально включено)\n❗Доступна всем пользователям', id)
		elif iacomm in mentionOff:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - отключает упоминания ботом для текущего пользователя (изначально включено)\n❗Доступна всем пользователям', id)
		elif iacomm in voiceCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - генерирует предложение из рандомных слов, иногда со смысолом\n❗Доступна всем пользователям', id)
		elif iacomm in voiceDataSize:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит размер собранных данных о текущей беседе\n❗Доступна всем пользователям', id)
		elif iacomm in clearVoiceData:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - очищает собранные данные о текущей беседе\n❗Доступна всем пользователям', id)
		elif iacomm in rollCube:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - бросает игральную кость и выводит выпавшее число\n❗Доступна всем пользователям', id)
		elif iacomm in checkCurBotStatus:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит текущий статус бота в беседе(участник/администратор)\n❗Доступна всем пользователям', id)
		elif iacomm in setNewGreetings:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - устанавливает пересланное из лс бота сообщение как приветствие(прикрепленные объекты поддерживаются, но не больше одного, даже если вы прикрепите две фотки в самом приветствии будет только первая)\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457248622_0732daf4e8d0c35da2,photo507365405_457248623_9c4c4fce9ce7f23ef8')
		elif iacomm in deleteGreeting:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - удаляет текущее приветствие беседы\n❗Доступна администраторам беседы и разрешённым пользователям', id)
		elif iacomm in setRulesCommand:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - устанавливает пересланное сообщение как правила(прикрепленные объекты не поддерживаются, даже если вы прикрепите что либо в самих правилах будет только текст)\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457248625_6468e7ebf7dd4c9512')
		elif iacomm in deleteRules:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - удаляет текущие правила беседы\n❗Доступна администраторам беседы и разрешённым пользователям', id)
		elif iacomm in curGreeting:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит текущее приветствие беседы\n❗Доступна всем пользователям', id)
		elif iacomm in curRules:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит текущие правила беседы\n❗Доступна всем пользователям', id)
		elif iacomm in kickUserCmd:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - исключает указанного пользователя из беседы\n❗Доступна администраторам и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457248681_ce4ea5544d161ced89,photo507365405_457248682_2a693eb989d17a02c9,photo507365405_457248683_ea1878d8a029641593,photo507365405_457248684_00cfeaaed3780ed379')
		elif iacomm in banUserCmd:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - вносит указанного пользователя в список забаненных и исключает, его если он в беседе. Пока пользователь забанен, бот не будет позволять ему зайти в беседу\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457248950_3182a2b450cb62c69d')
		elif iacomm in unbanUserCmd:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - убирает указанного пользователя из списка забаненных\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457248951_8c1a015598ba53df7a')
		elif iacomm in getRandomCount:
			randomStart = random.randint(-100, 100)
			randomEnd = random.randint(randomStart, 100)
			if not iacomm.startswith('/'):
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит рандомное число в указанном диапазоне\n❗Доступна всем пользователям\n❔Пример использования:\n' + iacomm + ' от ' + str(randomStart) + ' до ' + str(randomEnd), id)
			else:
				send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит рандомное число в указанном диапазоне\n❗Доступна всем пользователям\n❔Пример использования:\n' + iacomm + '=' + str(randomStart) + ', ' + str(randomEnd), id)
		elif iacomm in bannedListCommand:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список забаненных пользователей\n❗Доступна ', id)
		elif iacomm in warnCmd:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - выдаёт указанному пользователю предупреждение. При достижении максимального количества данного пользователя ждёт бан\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457249061_69ef3a27d6a34bc469')
		elif iacomm in unwarnCmd:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - снимает одно предупреждение у данного пользователя\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457249062_cd0e4b31b3ff4992de')
		elif iacomm in fullUserUnwarnCmd:
			send_message_to_chat_att('❕"' + iacomm + '" или другие вариации этой команды - снимает все предупреждения у данного пользователя\n❗Доступна администраторам беседы и разрешённым пользователям\n❔Пример использования:', id, 'photo507365405_457249063_342b835148b920930d')
		elif iacomm in fullUnwarnCmd:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - снимает у всех предупреждения\n❗Доступна администраторам беседы и разрешённым пользователям', id)
		elif iacomm in getWarnedUsersList:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит список пользователей с предупреждениями\n❗Доступна администраторам беседы и разрешённым пользователям', id)
		elif iacomm in checkMyWarns:
			send_message_to_chat('❕"' + iacomm + '" или другие вариации этой команды - выводит количество предупреждений у данного пользователя\n❗Доступна всем пользователям', id)
		else:
			send_message_to_chat('⚠️Я не нашла информацию об этой команде, возможно вы ошиблись в её написании', id)
	elif message.startswith('Дарки, кик') and adminStatus == 1 or message.startswith('Дарки кик') and adminStatus == 1 or message.startswith('/darky_kick') and adminStatus == 1:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				replyId = 0
				fwdId = 0
				textId = 0
				userId = 0
				if not event.obj.message['fwd_messages'] == []: #получение айди по первому пересланному сообщению
					fwdId = 1
					userId = event.obj.message['fwd_messages'][0]['from_id']
				else: #получение айди по упоминанию и тд.
					textId = 1
					userIdStr = message
					if message.startswith('Дарки'):
						userIdStr = userIdStr.lstrip('Дарки,').lstrip(' ').lstrip('кик').lstrip(' ')
						if userIdStr.startswith('['):
							userIdStr = userIdStr.lstrip('[id1234567890').lstrip('@*|').rstrip(']')
					elif message.startswith('/darky'):
						userIdStr = userIdStr.lstrip('/darky_kick').lstrip(' =')
						if userIdStr.startswith('['):
							userIdStr = userIdStr.lstrip('[id1234567890').lstrip('@*|').rstrip(']')
					chatMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
					countOfMembers = chatMembers['count']
					currUser = 0
					try:
						userId = 0
						while currUser < countOfMembers:
							if chatMembers['profiles'][currUser]['screen_name'] == userIdStr or 'id' + str(chatMembers['profiles'][currUser]['id']) == userIdStr or str(chatMembers['profiles'][currUser]['id']) == userIdStr:
								userId = chatMembers['profiles'][currUser]['id']
								break
							else:
								currUser = currUser + 1
					except:
						userId = 0
				try:
					if not event.obj.message['reply_message']['from_id'] == 0: #получение айди по ответу
						replyId = 1
						userId = event.obj.message['reply_message']['from_id']
				except:
					pass
				userFounded = 0
				try: #определение есть ли данный пользователь в беседе
					chatMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
					countOfMembers = chatMembers['count']
					currUser = 0
					while currUser < countOfMembers:
						if chatMembers['profiles'][currUser]['id'] == userId:
							userFounded = 1
							break
						else:
							currUser = currUser + 1
				except:
					userFounded = 0
				if userFounded == 1:
					if userId > 0:
						try:
							vk.messages.removeChatUser(chat_id = event.chat_id, user_id = userId)
							send_message_to_chat('✅Пользователь исключён', id)
						except:
							send_message_to_chat('❌Пользователь не исключён\nПричина: Данный пользователь - администратор беседы', id)
					else:
						send_message_to_chat('⚠️Данного пользователя нет в беседе', id)
				else:
					send_message_to_chat('⚠️Данного пользователя нет в беседе', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in banUserCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				replyMess = 0
				fwdMess = 0
				try: #получение айди пользователя которого нужно заблокировать
					bannedUser = event.obj.message['reply_message']['from_id']
					replyMess = 1
				except:
					try:
						replyMess = 0
						bannedUser = event.obj.message['fwd_messages'][0]['from_id']
						fwdMess = 1
					except:
						pass
				if replyMess == 1 or fwdMess == 1: #если айди был получен через ответы или пересланные сообшения - команда выполняется дальше
					if bannedUser > 0: #пользователи имеют положительный айди
						userAdmin = False
						try:
							allUsers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
							d = 0
							while d < len(allUsers):
								if allUsers['items'][d]['member_id'] == bannedUser:
									try:
										if allUsers['items'][accssRP]['is_admin'] == True:
											userAdmin = True
											break
									except:
										userAdmin = False
										break
								else:
									d = d + 1
						except:
							userAdmin = False
						try: # попытка кикнуть пользователя если он ещё в беседе
							vk.messages.removeChatUser(chat_id = event.chat_id, user_id = bannedUser) #удаление пользователя
							chatTitle = vk.messages.getConversationsById(peer_ids = 2000000000 + event.chat_id)['items'][0]['chat_settings']['title']
							send_message_to_user('⚠️Вы были исключены из беседы "' + chatTitle + '" поскольку получили там бан', bannedUser)
						except vk_api.exceptions.VkApiError:
							pass
						except:
							raise
						userAlreadyBanned = 0
						try: #проверка был ли уже пользователь забанен
							with open(blPath + '/' + str(rpId) + '.ini', 'r') as banList:
								allBannedUsers = banList.read().split('\n')
								banList.close()
							k = 0
							while k < len(allBannedUsers) - 1:
								if str(bannedUser) == allBannedUsers[k]:
									userAlreadyBanned = 1
									break
								else:
									k = k + 1
						except:
							userAlreadyBanned = 0
						if userAlreadyBanned == 0 and userAdmin == False:
							try:
								with open(blPath + '/' + str(rpId) + '.ini', 'a') as banList:
									banList.write(str(bannedUser) + '\n')
									banList.close()
							except:
								with open(blPath + '/' + str(rpId) + '.ini', 'w') as banList:
									banList.close()
								with open(blPath + '/' + str(rpId) + '.ini', 'a') as banList:
									banList.write(str(bannedUser) + '\n')
									banList.close()
							send_message_to_chat('✅Пользователь забанен навсегда', id)
						elif userAlreadyBanned == 0 and userAdmin == True:
							send_message_to_chat('⚠️Этот пользователь является администратором в данной беседе. Я не могу исключать их, банить и так далее', id)
						else:
							send_message_to_chat('⚠️Этот пользователь уже забанен в данной беседе', id)
					else:
						send_message_to_chat('❌Я могу забанить лишь пользователя, не бота или сообщество', id)
				else:
					send_message_to_chat('⚠️Для выполнения этой команды мне необходимо пересланное сообщение или ответ на сообщение пользователя, которого нужно забанить', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in unbanUserCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				replyMess = 0
				fwdMess = 0
				try: #получение айди пользователя которого нужно разблокировать
					bannedUser = event.obj.message['reply_message']['from_id']
					replyMess = 1
				except:
					try:
						replyMess = 0
						bannedUser = event.obj.message['fwd_messages'][0]['from_id']
						fwdMess = 1
					except:
						pass
				if replyMess == 1 or fwdMess == 1: #если айди был получен через ответы или пересланные сообшения - команда выполняется дальше
					if bannedUser > 0: #пользователи имеют положительный айди
						userAlreadyBanned = 0
						try: #проверка был ли уже пользователь забанен
							with open(blPath + '/' + str(rpId) + '.ini', 'r') as banList:
								backupBannedUsers = banList.read() #бэкап на случай ошибки при записи
								allBannedUsers = backupBannedUsers.split('\n')
								banList.close()
							k = 0
							while k < len(allBannedUsers) - 1:
								if str(bannedUser) == allBannedUsers[k]:
									userAlreadyBanned = 1
									break
								else:
									k = k + 1
						except:
							userAlreadyBanned = 0
						if userAlreadyBanned == 1:
							bannedUsersResult = ''
							k = 0
							while k < len(allBannedUsers) - 1:
								if str(bannedUser) == allBannedUsers[k]:
									pass
								else:
									bannedUsersResult = bannedUsersResult + allBannedUsers[k] + '\n'
								k = k + 1
							try:
								with open(blPath + '/' + str(rpId) + '.ini', 'w') as banList:
									banList.write(bannedUsersResult)
									banList.close()
								send_message_to_chat('✅Пользователь разбанен', id)
							except:
								with open(blPath + '/' + str(rpId) + '.ini', 'w') as banList:
									banList.write(backupBannedUsers)
									banList.close()
								send_message_to_chat('❌Произошла ошибка, список забаненных восстановлен', id)
						else:
							send_message_to_chat('⚠️Этого пользователя нет в списке забаненных', id)
					else:
						send_message_to_chat('❌Я могу разбанить лишь пользователя, не бота или сообщество', id)
				else:
					send_message_to_chat('⚠️Для выполнения этой команды мне необходимо пересланное сообщение или ответ на сообщение пользователя, которого нужно разбанить', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in bannedListCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				bannedUsersList = 'Забаненные пользователи в этой беседе:\n'
				k = 0
				try:
					with open(blPath + '/' + str(rpId) + '.ini', 'r') as banList:
						allBannedUsers = banList.read().split('\n')
						banList.close()
					while k < len(allBannedUsers) - 1:
						bannedUsersList = bannedUsersList + str(k + 1) + '. [id' + allBannedUsers[k] + '|' + allBannedUsers[k] + ']\n'
						k = k + 1
				except:
					bannedUsersList = 'Забаненные пользователи в этой беседе:\n'
				if bannedUsersList == 'Забаненные пользователи в этой беседе:\n':
					send_message_to_chat('⚠️В данной беседе нет забаненных пользователей', id)
				elif not bannedUsersList == 'Забаненные пользователи в этой беседе:\n':
					send_message_to_chat(bannedUsersList, id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in warnCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				replyMess = 0
				fwdMess = 0
				try: #получение айди пользователя которого нужно заварнить
					warnedUser = event.obj.message['reply_message']['from_id']
					replyMess = 1
				except:
					try:
						replyMess = 0
						warnedUser = event.obj.message['fwd_messages'][0]['from_id']
						fwdMess = 1
					except:
						pass
				if replyMess == 1 or fwdMess == 1: #если айди был получен через ответы или пересланные сообшения - команда выполняется дальше
					userAdmin = False
					try: #проверка админки у данного пользователя
						allMembers = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
						w = 0
						while w < allMembers['count']:
							if allMembers['items'][w]['member_id'] == warnedUser:
								try:
									userAdmin = allMembers['items'][w]['is_admin']
								except:
									userAdmin = False
								break
							else:
								w += 1
					except:
						userAdmin = False
					try: #проверка есть ли файл варнов
						with open(warnPath + '/' + str(rpId) + '.ini') as warnList:
							backupWarnList = warnList.read()
							warnList.close()
						warnedList = backupWarnList.split('\n')
					except: #создание файла варнов
						with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
							warnList.close()
						warnedList = ['507365405||0', '']
					try: #проверка количества варнов
						w = 0
						warnGet = False
						curWarnCount = 0
						while w < len(warnedList) - 1:
							if str(warnedUser) == warnedList[w].split('||')[0]:
								curWarnCount = int(warnedList[w].split('||')[1])
								warnGet = True
								break
							else:
								w += 1
					except:
						curWarnCount = 0
					if userAdmin == False:
						if warnGet == True and curWarnCount < 4:
							curWarnCount += 1
							warnListResult = ''
							w = 0
							while w < len(warnedList) - 1:
								if str(warnedUser) == warnedList[w].split('||')[0]:
									warnListResult = warnListResult + str(warnedUser) + '||' + str(curWarnCount) + '\n'
								else:
									warnListResult = warnListResult + warnedList[w] + '\n'
								w += 1
							try:
								with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
									warnList.write(warnListResult)
									warnList.close()
								send_message_to_chat('❕[id' + str(warnedUser) + '|Вы] получили ' + str(curWarnCount) + '/5 предупреждений.\nПри достижении максимального количества вы будете забанены', id)
							except:
								with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
									warnList.write(backupWarnList)
									warnList.close()
								send_message_to_chat('⚠️Произошла ошибка. Варны восстановлены', id)
						elif warnGet == True and curWarnCount > 3:
							curWarnCount += 1
							send_message_to_chat('❗[id' + str(warnedUser) + '|Вы] получили ' + str(curWarnCount) + '/5 предупреждений и будете забанены', id)
							event.obj.message['reply_message']['from_id'] = warnedUser
							init_message_from_chat('Дарки, бан', event.chat_id)
							warnListResult = ''
							w = 0
							while w < len(warnedList) - 1:
								if str(warnedUser) == warnedList[w].split('||')[0]:
									pass
								else:
									warnListResult = warnListResult + warnedList[w] + '\n'
								w += 1
							with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
								warnList.write(warnListResult)
								warnList.close()
						elif warnGet == False:
							curWarnCount += 1
							with open(warnPath + '/' + str(rpId) + '.ini', 'a') as warnList:
								warnList.write(str(warnedUser) + '||' + str(curWarnCount) + '\n')
								warnList.close()
							send_message_to_chat('❕[id' + str(warnedUser) + '|Вы] получили ' + str(curWarnCount) + '/5 предупреждений.\nПри достижении максимального количества вы будете забанены', id)
					else:
						send_message_to_chat('⚠️Этот пользователь является администратором в данной беседе. Я не могу исключать их, банить и так далее', id)
				else:
					send_message_to_chat('⚠️Для выполнения этой команды мне необходимо пересланное сообщение или ответ на сообщение пользователя, которому нужно выдать варн', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in unwarnCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				replyMess = 0
				fwdMess = 0
				try: #получение айди пользователя которого нужно разварнить
					warnedUser = event.obj.message['reply_message']['from_id']
					replyMess = 1
				except:
					try:
						replyMess = 0
						warnedUser = event.obj.message['fwd_messages'][0]['from_id']
						fwdMess = 1
					except:
						pass
				if replyMess == 1 or fwdMess == 1: #если айди был получен через ответы или пересланные сообшения - команда выполняется дальше
					warnFileExist = 0
					try: #проверка есть ли файл варнов
						with open(warnPath + '/' + str(rpId) + '.ini') as warnList:
							backupWarnList = warnList.read()
							warnList.close()
						warnedList = backupWarnList.split('\n')
						warnFileExist = 1
					except:
						warnFileExist = 0
					if warnFileExist == 1:
						try:
							w = 0
							while w < len(warnedList) - 1:
								if str(warnedUser) == warnedList[w].split('||')[0]:
									curWarnCount = int(warnedList[w].split('||')[1])
									break
								else:
									w += 1
							if curWarnCount > 1:
								curWarnCount -= 1
								w = 0
								unwarnListResult = ''
								while w < len(warnedList) - 1:
									if str(warnedUser) == warnedList[w].split('||')[0]:
										unwarnListResult = unwarnListResult + str(warnedUser) + '||' + str(curWarnCount) + '\n'
									else:
										unwarnListResult = unwarnListResult + warnedList[w]
									w += 1
								try:
									with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
										warnList.write(unwarnListResult)
										warnList.close()
									send_message_to_chat('✅Предупреждение снято, у данного пользователя теперь ' + str(curWarnCount) + '/5 предупреждений', id)
								except:
									with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
										warnList.write(backupWarnList)
										warnList.close()
									send_message_to_chat('⚠️Произошла ошибка. Варны восстановлены', id)
							elif curWarnCount < 2:
								w = 0
								unwarnListResult = ''
								while w < len(warnedList) - 1:
									if str(warnedUser) == warnedList[w].split('||')[0]:
										pass
									else:
										unwarnListResult = unwarnListResult + warnedList[w]
									w += 1
								try:
									with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
										warnList.write(unwarnListResult)
										warnList.close()
									send_message_to_chat('✅Предупреждение снято, у данного пользователя теперь нет предупреждений', id)
								except:
									with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
										warnList.write(backupWarnList)
										warnList.close()
									send_message_to_chat('⚠️Произошла ошибка. Варны восстановлены', id)
						except:
							send_message_to_chat('⚠️У данного пользователя нет предупреждений', id)
					elif warnFileExist == 0:
						send_message_to_chat('⚠️У данного пользователя нет предупреждений', id)
				else:
					send_message_to_chat('⚠️Для выполнения этой команды мне необходимо пересланное сообщение или ответ на сообщение пользователя, которому нужно снять предупреждение', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in fullUserUnwarnCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				replyMess = 0
				fwdMess = 0
				try: #получение айди пользователя которого нужно разварнить
					warnedUser = event.obj.message['reply_message']['from_id']
					replyMess = 1
				except:
					try:
						replyMess = 0
						warnedUser = event.obj.message['fwd_messages'][0]['from_id']
						fwdMess = 1
					except:
						pass
				if replyMess == 1 or fwdMess == 1: #если айди был получен через ответы или пересланные сообшения - команда выполняется дальше
					warnFileExist = 0
					try: #проверка есть ли файл варнов
						with open(warnPath + '/' + str(rpId) + '.ini') as warnList:
							backupWarnList = warnList.read()
							warnList.close()
						warnedList = backupWarnList.split('\n')
						warnFileExist = 1
					except:
						warnFileExist = 0
					if warnFileExist == 1:
						try:
							w = 0
							unwarnListResult = ''
							while w < len(warnedList) - 1:
								if str(warnedUser) == warnedList[w].split('||')[0]:
									pass
								else:
									unwarnListResult = unwarnListResult + warnedList[w]
								w += 1
							try:
								with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
									warnList.write(unwarnListResult)
									warnList.close()
								send_message_to_chat('✅Предупреждения сняты, у данного пользователя теперь нет предупреждений', id)
							except:
								with open(warnPath + '/' + str(rpId) + '.ini', 'w') as warnList:
									warnList.write(backupWarnList)
									warnList.close()
								send_message_to_chat('⚠️Произошла ошибка. Варны восстановлены', id)
						except:
							send_message_to_chat('⚠️У данного пользователя нет предупреждений', id)
					elif warnFileExist == 0:
						send_message_to_chat('⚠️У данного пользователя нет предупреждений', id)
				else:
					send_message_to_chat('⚠️Для выполнения этой команды мне необходимо пересланное сообщение или ответ на сообщение пользователя, которому нужно снять предупреждения', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in fullUnwarnCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				try:
					os.remove(warnPath + '/' + str(rpId) + '.ini')
					send_message_to_chat('✅Все предупреждения в этой беседе были сняты', id)
				except:
					send_message_to_chat('⚠️В данной беседе ни у кого нет ни одного предупреждения', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in getWarnedUsersList:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				try:
					with open(warnPath + '/' + str(rpId) + '.ini') as warnList:
						backupWarnList = warnList.read()
						warnList.close()
					if backupWarnList != '':
						warnedList = backupWarnList.split('\n')
						w = 0
						warnListResult = '❕Все пользователи с предупреждениями:\n'
						while w < len(warnedList) - 1:
							warnedUserId = warnedList[w].split('||')[0]
							curWarnCount = warnedList[w].split('||')[1]
							n = 0
							try: #получение имени и фамилии
								while n < allMembersOfChat['count']:
									if int(warnedUserId) == allMembersOfChat['profiles'][n]['id']:
										first_name = allMembersOfChat['profiles'][n]['first_name']
										last_name = allMembersOfChat['profiles'][n]['last_name']
										break
									else:
										n += 1
							except:
								first_name = 'user_id:'
								last_name = warnedUserId
							try: #проверка на разрешение упоминания
								mentPermission = 0
								with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
									mentionPermission = checkMentionPerm.read()
									checkMentionPerm.close()
								mentionPermission = mentionPermission.split('_')
								curUserCheckMentPerm = 0
								while curUserCheckMentPerm < len(mentionPermission):
									curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
									if curCheckMentPerm == warnedUserId:
										mentPermission = 1
									else:
										pass
									curUserCheckMentPerm = curUserCheckMentPerm + 1
							except:
								mentPermission = 0
							if mentPermission == 1:
								warnListResult = warnListResult + str(w + 1) + '. ' + first_name + ' ' + last_name + ' (' + str(curWarnCount) + '/5)\n'
							elif mentPermission == 0:
								warnListResult = warnListResult + str(w + 1) + '. [id' + warnedUserId + '|' + first_name + ' ' + last_name + '] ' + str(curWarnCount) + '/5\n'
							w += 1
						send_message_to_chat(warnListResult, id)
					else:
						send_message_to_chat('⚠️В данной беседе ни у кого нет ни одного предупреждения', id)
				except:
					send_message_to_chat('⚠️В данной беседе ни у кого нет ни одного предупреждения', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in checkMyWarns:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		try:
			with open(warnPath + '/' + str(rpId) + '.ini') as warnList:
				backupWarnList = warnList.read()
				warnList.close()
			if backupWarnList != '':
				warnedList = backupWarnList.split('\n')
				w = 0
				warnCount = 0
				while w < len(warnedList) - 1:
					if str(event.obj.message['from_id']) == warnedList[w].split('||')[0]:
						warnCount = warnedList[w].split('||')[1]
						break
					else:
						w += 1
				if warnCount != 0:
					send_message_to_chat('❕У вас ' + str(warnCount) + '/5 предупреждений', id)
				else:
					send_message_to_chat('⚠️У вас отсутствуют предупреждения в этой беседе', id)
			else:
				send_message_to_chat('⚠️У вас отсутствуют предупреждения в этой беседе', id)
		except:
			send_message_to_chat('⚠️У вас отсутствуют предупреждения в этой беседе', id)
	elif message in getCommandList:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		allCmdsOut = ''
		with open(mainPathDB + 'commandList.ini') as allCommands:
			allCmdsList = allCommands.read().split('\n\n')
			allCommands.close()
		allCmdsOut = allCmdsList[0] + '\n\n' + allCmdsList[1] + '\n\n' + allCmdsList[3]
		send_message_to_chat(allCmdsOut, id)
	elif 'тест' in message.lower() or 'test' in message.lower():
		if adminStatus == 1:
			secretTaken = 0
			usersWithSecret = vk.messages.getConversationMembers(peer_id = 2000000004)
			print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
			u = 0
			try:
				while not u > usersWithSecret['count']:
					if event.obj.message['from_id'] == usersWithSecret['profiles'][u]['id']:
						secretTaken = 1
						break
					else:
						u = u + 1
			except:
				secretTaken = 0
			if 'тест' in message.lower() and secretTaken == 0 or 'test' in message.lower() and secretTaken == 0:
				if message.lower() == 'тест2310':
					send_message_to_chat('Поздравляю! Вы получили секрет - ссылка на беседу где проводятся мои тесты, там вы можете раньше всех узнать о том, что будет добавлено в меня и увидеть часть процесса разработки', id)
					send_message_to_chat('https://vk.me/join/AJQ1d7SbHhdQs8BxnX7faLXp', id)
				elif message.lower() == 'тест' + bd_date:
					send_message_to_chat('Хорошая попытка, но подумайте лучше', id)
				else:
					bd_day_str = ''
					bd_month_str = ''
					bd_month = random.randint(1, 12)
					if not bd_month == 2:
						bd_day = random.randint(1, 31)
					else:
						bd_day = random.randint(1, 29)
					if bd_day == 23 and bd_month == 10:
						while bd_day == 23 and bd_month == 10:
							bd_month = random.randint(1, 12)
							if not bd_month == 2:
								bd_day = random.randint(1, 31)
							else:
								bd_day = random.randint(1, 29)
					if bd_day < 10:
						bd_day_str = '0' + str(bd_day)
					else:
						bd_day_str = str(bd_day)
					if bd_month < 10:
						bd_month_str = '0' + str(bd_month)
					else:
						bd_month_str = str(bd_month)
					bd_date = bd_day_str + bd_month_str
					send_message_to_chat('Вы почти у цели! Введите "тест" приписав к нему день рождения моего создателя без пробелов и точек.\nНапример "тест' + bd_date + '"', id)
	elif message.startswith("Дарки выбери") or message.startswith("Дарки, выбери"):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		choosingMess = event.obj.message['text']
		if message.startswith("Дарки выбери"):
			chooseStr = choosingMess.lstrip('Дарки ')
		if message.startswith("Дарки, выбери"):
			chooseStr = choosingMess.lstrip('Дарки, ')
		chooseStr = chooseStr.lstrip('выбери').lstrip(' ')
		chooseList = chooseStr.split(' или ')
		chooseListLen = len(chooseList)
		chooseRandInt = random.randint(0, chooseListLen)
		chooseResult = chooseList[chooseRandInt - 1]
		if chooseListLen > 1:
			send_message_to_chat('Я выбираю ' + chooseResult, id)
		else:
			send_message_to_chat('⚠️Я не могу выбрать что-либо поскольку мне дали либо один вариант ответа, либо мне не дали варианты ответа вообще', id)
	elif message.startswith('Дарки, вероятность') or message.startswith('Дарки вероятность'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		probabilityMess = event.obj.message['text']
		if message.startswith('Дарки, вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки, ')
		if message.startswith('Дарки вероятность'):
			probabilityStr = probabilityMess.lstrip('Дарки ')
		probabilityStr = probabilityStr.lstrip('вероятность').lstrip(' ')
		probabilityRandom = random.randint(0, 100)
		probabilityResult = str(probabilityRandom) + '%'
		if not probabilityStr == '':
			send_message_to_chat('Вероятность того, что ' + probabilityStr + ' составляет ' + probabilityResult, id)
		else:
			send_message_to_chat('⚠️Не могу просчитать вероятность, пожалуйста введите предложение после "Дарки, вероятность"', id)
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
			send_message_to_chat('❌Попытка' + tryStr + ' вышла неудачной', id)
		elif tryRandom == 1 and not tryStr == '':
			send_message_to_chat('✅Попытка' + tryStr + ' вышла удачной', id)
		else:
			send_message_to_chat('⚠️Пожалуйста укажите действие, дабы я решила, было ли оно удачным или же наоборот - неудачным', id)
	elif message.startswith('Дарки, искази текст') or message.startswith('Дарки искази текст') or message.startswith('/darky_distort='):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			if message.startswith('Дарки, '):
				distortMess = message.lstrip('Дарки, ')
			elif message.startswith('Дарки '):
				distortMess = message.lstrip('Дарки ')
			distortMess = distortMess.lstrip('искази ').lstrip('текст:').lstrip(' ')
		elif message.startswith('/darky'):
			distortMess = message.lstrip('/darky_distort').lstrip('=')
		distortMess = list(distortMess)
		distortMessageOut = distortMessage(distortMess)
		send_message_to_chat(distortMessageOut, id)
	elif message.startswith('Дарки, скажи') or message.startswith('Дарки скажи') or message.startswith('/darky_say='):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			if message.startswith('Дарки, '):
				repeatMess = message.lstrip('Дарки, ')
			elif message.startswith('Дарки '):
				repeatMess = message.lstrip('Дарки ')
			repeatMess = repeatMess.lstrip('скажи ')
		elif message.startswith('/darky'):
			repeatMess = message.lstrip('/darky_say').lstrip('=')
		send_message_to_chat(repeatMess, id)
	elif message in rollCube:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		diceRandom = random.randint(1, 6)
		send_message_to_chat('🎲На кубике выпало число: ' + str(diceRandom), id)
	elif message in voiceCommand:
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
		grammaticRand = random.randint(0, 10)
		if grammaticRand == 0:
			outMess = outMess.capitalize()
		elif grammaticRand == 1:
			outMess = outMess.upper()
		elif grammaticRand == 2:
			outMess = outMess.lower()
		if len(wordList) > 19:
			send_message_to_chat(outMess, id)
		elif len(wordList) < 20:
			send_message_to_chat('⚠️Я пока что собрала недостаточно данных для более менее хорошей генерации своих сообщений, дайте мне изучить беседу подольше и я обещаю, что смогу сгенерировать что-нибудь', id)
		i = 0
		outMess = ''
	elif message in clearVoiceData:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		send_message_to_chat('Очищаю собранные данные об этом диалоге...', id)
		with open(pathMess + '/' + str(event.chat_id) + '.ini', 'w') as messEarse:
			messEarse.close()
		send_message_to_chat('✅Данные очищены', id)
	elif message in voiceDataSize:
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
		send_message_to_chat('Размер собранных данных об этом диалоге составляет: ' + str(fSize) + ' ' + sizeTypeStr, id)
	elif message in checkCurBotStatus:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		darkyIsAdmin = 0
		try:
			checkCurStatus = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
			darkyIsAdmin = 1
		except:
			darkyIsAdmin = 0
		if darkyIsAdmin == 0:
			send_message_to_chat('Мой статус в этой беседе: участник', id)
		if darkyIsAdmin == 1:
			send_message_to_chat('Мой статус в этой беседе: администратор', id)
	elif message in mentionOff:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		try:
			with open(mainPathDB + 'usersMentionOff.ini', 'a') as mentionOffFile:
				mentionOffFile.close()
		except:
			with open(mainPathDB + 'usersMentionOff.ini', 'w') as mentionOffFile:
				mentionOffFile.close()
		try:
			with open(mainPathDB + 'usersMentionOff.ini') as mentionOffFile:
				checkMentionPermMode = mentionOffFile.read()
				mentionOffFile.close()
			try:
				m = 0
				mentionCurrModeOff = 0
				while m < len(checkMentionPermMode.split('_')):
					checkMentionPermModeSplit = checkMentionPermMode.split('_')
					curMentionCheckMode = checkMentionPermModeSplit[m]
					if curMentionCheckMode == str(event.obj.message['from_id']):
						mentionCurrModeOff = 1
					m = m + 1
			except:
				mentionCurrModeOff = 0
			if mentionCurrModeOff == 0:
				with open(mainPathDB + 'usersMentionOff.ini', 'a') as mentionOffFile:
					mentionOffFile.write(str(event.obj.message['from_id']) + '_')
					mentionOffFile.close()
				send_message_to_chat('✅Постараюсь не упоминать вас без нужды', id)
			else:
				send_message_to_chat('Я уже снизила ваше упоминание в моих сообщениях до минимума', id)
		except:
			send_message_to_chat('⚠️Произошла ошибка\n\nДополнительная информация:\n- - -\n' + getTraceback(), event.chat_id)
	elif message in mentionOn:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		try:
			foundedUserWithOffMention = 0
			with open(mainPathDB + 'usersMentionOff.ini') as mentionOnFile:
				mentionOffUsers = mentionOnFile.read()
				mentionOnFile.close()
			m = 0
			while m < len(mentionOffUsers.split('_')):
				mentionOffUsersSplit = mentionOffUsers.split('_')
				curMentionCheckMode = mentionOffUsersSplit[m]
				if curMentionCheckMode == str(event.obj.message['from_id']):
					foundedUserWithOffMention = 1
				m = m + 1
			if foundedUserWithOffMention == 1:
				with open(mainPathDB + 'usersMentionOff.ini', 'w') as mentionOnFile:
					m = 0
					while m < len(mentionOffUsers.split('_')) - 1:
						curUserChangePermMention = mentionOffUsersSplit[m]
						if curUserChangePermMention == str(event.obj.message['from_id']):
							pass
						else:
							mentionOnFile.write(mentionOffUsersSplit[m] + '_')
						m = m + 1
					mentionOnFile.close()
				send_message_to_chat('✅Я включила вам все упоминания в своих ответах', id)
			else:
				send_message_to_chat('❌Я не могу начать вас упоминать если у вас итак включены упоминания от меня', id)
		except:
			send_message_to_chat('⚠️Произошла ошибка\n\nДополнительная информация:\n- - -\n' + getTraceback(), event.chat_id)
	elif message in setNewGreetings:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			greetingFromPersMess = False
			try:
				currentGreetingMess = vk.messages.getHistory(user_id = event.obj.message['from_id'])
				greetingAttachmentAccessKey = currentGreetingMess['items'][0]['attachments'][0][currentGreetingMess['items'][0]['attachments'][0]['type']]['access_key']
				if currentGreetingMess['items'][0]['conversation_message_id'] == event.obj.message['fwd_messages'][0]['conversation_message_id']:
					greetingFromPersMess = True
				else:
					raise
			except:
				greetingFromPersMess = False
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				if not event.obj.message['fwd_messages'] == [] and greetingFromPersMess == True:
					greetingText = event.obj.message['fwd_messages'][0]['text']
					greetingAttachmentAccessKey = ''
					try: #получение актуального ключа
						currentGreetingMess = vk.messages.getHistoryAttachments(peer_id = event.obj.message['from_id'], media_type = event.obj.message['fwd_messages'][0]['attachments'][0]['type'], count = 1)
						greetingAttachmentAccessKey = currentGreetingMess['items'][0]['attachment'][currentGreetingMess['items'][0]['attachment']['type']]['access_key']
					except:
						pass
					greetingAttachment = ''
					greetingAttachment = currentGreetingMess['items'][0]['attachment']['type'] + str(currentGreetingMess['items'][0]['attachment'][currentGreetingMess['items'][0]['attachment']['type']]['owner_id']) + '_' + str(currentGreetingMess['items'][0]['attachment'][currentGreetingMess['items'][0]['attachment']['type']]['id'])
					if not greetingAttachmentAccessKey == '':
						greetingAttachment = greetingAttachment + '_' + greetingAttachmentAccessKey
					else:
						pass
					with open(greetingsPath + '/' + str(rpId) + '.ini', 'w') as setGreeting:
						setGreeting.write(greetingText + '||' + greetingAttachment)
						setGreeting.close()
					send_message_to_chat('✅Приветствие установлено', id)
				else:
					send_message_to_chat('⚠️Чтобы установить приветствие напишите его мне в личные сообщения и перешлите сюда написав ту же команду', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in deleteGreeting:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				try:
					os.remove(greetingsPath + '/' + str(rpId) + '.ini')
					send_message_to_chat('✅Приветствие удалено', id)
				except:
					send_message_to_chat('❌Приветствие не удалено, возможно оно ещё не установлено', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in updateGrAccssKeyCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				greetingIsExist = False
				try: #проверка существования приветствия
					with open(greetingsPath + '/' + str(rpId) + '.ini') as greetingCheck:
						greetingBackup = greetingCheck.read()
						greetingCheck.close()
					greetingIsExist = True
				except:
					greetingIsExist = False
				if greetingIsExist == True:
					try:
						currentStep = 'Получение данных о текущем приветствии...'
						print(currentStep)
						greetingText = greetingBackup.split('||')[0] #получение данных о приветствии
						attachmentType = greetingBackup.split('||')[1].split('_')[0].rstrip('1234567890')
						attachmentOwnerId = greetingBackup.split('||')[1].lstrip('qwertyuiopasdfghjklzxcvbnm_-').split('_')[0]
						attachmentId = greetingBackup.split('||')[1].lstrip('qwertyuiopasdfghjklzxcvbnm_-').split('_')[1]
						currentStep = 'Поиск актуальной информации о прикреплённом объекте...'
						print(currentStep)
						attachmentsList = vk.messages.getHistoryAttachments(peer_id = attachmentOwnerId, media_type = attachmentType, count = 50)
						n = 0
						updatedGreeting = ''
						while n < len(attachmentsList['items']):
							if attachmentsList['items'][n]['attachment'][attachmentsList['items'][n]['attachment']['type']]['id'] == int(attachmentId):
								currentStep = 'Изменение данных о текущем приветствии...'
								print(currentStep)
								attachmentAccessKey = ''
								try:
									attachmentAccessKey = '_' + attachmentsList['items'][n]['attachment'][attachmentsList['items'][n]['attachment']['type']]['access_key']
								except:
									pass
								updatedGreeting = greetingText + '||' + attachmentType + attachmentOwnerId + '_' + attachmentId + attachmentAccessKey
								break
							else:
								n += 1
						if updatedGreeting != '':
							currentStep = 'Перезапись текущего приветствия...'
							print(currentStep)
							try:
								with open(greetingsPath + '/' + str(rpId) + '.ini', 'w') as setNewGreeting:
									setNewGreeting.write(updatedGreeting)
									setNewGreeting.close()
								send_message_to_chat('✅Ключ доступа к прикреплённому объекту обновлён', id)
							except:
								with open(greetingsPath + '/' + str(rpId) + '.ini', 'w') as setNewGreeting:
									setNewGreeting.write(greetingBackup)
									setNewGreeting.close()
								send_message_to_chat('⚠️Произошла ошибка, предыдущее приветствие восстановлено', id)
						elif updatedGreeting == '':
							send_message_to_chat('⚠️Прикреплённый в вашем приветствии объект похоже был отправлен мне очень давно и я не смогла его найти. Пожалуйста установите приветствие заново во избежание его некорректной работы', id)
					except:
						send_message_to_chat('⚠️Произошла ошибка на этом этапе жанной комарды: ' + currentStep + '\n\nДополнительная информация:\n- - -\n' + getTraceback(), event.chat_id)
				else:
					send_message_to_chat('⚠️В вашей беседе нет установленного приветствия', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in updateGrAccssKeysCmd:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
			with open(pathAU, 'r') as adminUsersIds:
				auids = adminUsersIds.read()
				adminUsersIds.close()
			auids = auids.split('-')
			if str(event.obj.message['from_id']) in auids:
				greetingIsExist = False
				try:
					greetingList = os.listdir(greetingsPath)
					greetingIsExist = True
				except:
					greetingIsExist = False
				if greetingIsExist == True:
					i = 0
					updateGreetingsResult = ''
					while i < len(greetingList):
						try:
							print(greetingList[i])
							currentStep = 'Получение данных о текущем приветствии...'
							print(currentStep)
							with open(greetingsPath + '/' + greetingList[i]) as checkGreeting:
								greetingBackup = checkGreeting.read()
								checkGreeting.close()
							greetingText = greetingBackup.split('||')[0] #получение данных о приветствии
							attachmentType = greetingBackup.split('||')[1].split('_')[0].rstrip('1234567890')
							attachmentOwnerId = greetingBackup.split('||')[1].lstrip('qwertyuiopasdfghjklzxcvbnm_-').split('_')[0]
							attachmentId = greetingBackup.split('||')[1].lstrip('qwertyuiopasdfghjklzxcvbnm_-').split('_')[1]
							currentStep = 'Поиск актуальной информации о прикреплённом объекте...'
							print(currentStep)
							attachmentsList = vk.messages.getHistoryAttachments(peer_id = attachmentOwnerId, media_type = attachmentType, count = 200)
							n = 0
							updatedGreeting = ''
							while n < len(attachmentsList['items']):
								if attachmentsList['items'][n]['attachment'][attachmentsList['items'][n]['attachment']['type']]['id'] == int(attachmentId):
									currentStep = 'Изменение данных о текущем приветствии...'
									print(currentStep)
									attachmentAccessKey = ''
									try:
										attachmentAccessKey = '_' + attachmentsList['items'][n]['attachment'][attachmentsList['items'][n]['attachment']['type']]['access_key']
									except:
										pass
									updatedGreeting = greetingText + '||' + attachmentType + attachmentOwnerId + '_' + attachmentId + attachmentAccessKey
									break
								else:
									n += 1
							if updatedGreeting != '':
								currentStep = 'Перезапись текущего приветствия...'
								print(currentStep)
								try:
									with open(greetingsPath + '/' + greetingList[i], 'w') as setNewGreeting:
										setNewGreeting.write(updatedGreeting)
										setNewGreeting.close()
								except:
									with open(greetingsPath + '/' + greetingList[i], 'w') as setNewGreeting:
										setNewGreeting.write(greetingBackup)
										setNewGreeting.close()
									updateGreetingsResult += '⚠️Ошибка при перезаписи приветствия "' + greetingList[i] + '"\n'
							elif updatedGreeting == '':
								send_message_to_chat('⚠️Обнаружена некорректная работа вашего приветствия, настоятельно рекомендую установить его заново', greetingList[i].rstrip('.ini'))
						except:
							send_message_to_chat('⚠️Произошла ошибка на этом этапе данной команды: ' + currentStep + '\n\nДополнительная информация:\n- - -\n' + getTraceback(), event.chat_id)
						i += 1
					if updateGreetingsResult != '':
						send_message_to_chat(updateGreetingsResult, id)
					else:
						send_message_to_chat('✅Ключи доступа в приветствиях обновлены, приветствия перезаписаны', id)
				else:
					send_message_to_chat('⚠️В вашей беседе нет установленного приветствия', id)
			else:
				send_message_to_chat('⛔В доступе отказано', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in setRulesCommand:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				if not event.obj.message['fwd_messages'] == []:
					rulesText = str(event.obj.message['fwd_messages'][0]['text'])
					with open(rulePath + '/' + str(rpId) + '.ini', 'w') as setRule:
						setRule.write(rulesText)
						setRule.close()
					send_message_to_chat('✅Правила установлены', id)
				else:
					send_message_to_chat('⚠️Чтобы установить правила напишите их отдельным сообщением и перешлите сюда написав ту же команду', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in deleteRules:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if adminStatus == 1:
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
			if str(event.obj.message['from_id']) in auids or userIsAdmin == True:
				try:
					os.remove(rulePath + '/' + str(rpId) + '.ini')
					send_message_to_chat('✅Правила удалены', id)
				except:
					send_message_to_chat('❌Правила не удалены, возможно они ещё не установлены', id)
			else:
				send_message_to_chat('⛔В доступе отказано.\nВы не являетесь администратором', id)
		else:
			send_message_to_chat('⚠️Выполнение этой команды невозможно, пока у меня нет статуса администратора.', id)
	elif message in curRules:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		try:
			with open(rulePath + '/' + str(rpId) + '.ini') as rules:
				rulesText = rules.read()
				rules.close()
			send_message_to_chat(rulesText, id)
		except:
			send_message_to_chat('⚠️В данной беседе ещё не установлены правила', id)
	elif message in curGreeting:
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		try:
			with open(greetingsPath + '/' + str(event.chat_id) + '.ini') as greetingToChat:
				greeting = greetingToChat.read()
				greetingToChat.close()
			greetingText = greeting.split('||')[0]
			greetingAttachment = greeting.split('||')[1]
			send_message_to_chat_att(greetingText, event.chat_id, greetingAttachment)
		except:
			send_message_to_chat('⚠️В данной беседе ещё не установлено приветствие', id)
	elif message.startswith('Дарки, рандом') or message.startswith('Дарки рандом') or message.startswith('/darky_random'):
		print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
		if message.startswith('Дарки'):
			randomSize = message.lstrip('Дарки,').lstrip(' ').lstrip('рандом').lstrip(' ').lstrip('от').lstrip(' ').split(' до ')
		elif message.startswith('/darky'):
			randomSize = message.lstrip('/darky_random').lstrip('=').split(', ')
		if len(randomSize) == 2:
			try:
				randomResult = random.randint(int(randomSize[0]), int(randomSize[1]))
				send_message_to_chat('Рандомное число: ' + str(randomResult), id)
			except ValueError:
				send_message_to_chat('⚠️Вторая граница должна превышать первую', id)
		else:
			send_message_to_chat('⚠️Границы рандома должны быть указаны двумя числами разделёнными "до"', id)
	elif len(message.split(' ')) == 2:
		messWords = message.split(' ')
		if messWords[0].lower() in hiCommand and "Дарки" in message or messWords[1].lower() in hiCommand and "Дарки" in message:
			print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], ':', message)
			hiMessage = ['Преть', 'Привет']
			hiRand = random.randint(1, len(hiMessage))
			send_message_to_chat(hiMessage[hiRand - 1], id)

def updateAccssKeysInGreetings():
	greetingIsExist = False
	try:
		greetingList = os.listdir(greetingsPath)
		greetingIsExist = True
	except:
		greetingIsExist = False
	if greetingIsExist == True:
		i = 0
		updateGreetingsResult = ''
		while i < len(greetingList):
			try:
				print(greetingList[i])
				currentStep = 'Получение данных о текущем приветствии...'
				print(currentStep)
				with open(greetingsPath + '/' + greetingList[i]) as checkGreeting:
					greetingBackup = checkGreeting.read()
					checkGreeting.close()
				greetingText = greetingBackup.split('||')[0] #получение данных о приветствии
				attachmentType = greetingBackup.split('||')[1].split('_')[0].rstrip('1234567890')
				attachmentOwnerId = greetingBackup.split('||')[1].lstrip('qwertyuiopasdfghjklzxcvbnm_-').split('_')[0]
				attachmentId = greetingBackup.split('||')[1].lstrip('qwertyuiopasdfghjklzxcvbnm_-').split('_')[1]
				currentStep = 'Поиск актуальной информации о прикреплённом объекте...'
				print(currentStep)
				attachmentsList = vk.messages.getHistoryAttachments(peer_id = attachmentOwnerId, media_type = attachmentType, count = 200)
				n = 0
				updatedGreeting = ''
				while n < len(attachmentsList['items']):
					if attachmentsList['items'][n]['attachment'][attachmentsList['items'][n]['attachment']['type']]['id'] == int(attachmentId):
						currentStep = 'Изменение данных о текущем приветствии...'
						print(currentStep)
						attachmentAccessKey = ''
						try:
							attachmentAccessKey = '_' + attachmentsList['items'][n]['attachment'][attachmentsList['items'][n]['attachment']['type']]['access_key']
						except:
							pass
						updatedGreeting = greetingText + '||' + attachmentType + attachmentOwnerId + '_' + attachmentId + attachmentAccessKey
						break
					else:
						n += 1
				if updatedGreeting != '':
					currentStep = 'Перезапись текущего приветствия...'
					print(currentStep)
					try:
						with open(greetingsPath + '/' + greetingList[i], 'w') as setNewGreeting:
							setNewGreeting.write(updatedGreeting)
							setNewGreeting.close()
					except:
						with open(greetingsPath + '/' + greetingList[i], 'w') as setNewGreeting:
							setNewGreeting.write(greetingBackup)
							setNewGreeting.close()
						updateGreetingsResult += '⚠️Ошибка при перезаписи приветствия "' + greetingList[i] + '"\n'
				elif updatedGreeting == '':
					send_message_to_chat('⚠️Обнаружена некорректная работа вашего приветствия, настоятельно рекомендую установить его заново', greetingList[i].rstrip('.ini'))
			except:
				send_message_to_chat('⚠️Произошла ошибка на этом этапе обновления ключей доступа: ' + currentStep + '\n\nДополнительная информация:\n- - -\n' + getTraceback(), 507365405)
			i += 1
		if updateGreetingsResult != '':
			send_message_to_user(updateGreetingsResult, 507365405)
		else:
			send_message_to_user('✅Ключи доступа в приветствиях обновлены, приветствия перезаписаны', 507365405)
	else:
		send_message_to_user('⚠️Папка с приветствиями отсутствует', 507365405)

def diagnosticsScript():
	global adminStatus
	global rpId
	diagnosticsLog = ''
	diagnosticsLogPers = ''
	diagnosticsLogChat = ''
	event.obj.message['from_id'] = 270488028
	event.obj.message['fwd_messages'][0]['from_id'] = 270488028
	event.obj.message['fwd_messages'][0]['text'] = 'ыыы'
	print('Проверка личных сообщений...')
	i = 0
	while i < len(commandListPersMess):
		event.obj.message['text'] = commandListPersMess[i]
		try:
			init_message_from_user(commandListPersMess[i], 270488028)
		except:
			diagnosticsLogPers += '⚠️[ЛС]' + commandListPersMess[i] + ' - Может вывести из строя\n' + getTraceback()
		i += 1
	if diagnosticsLogPers == '':
		diagnosticsLog += '✅[ЛС] Проблем не обнаружено\n'
	else:
		diagnosticsLog += diagnosticsLogPers
	print('Проверка чатов...')
	rpId = 7
	event.chat_id = 7
	i = 0
	while i < len(commandListChatMess):
		event.obj.message['text'] = commandListChatMess[i]
		try:
			adminStatus = 0
			try:
				adminCheck = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
				adminStatus = 1
			except:
				pass
			init_message_from_chat(commandListChatMess[i], 7)
		except:
			diagnosticsLogChat += '⚠️[Беседы]' + commandListChatMess[i] + ' - Может вывести из строя\n' + getTraceback()
		i += 1
	if diagnosticsLogChat == '':
		diagnosticsLog += '✅[Беседы] Проблем не обнаружено\n'
	else:
		diagnosticsLog += diagnosticsLogChat
	print('Диагностика скрипта завершена, запись лога в файл...')
	with open(mainPathDB + 'diagnosticsResult.ini', 'w') as diagResult:
		diagResult.write(diagnosticsLog)
		diagResult.close()

print('Проверка необходимых файлов и директорий...')

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
checkDirsExist('*greetings', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'greetings')
		print(mainPathDB + 'greetings - created')
		checkDirsExist('*greetings', os.getcwd())
		greetingsPath = neededFoundedDirs[0]
		print(greetingsPath + ' - founded')
	except:
		pass
else:
	greetingsPath = neededFoundedDirs[0]
	print(greetingsPath + ' - founded')
checkDirsExist('*rules', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'rules')
		print(mainPathDB + 'rules - created')
		checkDirsExist('*rules', os.getcwd())
		rulePath = neededFoundedDirs[0]
		print(rulePath + ' - founded')
	except:
		pass
else:
	rulePath = neededFoundedDirs[0]
	print(rulePath + ' - founded')
checkDirsExist('*warns', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'warns')
		print(mainPathDB + 'warns - created')
		checkDirsExist('*warns', os.getcwd())
		warnPath = neededFoundedDirs[0]
		print(warnPath + ' - founded')
	except:
		pass
else:
	warnPath = neededFoundedDirs[0]
	print(warnPath + ' - founded')
checkDirsExist('*blacklists', os.getcwd())
if len(neededFoundedDirs) < 1:
	try:
		os.mkdir(mainPathDB + 'blacklists')
		print(mainPathDB + 'blacklists - created')
		checkDirsExist('*blacklists', os.getcwd())
		blPath = neededFoundedDirs[0]
		print(blPath + ' - founded')
	except:
		pass
else:
	blPath = neededFoundedDirs[0]
	print(blPath + ' - founded')
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
	
print('Файлы и директории прошли проверку!')

print('Проверка режима для запуска...')
diagnostics = False
try:
	with open(mainPathDB + 'diagnosticsStarted.ini') as diagnostic:
		diagnostic.close()
	os.remove(mainPathDB + 'diagnosticsStarted.ini')
	diagnostics = True
except:
	diagnostics = False
	
if diagnostics == True:
	print('Режим: Диагностика')
	print('Создание класса event для эмуляции событий...')
	class event:
		chat_id = 0
		class obj:
			message = {'text': '', 'from_id': 0, 'fwd_messages':[{'from_id': 0, 'text': ''}]}
	print('Начало диагностики...')
	with open(mainPathDB + 'startUp.ini', 'w') as startUpInfo:
		startUpInfo.close()
	diagnosticsScript()
	print('Завершение работы')
	raise SystemExit
else:
	print('Режим: Стандартный')

with open(mainPathDB + 'startUp.ini', 'w') as startUpInfo:
	startUpInfo.close()
print('Всё готово(' + currentVersion + ')')
bd_date = 'null'
while True:
	try:
		for event in botlongpoll.listen(): #своеобразное прослушивание новых событий
			adminStatus = 0
			#print(event)
			userIsBanned = False
			randGrAKUpd = random.randint(0, 20)
			if randGrAKUpd == 1:
				print('Обновление ключей доступа в приветствиях...')
				updateAccssKeysInGreetings()
				print('Готово')
			else:
				pass
			try:
				with open(blPath + '/' + str(event.chat_id) + '.ini') as banCheck:
					bannedUsers = banCheck.read().split('\n')
					banCheck.close()
				b = 0
				while b < len(bannedUsers) - 1:
					if event.obj.message['action']['member_id'] == int(bannedUsers[b]):
						userIsBanned = True
						break
					else:
						b = b + 1
			except:
				userIsBanned = False
			try:
				if event.obj.message['action']['type'] == 'chat_invite_user' and event.obj.message['action']['member_id'] == -192784148:
					print('chat:', event.chat_id, 'id:', event.obj.message['from_id'], '<bot added to chat>')
					send_message_to_chat_att('Спасибо за добавление в беседу\n\nЯ постараюсь быть максимально послушной не смотря на мои недоработки. Если вы нашли недоработку или ошибку в моей работе - сообщите моему [id507365405|создателю], написав ему в личные сообщения.\n\nЧтобы узнать мои команды - введите "Дарки, команды"\nДля вызова помощи - "Дарки, помощь".\n\nТакже я обнаружила, что пока не имею статус администратора, поэтому советую выдать мне его для успешной работы некоторых моих команд.\n\nВыдать мне администратора можно как с компьютера, так и с телефона, если вы с компьютера просто следуйте картинкам ниже, а если вы с телефона то выполните пункты ниже:\n1. Зайдите в вк через браузер.\n2. Активируйте версию для компьютера\n3. Также следуйте картинкам ниже.', event.chat_id, 'photo-192784148_457239027,photo-192784148_457239028,photo-192784148_457239029')
				elif event.obj.message['action']['type'] == 'chat_invite_user' and event.obj.message['action']['member_id'] < 0:
					replics = ['Зачем тут ещё один бот? ;·', 'Я наверняка лучше', 'Зачем тут ещё один бот? Я вам не нужна?', 'Мой функционал наверняка больше']
					send_message_to_chat(random.choice(replics), event.chat_id)
			except:
				pass
			try: #приветствие при новом пользователе
				if event.obj.message['action']['type'] == 'chat_invite_user' and event.obj.message['action']['member_id'] > 0 and userIsBanned == False or event.obj.message['action']['type'] == 'chat_invite_user_by_link' and event.obj.message['from_id'] > 0 and userIsBanned == False:
					with open(greetingsPath + '/' + str(event.chat_id) + '.ini') as greetingToChat:
						greeting = greetingToChat.read()
						greetingToChat.close()
					greetingText = greeting.split('||')[0]
					greetingAttachment = greeting.split('||')[1]
					try:
						mentPermission = 0
						with open(mainPathDB + 'usersMentionOff.ini') as checkMentionPerm:
							mentionPermission = checkMentionPerm.read()
							checkMentionPerm.close()
						mentionPermission = mentionPermission.split('_')
						curUserCheckMentPerm = 0
						while curUserCheckMentPerm < len(mentionPermission):
							curCheckMentPerm = mentionPermission[curUserCheckMentPerm]
							if curCheckMentPerm == str(event.obj.message['action']['member_id']):
								mentPermission = 1
							else:
								pass
							curUserCheckMentPerm = curUserCheckMentPerm + 1
					except:
						mentPermission = 0
					try:
						userInfo = vk.users.get(user_ids = event.obj.message['action']['member_id'])
						newUserFirstName = userInfo[0]['first_name']
					except:
						try:
							userInfo = vk.users.get(user_ids = event.obj.message['from_id'])
							newUserFirstName = userInfo[0]['first_name']
						except:
							send_message_to_chat('⚠️Произошла ошибка\n\nДополнительная информация:\n- - -\n' + getTraceback(), event.chat_id)
					if mentPermission == 0:
						try:
							greetingMention = '[id' + str(event.obj.message['action']['member_id']) + '|' + newUserFirstName + ',]\n'
						except:
							greetingMention = '[id' + str(event.obj.message['from_id']) + '|' + newUserFirstName + ',]\n'
					else:
						greetingMention = newUserFirstName + ',\n'
					send_message_to_chat_att(greetingMention + greetingText, event.chat_id, greetingAttachment)
				elif userIsBanned == True:
					bannedUser = event.obj.message['action']['member_id']
					try: # попытка кикнуть пользователя если он ещё в беседе
						vk.messages.removeChatUser(chat_id = event.chat_id, user_id = bannedUser) #удаление пользователя
						chatTitle = vk.messages.getConversationsById(peer_ids = 2000000000 + event.chat_id)['items'][0]['chat_settings']['title']
						send_message_to_user('⚠️Вы были исключены из беседы "' + chatTitle + '" поскольку получили там бан', bannedUser)
						send_message_to_chat('✅Данный [id' + str(bannedUser) + '|пользователь] забанен и был успешно исключён', event.chat_id)
					except:
						pass
			except:
				pass
			try:
				adminCheck = vk.messages.getConversationMembers(peer_id = 2000000000 + event.chat_id)
				adminStatus = 1
			except:
				pass
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
				init_message_from_chat(event.obj.message['text'], event.chat_id)
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
				init_message_from_user(event.obj.message['text'], event.obj.message['from_id'])
	except (TimeoutError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		randGrAKUpd = random.randint(0, 20)
		if randGrAKUpd == 1:
			print('Обновление ключей доступа в приветствиях...')
			updateAccssKeysInGreetings()
			print('Готово')
		else:
			pass
	except requests.exceptions.ConnectionError:
		print('Ожидание подключения...')
		time.sleep(5)
		try:
			send_message_to_user('✅Переподключение сети прошло успешно', 507365405)
		except:
			pass
	except KeyboardInterrupt:
		print()
		raise SystemExit
	except:
		send_message_to_user('⚠️Произошла ошибка\nМоя работа была приостановлена\n\nДополнительная информация:\n- - -\n' + getTraceback(), 507365405)
		try:
			input()
		except:
			pass
