print('Инициализация текущей версии...')
currentVersion = '3.0.0'

print('Импорт модулей...')
from vk_api.utils import get_random_id
import sys
import requests
import subprocess
import os
import signal
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import wget
from accessToken import accessToken
import fnmatch
import traceback
import time

print('Авторизация...')
group_id = 192784148
vk_session = vk_api.VkApi(token=accessToken) #авторизация как сообщество
botlongpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()

os.chdir('/storage/sdcard0')

urlCurVer = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/curVer.ini'
urlUpdHyst = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/updHyst.ini'
urlDB = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/darkyBot.py'
urlMB = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/mainBot.py'

print('Инициализация команд...')

startUpCommand = ['Дарки, запустись', 'Дарки запустись', '/darky_startUp']
turnOffCommand = ['Дарки, выключись', 'Дарки выключись', '/darky_turnOff']
restartCommand = ['Дарки, перезапустись', 'Дарки перезапустись', '/darky_restart']
updateCommand = ['Дарки, обновись', 'Дарки обновись', '/darky_update']
diagnosticsCommand = ['Дарки, диагностика', 'Дарки диагностика', 'Дарки, запусти диагностику', 'Дарки запусти диагностику', '/darky_diagnostics']

print('Загрузка классов...')

class StartUpTimeout:
	print('StartUpTimeout')

print('Загрузка функций...')

def send_message_to_user(message): #функция отвечающая за отправку сообщений пользователю
	vk.messages.send(user_id = event.obj.message['from_id'], random_id = get_random_id(), message = message)

def send_message_to_chat(message): #функция отвечающая за отправку сообщений в беседу
	vk.messages.send(chat_id = event.chat_id, random_id = get_random_id(), message = message)
    
mode = 0 #помогает скрипту определять включен ли бот, чтобы исключить повторное включение

darkyBotPID = 0#необходим для завершения процесса

diagnosticsStarts = 0 #укажет на режим запуска

neededFoundedFiles = []
foundedFiles = []

def checkFileExist(filename, pathToFile):
	global neededFoundedFiles
	foundedFiles = []
	for root, dirs, files in os.walk(pathToFile):
		for name in files:
			if fnmatch.fnmatch(name, filename):
				foundedFiles.append(os.path.join(root, name))
	n = 0
	neededFoundedFiles = []
	while not n == len(foundedFiles):
		if foundedFiles[n].endswith('/DarkyBot/' + filename.lstrip('*')):
			neededFoundedFiles.append(foundedFiles[n])
		n = n + 1

