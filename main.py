"""
start.py

Dieses Modul kümmert sich um den Start und das Beenden des Programmes

Typisches Anwendungsbeispiel:
main()
"""
import settings
import gui
import person
import logging
import time
import rfid

#import RPi.GPIO as GPIO

from person import addPerson


LOGPATH = None

def main():
    """
	Starten und Beenden des Programmes:
	"""
    start()
    exit()

def start():
	"""
	Starten des Programmes:
	"""
	try:
		#init all modules
		settings.init()
		LOGPATH = str(settings.getSetting('log.log'))

		logging.basicConfig(filename=LOGPATH,level=logging.INFO)
		
		person.init()

		#rfid.init()
		
		#start gui
		gui.start()		
		
		
		
	except KeyboardInterrupt:
		exit()
	
def exit():
	"""
	:Beenden des Programmes:
	"""
	#GPIO.cleanup()
	logging.warning('Exiting Script')
	print('Exit')



if __name__ == '__main__':
    main()