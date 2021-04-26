"""
start.py

Dieses Modul kümmert sich um den Start und das Beenden des Programmes

Typisches Anwendungsbeispiel:
main()
"""

import gui
import person
import logging
import time
import rfid

#import RPi.GPIO as GPIO

from person import addPerson


#LOGPATH = 'log.json'


#TODO Move this Setting into Settings
LOGPATH = 'D:/OneDrive/Dokumente/Uni/Bachelorarbeit/GitHub/Smart Fridge/log.json'

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
		person.init()
		logging.basicConfig(filename=LOGPATH,level=logging.INFO)
		
		rfid.init()
		
		#start gui
		gui.start()		
		
		#test
		
		
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