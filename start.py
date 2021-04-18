import gui
import person
import logging
#import RPi.GPIO as GPIO
from person import addPerson
import time
import rfid

#LOGPATH = 'log.json'
LOGPATH = '/home/pi/jt/log.json'

def start():
	"""
	:Starten des Programmes:
	"""
	try:
		#init all modules
		person.init()
		logging.basicConfig(filename=LOGPATH,level=logging.INFO)
		
		rfid.testrfid()
		
		#start gui
		gui.start()		
		
		#test
		
		
	except KeyboardInterrupt:
		exit()
	
def exit():
	#GPIO.cleanup()
	logging.warning('Exiting Script')
	print('Exit')
start()
exit()