import json
import os.path
import logging
import time

PEOPLE = 'people'
RFID = 'rfid'
NAME = 'name'
SEEN = 'seen'
MONEY = 'money'



#DATAPATH = 'data.json'
DATAPATH = 'D:/OneDrive/Dokumente/Uni/Bachelorarbeit/GitHub/Smart Fridge/data.json'


def init():
    if not(fileExist(DATAPATH)):
        data = {}
        data[PEOPLE] = []
        data[RFID] = []
        with open(DATAPATH, 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(1)
        print('File \'data.json\' created')

def getdata():
    with open(DATAPATH, 'r') as namejson:
        return json.load(namejson)
    
def auth(rfid):
    rfid = str(rfid)
    if(rfid == '1321908530113'):
        return 1
    else:
        logging.warning('Fehlgeschlagener Login mit '+str(rfid) + ' ' + getName(rfid))
        print('Fehlgeschlagener Login mit '+str(rfid) + ' ' + getName(rfid))
        return -1

def addPerson(name, rfid):
    rfid = str(rfid)
    rfid = rfid.translate(None, '()')
    if(rfidExists(rfid)):
        logging.warning('Versuch RFID doppelt anzulegen '+str(rfid) + ' '+str(name))
        print('RFID bereits vorhanden, Vorgang wird abgebrochen')
        return -2
    elif(nameExists(name)):
        print('Name bereits vorhanden')
        return -1
    else:
        addNameRFID(name, rfid)
        return 1

def rfidExists(rfid):
    rfid = str(rfid)
    data = getdata()
    for i in data[RFID]:
        if i[RFID] == rfid:
            return True

def nameExists(name):
    data = getdata()
    for i in data[PEOPLE]:
        if i[NAME] == name:
            return True

def addNameRFID(name, rfid):
    rfid = str(rfid)
    data = getdata()
    data[PEOPLE].append({
        NAME:name,
        RFID:str(rfid),
        SEEN: time.strftime('%d/%m/%Y')
    })
    data[RFID].append({
        RFID:rfid,
        MONEY: 0
    })
    with open(DATAPATH, 'w') as namejson:
        json.dump(data, namejson)
    time.sleep(1)
    print('Name \''+name+'\' mit RFID \''+rfid+'\' wurde hinzugefuegt')

def getName(rfid):
    rfid = str(rfid)
    data = getdata()
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[NAME]
    return 'NoName'

def getRFID(name):
    print('suche '+ str(name))
    data = getdata()
    for i in data[PEOPLE]:
        if i[NAME] == name:
            return i[RFID]
    return 'NoRfid'

def lastSeen(rfid):
    rfid = str(rfid)
    data = getdata()
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[SEEN]
    return 'NotFound'


def fileExist(name):
    return os.path.exists(name)
