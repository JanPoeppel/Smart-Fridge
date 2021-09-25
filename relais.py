import time
import RPi.GPIO as GPIO


def open(timet):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)
    #relais
    if(timet > 9):
        timet = 9
    #relais
    time.sleep(timet)
    GPIO.output(19, GPIO.LOW)
