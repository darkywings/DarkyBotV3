print('importing "get_random_id"...')
from vk_api.utils import get_random_id

print('importing "sys"...')
import sys

print('importing "subprocess"...')
import subprocess

print('importing "os"...')
import os

print('importing "signal"...')
import signal

print('importing "vk_api"...')
import vk_api

print('importing "VkLongPoll" and "VkEventType"...')
from vk_api.longpoll import VkLongPoll, VkEventType

print('importing "wget"...')
import wget

print('importing "accessToken"...')
from accessToken import accessToken

print('authorization...')
group_id = 192784148
vk_session = vk_api.VkApi(token=accessToken) #авторизация как сообщество
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

print('checking files...')

pmFileExist = 0
cmFileExist = 0

'''pathCV = os.path.abspath('curVer.ini ')
pathUH = os.path.abspath('updHyst.ini ')
pathMB = os.path.abspath('mainBot.py ')
pathPM = os.path.abspath('pm.py ')
pathCM = os.path.abspath('cm.py ')'''
pathCV = '/storage/sdcard0/DarkyBot/curVer.ini'
pathUH = '/storage/sdcard0/DarkyBot/updHyst.ini'
pathMB = '/storage/sdcard0/DarkyBot/mainBot.py'
pathPM = '/storage/sdcard0/DarkyBot/pm.py'
pathCM = '/storage/sdcard0/DarkyBot/cm.py'

try:
	with open(pathPM, 'r') as personalMessages:
		pmPython = personalMessages.read()
		pmFileExist = 1
		personalMessages.close()
except:
	print('err: file "pm.py" not found')

try:
	with open(pathCM, 'r') as chatMessages:
		cmPython = chatMessages.read()
		cmFileExist = 1
		chatMessages.close()
except:
	print('err: file "cm.py" not found')

print('files are checked!')

print('creating functions...')

def send_message_to_user(message): #функция отвечающая за отправку сообщений пользователю
    random_id = get_random_id(),
    user_id = int(event.user_id)

    vk.messages.send(
        random_id=random_id,
        user_id=user_id,
        message=message
    )
    
mode = 0 #помогает скрипту определять включен ли бот, чтобы исключить повторное включение

pmPID = 0
cmPID = 0
#оба необходимы для завершения процессов

urlCurVer = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/curVer.ini'
urlUpdHyst = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/updHyst.ini'
urlPM = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/pm.py'
urlCM = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/cm.py'
urlMB = 'https://raw.githubusercontent.com/skanim-sdw/DarkyBot/master/mainBot.py'

