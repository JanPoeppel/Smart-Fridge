"""
rfid.py

Dieses Modul ist die Schnittstelle zum RFID Reader Modul.

Typisches Anwendungsbeispiel:
rfid.init()
uid = readuid()
data = readdata()
tuple = readall()
"""
#!/usr/bin/env python
# -*- coding: utf8 -*-

#import MFRC522 #TODO #9 Setup remote control
import time
import re
import subprocess


def init():
    #TODO #10 Error Handling on Raspberry and Windows
    # wmi = win32com.client.GetObject ("winmgmts:")
    # for usb in wmi.InstancesOf ("Win32_USBHub"):
    #     print(usb.DeviceID)

    device_re = re.compile(
        b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb")
    devices = []
    for i in df.split(b'\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    print(devices)
    #TODO #12 for which usecase?
    # with open('/dev/tty0', 'r') as tty:
    #     while True:
    #         RFID_input = tty.readline()
    #         print(str(RFID_input))


def readUID():
    """
    Liest die UID

    Liest die UID vom RFID Chip


    Returns:
        String: Die UID
        False: Wenn ein Fehler aufgetreten ist.
    """
    print("Reading uid")
    time.sleep(2)
    li = __read(1)
    if(li == None):
        return False
    ret = ''.join(str(e) for e in li)
    return ret


def readdata():
    """
    Liest die Daten

    Liest die Daten vom RFID Chip


    Returns:
        String: Die Daten
        False: Wenn ein Fehler aufgetreten ist.
    """
    return __read(2)


def readall():
    """
    Liest die UID und Daten

    Liest die UID und Daten vom RFID Chip


    Returns:
        Tuple: <UID, String> 
        False: Wenn ein Fehler aufgetreten ist.
    """
    tup = __read(0)
    data = ''.join(str(e) for e in tup[1])
    return (tup[0], data)


def __read(mode):
    #TODO #11 Quelle
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
                        return(uid, data)
                    if(mode == 1):
                        return uid
                    if(mode == 2):
                        return data

    except KeyboardInterrupt:
        print('Abbruch')
        return False
