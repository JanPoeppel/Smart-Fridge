#!/usr/bin/env python
# -*- coding: utf8 -*-
 
#import RPi.GPIO as GPIO
#import MFRC522
import time
 
def readuid():
    print("Reading uid")
    time.sleep(2)
    return '1321908530113'
    li = read(1)
    if(li == None):
        return -1
    ret = ''.join(str(e) for e in li)
    return ret

def readdata():
    return read(2)

def readall():
    return read(0)

def read(mode):
    ret = '1321908530113'
    return ret

def testrfid():
    with open('/dev/tty0', 'r') as tty:
        while True:
            RFID_input = tty.readline()
            print(str(RFID_input))
    

"""
def read(mode): 
    MIFAREReader = MFRC522.MFRC522()
    try:
        b = True
        while b:
            # Scan for cards    
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
     
            # If a card is found
            if status == MIFAREReader.MI_OK:
                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()
                # This is the default key for authentication
                key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                # Select the scanned tag
                MIFAREReader.MFRC522_SelectTag(uid)
                # Authenticate
                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
                # Check if authenticated
                if status == MIFAREReader.MI_OK:
                    # Read block 8
                    data = MIFAREReader.MFRC522_Read(8)
                    if(mode == 0):
                        b = False
                        return(uid, data)
                    if(mode == 1):
                        b = False
                        return uid
                    if(mode == 2):
                        b = False
                        return data
 
    except KeyboardInterrupt:
        print('Abbruch')
        GPIO.cleanup()
"""