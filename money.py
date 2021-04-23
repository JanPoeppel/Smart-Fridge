import os.path
import json
import logging
import person
import time
from person import rfidExists

RFID = "rfid"
MONEY = "money"
PEOPLE = 'people'

#DATAPATH = 'data.json'
DATAPATH = 'D:/OneDrive/Dokumente/Uni/Bachelorarbeit/GitHub/Smart Fridge/data.json'


def init():
    if not(fileExist('data.json')):
        data = {}
        data[PEOPLE] = []
        data[RFID] = []
        with open(DATAPATH, 'w') as outfile:
            json.dump(data, outfile)
        logging.warn('File \'data.json\' created')

def withdraw(rfid, amount):
    """
    :Diese Funktion zieht Geld ab

    :param name: rfid
                    Die rfid zum Konto
    :param name: amount
                    Die Menge an Geld
    """
    rfid = str(rfid)
    data = getdata()
    for i in data[RFID]:
        if i[RFID] == rfid:
            i[MONEY] -= amount
            with open(DATAPATH, 'w') as namejson:
                json.dump(data, namejson)
            logging.info('RFID \''+rfid+'\' wurden '+str(amount)+' abgezogen, neuer Stand: '+str(i[MONEY]))
            break

def getMoney(rfid):
    rfid = str(rfid)
    data = getdata()
    for i in data[RFID]:
        if i[RFID] == rfid:
            return i[MONEY]
    return 'RFID nicht gefunden'

def addMoney(rfid, amount):
    rfid = str(rfid)
    data = getdata()
    if not(person.rfidExists(rfid)):
        print("Chip unbekannt, Vorgang abgebrochen")
        return
    for i in data[RFID]:
        if i[RFID] == rfid:
            i[MONEY] += amount
            with open(DATAPATH, 'w') as namejson:
                json.dump(data, namejson)
            logging.info("Geld hiunzugefuegt")
            name = person.getName(rfid)
            logging.info(name+'('+rfid+') wurden '+str(amount)+' hinzugefuegt, neuer Stand: '+str(i[MONEY]))
            print((name+'('+rfid+') wurden '+str(amount)+' hinzugefuegt, neuer Stand: '+str(i[MONEY])))
            break

def fileExist(name):
    return os.path.exists(name)

def getdata():
    if not (fileExist(DATAPATH)):
        person.init()
    with open(DATAPATH, 'r') as namejson:
        return json.load(namejson)