def init_message_from_user(message): #функция отвечающая за определение и выполнение команд
	global mode
	global pmPID
	global cmPID
	if message.startswith('Дарки, запустись') or message.startswith('Дарки запустись'): #команда запуска
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 0:
				mode = mode + 1
				print('turning on...')
				send_message_to_user('Запускаюсь...')
				print('starting "cm.py"...')
				if cmFileExist == 1:
					try:
						cm = subprocess.Popen('python ' + pathCM, shell=True, preexec_fn=os.setsid)
						cmPID = cm.pid
						send_message_to_user('Скрипт "cm.py" успешно запущен')
					except:
						send_message_to_user('Не удалось запустить файл "cm.py"\nПричина: В данном скрипте произошла ошибка')
				else:
					print('err')
					send_message_to_user('Не удалось запустить файл "cm.py"\nПричина: Я не смогла найти этот файл в заданной директории')
				print('starting "pm.py"...')
				if pmFileExist == 1:
					try:
						pm = subprocess.Popen('python ' + pathPM, shell=True, preexec_fn=os.setsid)
						pmPID = pm.pid
						send_message_to_user('Скрипт "pm.py" успешно запущен')
					except:
						send_message_to_user('Не удалось запустить файл "pm.py"\nПричина: В данном скрипте произошла ошибка')
				else:
					print('err')
					send_message_to_user('Не удалось запустить файл "pm.py"\nПричина: Я не смогла найти этот файл в заданной директории')
				if cmFileExist == 1 and pmFileExist == 1:
					send_message_to_user('Я готова к работе')
				else:
					send_message_to_user('Стабильность и правильность моей работы не гарантирую, но я готова к работе')
			else:
				send_message_to_user('Я уже запущена и готова к работе')
		else:
			print('accss-err')
			send_message_to_user('В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message.startswith('Дарки, выключись') or message.startswith('Дарки выключись'): #команда выключения
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 1:
				mode = mode - 1
				print('turn off...')
				send_message_to_user('Выключаюсь...')
				try:
					os.killpg(os.getpgid(pmPID), signal.SIGTERM)
					os.killpg(os.getpgid(cmPID), signal.SIGTERM)
					send_message_to_user('Выключение завершено')
				except:
					send_message_to_user('Выключение не было завершено из-за ошибки в коде')
			else:
				send_message_to_user('Я не могу выключиться если я не запущена')
		else:
			print('accss-err')
			send_message_to_user('В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message.startswith('Дарки, перезапустись') or message.startswith('Дарки перезапустись'):
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 1:
				print('restarting...')
				send_message_to_user('Перезапускаюсь...')
				try:
					os.killpg(os.getpgid(pmPID), signal.SIGTERM)
					os.killpg(os.getpgid(cmPID), signal.SIGTERM)
					pm = subprocess.Popen('python ' + pathPM, shell=True, preexec_fn=os.setsid)
					cm = subprocess.Popen('python ' + pathCM, shell=True, preexec_fn=os.setsid)
					pmPID = pm.pid
					cmPID = cm.pid
					send_message_to_user('Я успешно перезапустилась и готова к работе')
				except:
					send_message_to_user('При перезапуске произошла ошибка, осуществляю принудительное выключение...')
					os.killpg(os.getpgid(pmPID), signal.SIGTERM)
					os.killpg(os.getpgid(cmPID), signal.SIGTERM)
					send_message_to_user('Выключение завершено')
			else:
				send_message_to_user('Я не могу перезапуститься если я не запущена')
		else:
			send_message_to_user('В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message.startswith('Дарки, обновись') or message.startswith('Дарки обновись'):
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 1:
				print('updating...')
				send_message_to_user('Обновляюсь, пожалуйста подождите...')
				os.killpg(os.getpgid(pmPID), signal.SIGTERM)
				os.killpg(os.getpgid(cmPID), signal.SIGTERM)
				send_message_to_user('Загружаю файлы...')
				send_message_to_user('pm.py')
				try:
					os.remove(pathPM)
				except:
					print('delete err')
				print('downloading "pm.py"...')
				try:
					wget.download(urlPM, pathPM)
				except:
					print('err')
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('cm.py')
				try:
					os.remove(pathCM)
				except:
					print('delete err')
				print('downloading "cm.py"...')
				try:
					wget.download(urlCM, pathCM)
				except:
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('curVer.ini')
				try:
					os.remove(pathCV)
				except:
					print('delete err')
				print('downloading "curVer.ini"...')
				try:
					wget.download(urlCurVer, pathCV)
				except:
					print('err')
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('updHyst.ini')
				try:
					os.remove(pathUH)
				except:
					print('delete err')
				print('downloading "updHyst.ini"...')
				try:
					wget.download(urlUpdHyst, pathUH)
				except:
					print('err')
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('Обновление завершено')
				send_message_to_user('Запускаюсь...')
				try:
					pm = subprocess.Popen('python ' + pathPM, shell=True, preexec_fn=os.setsid)
					cm = subprocess.Popen('python ' + pathCM, shell=True, preexec_fn=os.setsid)
					pmPID = pm.pid
					cmPID = cm.pid
					send_message_to_user('Я готова к работе')
				except:
					send_message_to_user('При запуске произошла ошибка')
			elif mode == 0:
				send_message_to_user('Обновляюсь, пожалуйста подождите...')
				send_message_to_user('Загружаю файлы...')
				send_message_to_user('pm.py')
				try:
					os.remove(pathPM)
				except:
					print('delete err')
				print('downloading "pm.py"...')
				try:
					wget.download(urlPM, pathPM)
				except:
					print('err')
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('cm.py')
				try:
					os.remove(pathCM)
				except:
					print('delete err')
				print('downloading "cm.py"...')
				try:
					wget.download(urlCM, pathCM)
				except:
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('curVer.ini')
				try:
					os.remove(pathCV)
				except:
					print('delete err')
				print('downloading "curVer.ini"...')
				try:
					wget.download(urlCurVer, pathCV)
				except:
					print('err')
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('updHyst.ini')
				try:
					os.remove(pathUH)
				except:
					print('delete err')
				print('downloading "updHyst.ini"...')
				try:
					wget.download(urlUpdHyst, pathUH)
				except:
					print('err')
					send_message_to_user('При загрузке данного файла произошла ошибка')
				send_message_to_user('Обновление завершено')
		else:
			send_message_to_user('В доступе отказано, свяжитесь с моим [darky_wings|создателем]')
	elif message.startswith('Дарки, проверь наличие своих файлов') or message.startswith('Дарки проверь наличие своих файлов'):
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			send_message_to_user('Проверяю...')
			try:
				with open(pathCM) as cmCont:
					cmPY = cmCont.read()
					cmCont.close()
					send_message_to_user('Файл "cm.py" найден')
			except:
				send_message_to_user('Файл "cm.py" не найден')
			try:
				with open(pathPM) as pmCont:
					pmPY = pmCont.read()
					pmCont.close()
					send_message_to_user('Файл "pm.py" найден')
			except:
				send_message_to_user('Файл "pm.py" не найден')
			try:
				with open(pathCV) as curVerCont:
					curVerFile = curVerCont.read()
					curVerCont.close()
					send_message_to_user('Файл "curVer.ini" найден')
			except:
				send_message_to_user('Файл "curVer.ini" не найден')
			try:
				with open(pathUH) as updHystCont:
					updHysyFile = updHystCont.read()
					updHystCont.close()
					send_message_to_user('Файл "updHyst.ini" найден')
			except:
				send_message_to_user('Файл "updHyst.ini" не найден')
			send_message_to_user('Проверка завершена')
	elif message.startswith('Дарки, обнови главный скрипт') or message.startswith('Дарки обнови главный скрипт'):
		print('user:', event.user_id, ':', event.text)
		if event.user_id == 507365405:
			if mode == 1:
				os.killpg(os.getpgid(pmPID), signal.SIGTERM)
				os.killpg(os.getpgid(cmPID), signal.SIGTERM)
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
				raise SystemExit
			if mode == 0:
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
				raise SystemExit
		else:
			send_message_to_user('В доступе отказано, свяжитесь с моим [darky_wings|создателем]')

print('done')
while True:
	try:
		for event in longpoll.listen(): #своеобразное прослушивание новых сообщений
 		   if event.type == VkEventType.MESSAGE_NEW:
  		      init_message_from_user(event.text)
	except (requests.exceptions.ReadTimeout, socket.timeout):
		print('<<timeout>>')