def init_message_from_user(message): #функция отвечающая за определение и выполнение команд от пользователя
	global mode
	global darkyBotPID
	global pathDB
	global pathMB
	global pathCV
	global pathAU
	global pathUH
	global darkyBotFileExist
	global darkyBotMode
	global diagnosticsStarts
	if message in startUpCommand: #команда запуска
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 0:
				print('start up...')
				send_message_to_user('Запускаюсь...')
				startUpTimerBegin = time.time()
				darkyBotMode = 0
				print('starting "darkyBot.py"...')
				if darkyBotFileExist == 1:
					try:
						darkyBot = subprocess.Popen('python ' + pathDB, shell=True, preexec_fn=os.setsid)
						darkyBotPID = darkyBot.pid
						checkFileExist('*startUp.ini', os.getcwd())
						if len(neededFoundedFiles) > 0:
							pathSU = neededFoundedFiles[0]
						try:
							os.remove(pathSU)
						except:
							pass
						while darkyBotMode == 0 and not time.time() - startUpTimerBegin > 30:
							pathStartUp = pathMB.rstrip('mainBot.py') + 'startUp.ini'
							try:
								with open(pathMB.rstrip('mainBot.py') + 'startUp.ini') as startUpCheck:
									startUpCheck.close()
								os.remove(pathStartUp)
								darkyBotMode = 1
							except:
								pass
					except:
						exc_type, exc_value, exc_traceback = sys.exc_info()
						tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
						tbOut = ''
						n = 0
						while n < len(tbObject):
							tbOut = tbOut + tbObject[n] + '\n\n'
							n = n + 1
						send_message_to_user('⚠️Не удалось запустить скрипт "darkyBot.py"\nПричина: В скрипте произошла ошибка\n\nДополнительная информация:\n- - -\n' + tbOut)
					if darkyBotMode == 1 and diagnosticsStarts == 0:
						mode = 1
						startUpTimerEnd = time.time()
						startUpTime = startUpTimerEnd - startUpTimerBegin
						startUpTime = round(startUpTime, 3)
						send_message_to_user('✅Я готова к работе\nПрошло: ' + str(startUpTime) + ' сек.')
					elif darkyBotMode == 1 and diagnosticsStarts == 1:
						mode = 1
						send_message_to_user('Скрипт запущен. Частичная проверка работоспособности...')
					else:
						send_message_to_user('❌Скрипт "darkyBot.py" не запустился, возможно в нём произошла ошибка')
				else:
					send_message_to_user('⚠️Не удалось запустить скрипт "darkyBot.py"\nПричина: Я не смогла найти этот файл в заданной директории')
			else:
				send_message_to_user('⚠️Я уже запущена и готова к работе')
		else:
			print('accss-err')
			send_message_to_user('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	if message in turnOffCommand: #команда выключения
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 1:
				print('turn off...')
				send_message_to_user('Выключаюсь...')
				try:
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
					mode = 0
					darkyBotMode = 0
					send_message_to_user('✅Выключение завершено')
				except:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
					tbOut = ''
					n = 0
					while n < len(tbObject):
						tbOut = tbOut + tbObject[n] + '\n\n'
						n = n + 1
					send_message_to_user('⚠️Выключение не было завершено из-за ошибки в коде\n\nДополнительная информация:\n- - -n' + tbOut)
			else:
				send_message_to_user('⚠️Я не могу выключиться если я не запущена')
		else:
			print('accss-err')
			send_message_to_user('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message in restartCommand:
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 1:
				crash = 0
				print('restarting...')
				send_message_to_user('Перезапускаюсь...')
				restartTimerBegin = time.time()
				try:
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
					mode = 0
					darkyBotMode = 0
					darkyBot = subprocess.Popen('python ' + pathDB, shell=True, preexec_fn=os.setsid)
					darkyBotPIDPID = darkyBot.pid
					checkFileExist('*startUp.ini', os.getcwd())
					if len(neededFoundedFiles) > 0:
						pathSU = neededFoundedFiles[0]
					try:
						os.remove(pathSU)
					except:
						pass
					while darkyBotMode == 0 and not time.time() - restartTimerBegin > 30:
						pathStartUp = pathMB.rstrip('mainBot.py') + 'startUp.ini'
						try:
							with open(pathMB.rstrip('mainBot.py') + 'startUp.ini') as startUpCheck:
								startUpCheck.close()
							os.remove(pathStartUp)
							darkyBotMode = 1
						except:
							pass
				except:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
					tbOut = ''
					n = 0
					while n < len(tbObject):
						tbOut = tbOut + tbObject[n] + '\n\n'
						n = n + 1
					send_message_to_user('⚠️При перезапуске произошла ошибка, осуществляю принудительное выключение...\n\nДополнительная информация:\n- - -\n' + tbOut)
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
					pathRestart = pathMB.rstrip('mainBot.py') + 'startUp.ini'
					os.remove(pathRestart)
					crash = 1
					send_message_to_user('✅Выключение завершено')
				if darkyBotMode == 1 and crash == 0:
					restartTimerEnd = time.time()
					restartTimer = restartTimerEnd - restartTimerBegin
					restartTimer = round(restartTimer, 3)
					mode = 1
					send_message_to_user('✅Я успешно перезапустилась и готова к работе\nПрошло: ' + str(restartTimer) + ' сек.')
				elif darkyBotMode == 0 and crash == 0:
					send_message_to_user('⚠️Скрипт "darkyBot.py" слишком долго запускался и мне пришлось прервать процесс перезапуска.\nВозможно в этом скрипте произошла ошибка')
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
			else:
				send_message_to_user('⚠️Я не могу перезапуститься если я не запущена')
		else:
			send_message_to_user('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message in updateCommand:
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 1:
				os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
			else:
				pass
			print('updating...')
			send_message_to_user('Обновляюсь, пожалуйста подождите...')
			updateTimerBegin = time.time()
			mode = 0
			darkyBotMode = 0
			print('updating "darkyBot.py"...')
			try:
				os.remove(pathDB)
				wget.download(urlDB, pathDB)
			except:
				send_message_to_user('⚠️При обновлении "darkyBot.py" произошла ошибка')
			print('updating "curVer.ini"...')
			try:
				os.remove(pathCV)
				wget.download(urlCurVer, pathCV)
			except:
				send_message_to_user('⚠️При обновлении "curVer.ini" произошла ошибка')
			print('updating "updHyst.ini"...')
			try:
				os.remove(pathUH)
				wget.download(urlUpdHyst, pathUH)
			except:
				send_message_to_user('⚠️При обновлении "updHyst.ini" произошла ошибка')
			send_message_to_user('Перезапись путей к обновлённым файлам...')
			darkyBotFileExist = 0
			checkFileExist('*darkyBot.py', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathDB = neededFoundedFiles[0]
				darkyBotFileExist = 1
			checkFileExist('*curVer.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathUH = neededFoundedFiles[0]
			checkFileExist('*updHyst.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathUH = neededFoundedFiles[0]
			send_message_to_user('Обновление завершено')
			send_message_to_user('Запускаюсь...')
			try:
				darkyBot = subprocess.Popen('python ' + pathDB, shell=True, preexec_fn=os.setsid)
				darkyBotPID = darkyBot.pid
				checkFileExist('*startUp.ini', os.getcwd())
				if len(neededFoundedFiles) > 0:
					pathSU = neededFoundedFiles[0]
				try:
					os.remove(pathSU)
				except:
					pass
				while darkyBotMode == 0 and not time.time() - updateTimerBegin > 120:
					pathStartUp = pathMB.rstrip('mainBot.py') + 'startUp.ini'
					try:
						with open(pathMB.rstrip('mainBot.py') + 'startUp.ini') as startUpCheck:
							startUpCheck.close()
						os.remove(pathStartUp)
						darkyBotMode = 1
					except:
						pass
			except:
				exc_type, exc_value, exc_traceback = sys.exc_info()
				tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
				tbOut = ''
				n = 0
				while n < len(tbObject):
					tbOut = tbOut + tbObject[n] + '\n\n'
					n = n + 1
				send_message_to_user('⚠️Не удалось запустить скрипт "darkyBot.py"\nПричина: В скрипте произошла ошибка\n\nДополнительная информация:\n- - -\n' + tbOut)
			if darkyBotMode == 1:
				mode = 1
				updateTimerEnd = time.time()
				updateTime = updateTimerEnd - updateTimerBegin
				updateTime = round(updateTime, 3)
				send_message_to_user('✅Я готова к работе\nПрошло: ' + str(updateTime) + ' сек.')
			else:
				send_message_to_user('❌Скрипт "darkyBot.py" не запустился, возможно в нём произошла ошибка')
		else:
			send_message_to_user('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message in diagnosticsCommand:
		diagnosticsStarts = 1
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			diagnosticsTimer = time.time()
			send_message_to_user('Диагностика запущена, пожалуйста подождите...')
			diagnosticsLog = 'Файлы:\n'
			checkFileExist('*mainBot.py', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathMB = neededFoundedFiles[0]
				diagnosticsLog += '✅mainBot.py - найден\n'
			else:
				diagnosticsLog += '⚠️mainBot.py - не найден\n'
			checkFileExist('*darkyBot.py', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathDB = neededFoundedFiles[0]
				diagnosticsLog += '✅darkyBot.py - найден\n'
			else:
				diagnosticsLog += '⚠️darkyBot.py - не найден\n'
			checkFileExist('*adminUsers.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathAU = neededFoundedFiles[0]
				diagnosticsLog += '✅adminUsers.ini - найден\n'
			else:
				diagnosticsLog += '⚠️adminUsers.ini - не найден\n'
			checkFileExist('*curVer.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathCV = neededFoundedFiles[0]
				diagnosticsLog += '✅curVer.ini - найден\n'
			else:
				diagnosticsLog += '⚠️curVer.ini - не найден\n'
			checkFileExist('*updHyst.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathUH = neededFoundedFiles[0]
				diagnosticsLog += '✅updHyst.ini - найден\n'
			else:
				diagnosticsLog += '⚠️updHyst.ini - не найден\n'
			importedScripts = False
			try:
				with open(pathMB.rstrip('mainBot.py') + 'diagnosticsStarted.ini', 'w') as diagnosticsMode:
					diagnosticsMode.close() 
				init_message_from_user('Дарки запустись')
				checkWork = False
				checkWorkTimer = time.time()
				diagnosticsStarts = 0
				while checkWork == False and time.time() - checkWorkTimer < 30:
					time.sleep(1)
					try:
						with open(pathMB.rstrip('mainBot.py') + 'diagnosticsResult.ini') as diagnosticsResult:
							diagnosticsResults = diagnosticsResult.read()
							diagnosticsResult.close()
						if diagnosticsResults != '':
							diagnosticsLog += '\nПроверка работоспособности:\n' + diagnosticsResults
						else:
							diagnosticsLog += '\nПроверка работоспособности:\n⚠️Информация отсутствует'
						os.remove(pathMB.rstrip('mainBot.py') + 'diagnosticsResult.ini')
						checkWork = True
					except:
						checkWork = False
				mode = 0
				darkyBotMode = 0
				if checkWork == True:
					send_message_to_user('Диагностика завершена\n\nРезультат диагностики:\n\n' + diagnosticsLog + '\n\nПрошло: ' + str(round(time.time() - diagnosticsTimer, 3)) + 'сек.')
				else:
					send_message_to_user('⚠️Максимальный лимит времени исчерпан\nДиагностика завершена\n\nРезультат диагностики:\n\n' + diagnosticsLog + '\nПрошло: ' + str(round(time.time() - diagnosticsTimer, 3)) + 'сек.')
			except:
				exc_type, exc_value, exc_traceback = sys.exc_info()
				tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
				tbOut = ''
				n = 0
				while n < len(tbObject):
					tbOut = tbOut + tbObject[n] + '\n\n'
					n = n + 1
				send_message_to_user('⚠️Не удалось запустить скрипт "darkyBot.py" в режиме диагностики\nПричина: В скрипте произошла ошибка\n\nДополнительная информация:\n- - -\n' + tbOut)
		else:
			send_message_to_user('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message.startswith('Дарки, обнови главный скрипт') or message.startswith('Дарки обнови главный скрипт'):
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 1:
				os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
			else:
				pass
			print('download "mainBot.py"...')
			send_message_to_user('Обновляю главный скрипт...')
			try:
				os.remove(pathMB)
			except:
				print('err')
			try:
				wget.download(urlMB, pathMB)
			except:
				print('err')
				send_message_to_user('Возникла ошибка при загрузке главного скрипта')
			subprocess.Popen(['python', pathMB])
			send_message_to_user('✅Обновление завершено')
			raise SystemExit
		else:
			send_message_to_user('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')

def init_message_from_chat(message): #функция отвечающая за определение и выполнение команд в беседе
	global mode
	global darkyBotPID
	global pathDB
	global pathMB
	global pathCV
	global pathAU
	global pathUH
	global darkyBotFileExist
	global darkyBotMode
	global diagnosticsStarts
	if message in startUpCommand: #команда запуска
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 0:
				print('start up...')
				send_message_to_chat('Запускаюсь...')
				startUpTimerBegin = time.time()
				darkyBotMode = 0
				print('starting "darkyBot.py"...')
				if darkyBotFileExist == 1:
					try:
						darkyBot = subprocess.Popen('python ' + pathDB, shell=True, preexec_fn=os.setsid)
						darkyBotPID = darkyBot.pid
						checkFileExist('*startUp.ini', os.getcwd())
						if len(neededFoundedFiles) > 0:
							pathSU = neededFoundedFiles[0]
						try:
							os.remove(pathSU)
						except:
							pass
						while darkyBotMode == 0 and not time.time() - startUpTimerBegin > 30:
							pathStartUp = pathMB.rstrip('mainBot.py') + 'startUp.ini'
							try:
								with open(pathMB.rstrip('mainBot.py') + 'startUp.ini') as startUpCheck:
									startUpCheck.close()
								os.remove(pathStartUp)
								darkyBotMode = 1
							except:
								pass
					except:
						exc_type, exc_value, exc_traceback = sys.exc_info()
						tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
						tbOut = ''
						n = 0
						while n < len(tbObject):
							tbOut = tbOut + tbObject[n] + '\n\n'
							n = n + 1
						send_message_to_chat('⚠️Не удалось запустить скрипт "darkyBot.py"\nПричина: В скрипте произошла ошибка\n\nДополнительная информация:\n- - -\n' + tbOut)
					if darkyBotMode == 1 and diagnosticsStarts == 0:
						mode = 1
						startUpTimerEnd = time.time()
						startUpTime = startUpTimerEnd - startUpTimerBegin
						startUpTime = round(startUpTime, 3)
						send_message_to_chat('✅Я готова к работе\nПрошло: ' + str(startUpTime) + ' сек.')
					elif darkyBotMode == 1 and diagnosticsStarts == 1:
						mode = 1
						send_message_to_chat('Скрипт запущен. Частичная проверка работоспособности...')
					else:
						send_message_to_chat('❌Скрипт "darkyBot.py" не запустился, возможно в нём произошла ошибка')
				else:
					send_message_to_chat('⚠️Не удалось запустить скрипт "darkyBot.py"\nПричина: Я не смогла найти этот файл в заданной директории')
			else:
				send_message_to_chat('⚠️Я уже запущена и готова к работе')
		else:
			print('accss-err')
			send_message_to_chat('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	if message in turnOffCommand: #команда выключения
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 1:
				print('turn off...')
				send_message_to_chat('Выключаюсь...')
				try:
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
					mode = 0
					darkyBotMode = 0
					send_message_to_chat('✅Выключение завершено')
				except:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
					tbOut = ''
					n = 0
					while n < len(tbObject):
						tbOut = tbOut + tbObject[n] + '\n\n'
						n = n + 1
					send_message_to_chat('⚠️Выключение не было завершено из-за ошибки в коде\n\nДополнительная информация:\n- - -n' + tbOut)
			else:
				send_message_to_chat('⚠️Я не могу выключиться если я не запущена')
		else:
			print('accss-err')
			send_message_to_chat('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message in restartCommand:
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 1:
				crash = 0
				print('restarting...')
				send_message_to_chat('Перезапускаюсь...')
				restartTimerBegin = time.time()
				try:
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
					mode = 0
					darkyBotMode = 0
					darkyBot = subprocess.Popen('python ' + pathDB, shell=True, preexec_fn=os.setsid)
					darkyBotPIDPID = darkyBot.pid
					checkFileExist('*startUp.ini', os.getcwd())
					if len(neededFoundedFiles) > 0:
						pathSU = neededFoundedFiles[0]
					try:
						os.remove(pathSU)
					except:
						pass
					while darkyBotMode == 0 and not time.time() - restartTimerBegin > 30:
						pathStartUp = pathMB.rstrip('mainBot.py') + 'startUp.ini'
						try:
							with open(pathMB.rstrip('mainBot.py') + 'startUp.ini') as startUpCheck:
								startUpCheck.close()
							os.remove(pathStartUp)
							darkyBotMode = 1
						except:
							pass
				except:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
					tbOut = ''
					n = 0
					while n < len(tbObject):
						tbOut = tbOut + tbObject[n] + '\n\n'
						n = n + 1
					send_message_to_chat('⚠️При перезапуске произошла ошибка, осуществляю принудительное выключение...\n\nДополнительная информация:\n- - -\n' + tbOut)
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
					pathRestart = pathMB.rstrip('mainBot.py') + 'startUp.ini'
					os.remove(pathRestart)
					crash = 1
					send_message_to_chat('✅Выключение завершено')
				if darkyBotMode == 1 and crash == 0:
					restartTimerEnd = time.time()
					restartTimer = restartTimerEnd - restartTimerBegin
					restartTimer = round(restartTimer, 3)
					mode = 1
					send_message_to_chat('✅Я успешно перезапустилась и готова к работе\nПрошло: ' + str(restartTimer) + ' сек.')
				elif darkyBotMode == 0 and crash == 0:
					send_message_to_chat('⚠️Скрипт "darkyBot.py" слишком долго запускался и мне пришлось прервать процесс перезапуска.\nВозможно в этом скрипте произошла ошибка')
					os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
			else:
				send_message_to_chat('⚠️Я не могу перезапуститься если я не запущена')
		else:
			send_message_to_chat('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message in updateCommand:
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			if mode == 1:
				os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
			else:
				pass
			print('updating...')
			send_message_to_chat('Обновляюсь, пожалуйста подождите...')
			updateTimerBegin = time.time()
			mode = 0
			darkyBotMode = 0
			print('updating "darkyBot.py"...')
			try:
				os.remove(pathDB)
				wget.download(urlDB, pathDB)
			except:
				send_message_to_chat('⚠️При обновлении "darkyBot.py" произошла ошибка')
			print('updating "curVer.ini"...')
			try:
				os.remove(pathCV)
				wget.download(urlCurVer, pathCV)
			except:
				send_message_to_user('⚠️При обновлении "curVer.ini" произошла ошибка')
			print('updating "updHyst.ini"...')
			try:
				os.remove(pathUH)
				wget.download(urlUpdHyst, pathUH)
			except:
				send_message_to_chat('⚠️При обновлении "updHyst.ini" произошла ошибка')
			send_message_to_chat('Перезапись путей к обновлённым файлам...')
			darkyBotFileExist = 0
			checkFileExist('*darkyBot.py', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathDB = neededFoundedFiles[0]
				darkyBotFileExist = 1
			checkFileExist('*curVer.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathUH = neededFoundedFiles[0]
			checkFileExist('*updHyst.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathUH = neededFoundedFiles[0]
			send_message_to_chat('Обновление завершено')
			send_message_to_chat('Запускаюсь...')
			try:
				darkyBot = subprocess.Popen('python ' + pathDB, shell=True, preexec_fn=os.setsid)
				darkyBotPID = darkyBot.pid
				checkFileExist('*startUp.ini', os.getcwd())
				if len(neededFoundedFiles) > 0:
					pathSU = neededFoundedFiles[0]
				try:
					os.remove(pathSU)
				except:
					pass
				while darkyBotMode == 0 and not time.time() - updateTimerBegin > 120:
					pathStartUp = pathMB.rstrip('mainBot.py') + 'startUp.ini'
					try:
						with open(pathMB.rstrip('mainBot.py') + 'startUp.ini') as startUpCheck:
							startUpCheck.close()
						os.remove(pathStartUp)
						darkyBotMode = 1
					except:
						pass
			except:
				exc_type, exc_value, exc_traceback = sys.exc_info()
				tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
				tbOut = ''
				n = 0
				while n < len(tbObject):
					tbOut = tbOut + tbObject[n] + '\n\n'
					n = n + 1
				send_message_to_chat('⚠️Не удалось запустить скрипт "darkyBot.py"\nПричина: В скрипте произошла ошибка\n\nДополнительная информация:\n- - -\n' + tbOut)
			if darkyBotMode == 1:
				mode = 1
				updateTimerEnd = time.time()
				updateTime = updateTimerEnd - updateTimerBegin
				updateTime = round(updateTime, 3)
				send_message_to_chat('✅Я готова к работе\nПрошло: ' + str(updateTime) + ' сек.')
			else:
				send_message_to_chat('❌Скрипт "darkyBot.py" не запустился, возможно в нём произошла ошибка')
		else:
			send_message_to_chat('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message in diagnosticsCommand:
		diagnosticsStarts = 1
		checkFileExist('*adminUsers.ini', os.getcwd())
		if not len(neededFoundedFiles) == 0:
			pathAU = neededFoundedFiles[0]
		with open(pathAU, 'r') as adminUsersIds:
			auids = adminUsersIds.read()
			adminUsersIds.close()
		auids = auids.split('-')
		print('user:', event.obj.message['from_id'], ':', message)
		if str(event.obj.message['from_id']) in auids:
			diagnosticsTimer = time.time()
			send_message_to_chat('Диагностика запущена, пожалуйста подождите...')
			diagnosticsLog = 'Файлы:\n'
			checkFileExist('*mainBot.py', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathMB = neededFoundedFiles[0]
				diagnosticsLog += '✅mainBot.py - найден\n'
			else:
				diagnosticsLog += '⚠️mainBot.py - не найден\n'
			checkFileExist('*darkyBot.py', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathDB = neededFoundedFiles[0]
				diagnosticsLog += '✅darkyBot.py - найден\n'
			else:
				diagnosticsLog += '⚠️darkyBot.py - не найден\n'
			checkFileExist('*adminUsers.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathAU = neededFoundedFiles[0]
				diagnosticsLog += '✅adminUsers.ini - найден\n'
			else:
				diagnosticsLog += '⚠️adminUsers.ini - не найден\n'
			checkFileExist('*curVer.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathCV = neededFoundedFiles[0]
				diagnosticsLog += '✅curVer.ini - найден\n'
			else:
				diagnosticsLog += '⚠️curVer.ini - не найден\n'
			checkFileExist('*updHyst.ini', os.getcwd())
			if len(neededFoundedFiles) > 0:
				pathUH = neededFoundedFiles[0]
				diagnosticsLog += '✅updHyst.ini - найден\n'
			else:
				diagnosticsLog += '⚠️updHyst.ini - не найден\n'
			importedScripts = False
			try:
				with open(pathMB.rstrip('mainBot.py') + 'diagnosticsStarted.ini', 'w') as diagnosticsMode:
					diagnosticsMode.close() 
				init_message_from_chat('Дарки запустись')
				checkWork = False
				checkWorkTimer = time.time()
				diagnosticsStarts = 0
				while checkWork == False and time.time() - checkWorkTimer < 30:
					time.sleep(1)
					try:
						with open(pathMB.rstrip('mainBot.py') + 'diagnosticsResult.ini') as diagnosticsResult:
							diagnosticsResults = diagnosticsResult.read()
							diagnosticsResult.close()
						if diagnosticsResults != '':
							diagnosticsLog += '\nПроверка работоспособности:\n' + diagnosticsResults
						else:
							diagnosticsLog += '\nПроверка работоспособности:\n⚠️Информация отсутствует'
						os.remove(pathMB.rstrip('mainBot.py') + 'diagnosticsResult.ini')
						checkWork = True
					except:
						checkWork = False
				mode = 0
				darkyBotMode = 0
				if checkWork == True:
					send_message_to_chat('Диагностика завершена\n\nРезультат диагностики:\n\n' + diagnosticsLog + '\n\nПрошло: ' + str(round(time.time() - diagnosticsTimer, 3)) + 'сек.')
				else:
					send_message_to_chat('⚠️Максимальный лимит времени исчерпан\nДиагностика завершена\n\nРезультат диагностики:\n\n' + diagnosticsLog + '\nПрошло: ' + str(round(time.time() - diagnosticsTimer, 3)) + 'сек.')
			except:
				exc_type, exc_value, exc_traceback = sys.exc_info()
				tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
				tbOut = ''
				n = 0
				while n < len(tbObject):
					tbOut = tbOut + tbObject[n] + '\n\n'
					n = n + 1
				send_message_to_chat('⚠️Не удалось запустить скрипт "darkyBot.py" в режиме диагностики\nПричина: В скрипте произошла ошибка\n\nДополнительная информация:\n- - -\n' + tbOut)
		else:
			send_message_to_chat('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message.startswith('Дарки, обнови главный скрипт') or message.startswith('Дарки обнови главный скрипт'):
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 1:
				os.killpg(os.getpgid(darkyBotPID), signal.SIGTERM)
			else:
				pass
			print('download "mainBot.py"...')
			send_message_to_chat('Обновляю главный скрипт...')
			try:
				os.remove(pathMB)
			except:
				print('err')
			try:
				wget.download(urlMB, pathMB)
			except:
				print('err')
				send_message_to_user('Возникла ошибка при загрузке главного скрипта')
			subprocess.Popen(['python', pathMB])
			send_message_to_chat('✅Обновление завершено')
			raise SystemExit
		else:
			send_message_to_chat('⛔В доступе отказано, свяжитесь с моим [darky_wings|создателем]')

print('Проверка файлов...')

darkyBotFileExist = 0

checkFileExist('*mainBot.py', os.getcwd())
if len(neededFoundedFiles) > 0:
	pathMB = neededFoundedFiles[0]
	print(pathMB + ' - founded')
else:
	print('file "mainBot.py" not found!')

checkFileExist('*darkyBot.py', os.getcwd())
if len(neededFoundedFiles) > 0:
	pathDB = neededFoundedFiles[0]
	darkyBotFileExist = 1
	print(pathDB + ' - founded')
else:
	print('file "darkyBot.py" not found!')
	
checkFileExist('*adminUsers.ini', os.getcwd())
if len(neededFoundedFiles) > 0:
	pathAU = neededFoundedFiles[0]
	print(pathAU + ' - founded')
else:
	print('file "adminUsers.ini" not found!')
	
checkFileExist('*curVer.ini', os.getcwd())
if len(neededFoundedFiles) > 0:
	pathCV = neededFoundedFiles[0]
	print(pathCV + ' - founded')
else:
	print('file "curVer.ini" not found!')

checkFileExist('*updHyst.ini', os.getcwd())
if len(neededFoundedFiles) > 0:
	pathUH = neededFoundedFiles[0]
	print(pathUH + ' - founded')
else:
	print('file "updHyst.ini" not found!')

print('Всё готово(' + currentVersion + ')')
while True:
	try:
		for event in botlongpoll.listen(): #своеобразное прослушивание новых сообщений
			if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
				init_message_from_user(event.obj.message['text'])
			elif event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
				init_message_from_chat(event.obj.message['text'])
	except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
		pass
	except KeyboardInterrupt:
		print()
		raise SystemExit
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		tbObject = traceback.format_exception(exc_type, exc_value, exc_traceback, limit = 5)
		tbOut = ''
		c = 0
		while c < len(tbObject):
			tbOut = tbOut + tbObject[c] + '\n\n'
			c = c + 1
		vk.message.send(user_id = 507365405, random_id = get_random_id(), message = '⚠️Произошла ошибка\nМоя работа была приостановлена\n\nДополнительная информация:\n- - -\n' + tbOut)
		try:
			input()
		except:
			pass
