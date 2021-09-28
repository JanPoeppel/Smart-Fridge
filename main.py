#-*- coding:utf-8 -*-
"""
main.py

Dieses Modul kümmert sich um den Start und das Beenden des Programmes.
Dabei initalisiert es wichtige Variablen und überprüft, ob alle Abhängigkeiten verfügbar sind.

Hierfür müssen die zu prüfenden Module importiert werden.

.. note:: Die exit() Funktion wird auch bei einem KeyboardInterrupt Event aufgerufen.


"""
import settings
import person
import logging
import time
import rfid
import gui
import shop
import node

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
    
    Initialisiert das Einstellungsmodul :class:`settings.py` und setzt den LOGPATH auf den in der Datei hinterlegten Pfad.
    Danach wird die GUI gestartet.
    """
    try:
        #init all modules
        settings.init()
        LOGPATH = str(settings.getPath('log.log'))
        logging.basicConfig(filename='log.log',level=logging.INFO)
        
        person.init()
        gui.start()        
        
        
    except SystemExit:
        exit()        
    except KeyboardInterrupt:
        exit()
    
def exit():
    """
    Beenden des Programmes:
    
    Diese Funktion wird als letztes aufgerufen und kann daher zum Aufräumen genutzt werden.
    Zum Beispiel können noch gesetzte GPIOs zurückgesetzt werden.
    """
    #GPIO.cleanup()
    logging.warning('Exiting Script')
    print('Exit')



if __name__ == '__main__':
    main()
