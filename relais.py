"""
Dieses Modul setzt die Werte des GPIO Pins
"""
import time
import RPi.GPIO as GPIO


def open(timet):
    """
    Aktiviert für die angegebene Zeit den GPIO Pin 19
    
    .. note:: Die Zeitspanne wird automatisch auf max. 9s gesetzt. Dies dient zum Schutzfunktion des Magnetschlosses.
    
     Args:
        timet: Die angegebene Zeitspanne
    
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)
    #relais
    if(timet > 9):
        timet = 9
    #relais
    time.sleep(timet)
    GPIO.output(19, GPIO.LOW)
