"""
money.py

Dieses Modul kümmert sich um das Verwalten der Guthaben.

Typisches Anwendungsbeispiel:
| money.init()
| check = withdraw(RFID, Double)
| check = addMoney(RFID)
| money = getMoney(String, RFID)

"""
import settings
import os.path
import json
import logging
import person
import time


#Ein paar Strings um Tippfehler zu vermeiden
RFID = "rfid"
MONEY = "money"
PEOPLE = 'people'

def init():
    """
Initalisierung des Money Modules

Erstellt die data.json wenn noch keine existiert.
	"""
    if not(settings.fileExist('data.json')):
        data = {}
        data[PEOPLE] = []
        data[RFID] = []
        settings.saveData(data, 'data.json')
        logging.warn('File \'data.json\' created')
        print('File \'data.json\' created')
        #TODO #5 Exceptions?

def withdraw(rfid, amount):
    """
    Zieht Geld vom Guthaben ab

    Zieht das angegebene Guthaben von der verknüpften RFID ab.

    Args:
        rfid: Die RFID zum Konto
        amount: Die Menge an Guthaben

    Returns:
        True: Wenn das Abziehen erfolgreich war.
        False: Wenn ein Fehler aufgetreten ist.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    if (person.rfidExists(rfid)): 
        for i in data[RFID]:
            if i[RFID] == rfid:
                i[MONEY] -= amount
                settings.saveData(data, 'data.json')
                logging.info('RFID \''+rfid+'\' wurden '+str(amount)+' abgezogen, neuer Stand: '+str(i[MONEY]))
                return True
    return False

def getMoney(rfid):
    """
    Gibt das Guthaben zurück

    Gibt das Guthaben von dem , mit der RFID verknüpften, Konto zurück.

    Args:
        rfid: Die RFID zum Konto

    Returns:
        Double: aktuelles Guthaben
        False: Wenn ein Fehler aufgetreten ist.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[RFID]:
        if i[RFID] == rfid:
            return i[MONEY]
    return False

def addMoney(rfid, amount):
    """
    Erhöht das Guthaben

    Fügt das angegebene Geld einem mit der RFID verknüpften Konto hinzu.

    Args:
        rfid: Die RFID zum Konto
        amount: Die Menge an Guthaben

    Returns:
        True: Wenn das Hinzufügen erfolgreich war.
        False: Wenn ein Fehler aufgetreten ist.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    if (person.rfidExists(rfid)): 
        for i in data[RFID]:
            if i[RFID] == rfid:
                i[MONEY] += amount
                settings.saveData(data, 'data.json')
                logging.info("Geld hiunzugefuegt")
                name = person.getName(rfid)
                logging.info(name+'('+rfid+') wurden '+str(amount)+' hinzugefuegt, neuer Stand: '+str(i[MONEY]))
                print((name+'('+rfid+') wurden '+str(amount)+' hinzugefuegt, neuer Stand: '+str(i[MONEY])))
                return True
    print("Chip unbekannt, Vorgang abgebrochen")
    return False
