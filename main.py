"""
main.py

Dieses Modul kümmert sich um den Start und das Beenden des Programmes.
Dabei initalisiert es wichtige Variablen und überprüft ob alle Abhängigkeiten verfügbar sind.

Hierfür müssen die zu prüfenden Module importiert werden.

.. note:: Die exit() Funktion wird auch beim einem KeyboardInterrupt Event aufgerufen.


"""
import settings
import person
import logging
import time
import rfid
import gui
import shop

#import RPi.GPIO as GPIO


LOGPATH = None

def main():
    """
	Starten und Beenden des Programmes
	"""
    start()
    exit()

def start():
	"""
	Starten des Programmes:
	initialisiert das Einstellungsmodul :class:'settings'
	"""
	try:
		#init all modules
		settings.init()
		LOGPATH = str(settings.getPath('log.log'))
		logging.basicConfig(filename='log.log',level=logging.INFO)
		
		person.init()
		
		gui.start()		
		
		
		
	except KeyboardInterrupt:
		exit()
	
def exit():
	"""
	Beenden des Programmes
	"""
	#GPIO.cleanup()
	logging.warning('Exiting Script')
	print('Exit')



if __name__ == '__main__':
    main()
