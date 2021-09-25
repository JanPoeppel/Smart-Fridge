"""
Dieses Modul kuemmert sich um das Verwalten der Nutzenden

"""

import settings
import json
import os.path
import logging
import time

#Ein paar Strings um Tippfehler zu vermeiden
PEOPLE = 'people'
RFID = 'rfid'
NAME = 'name'
SEEN = 'seen'
MONEY = 'money'
ADMIN = 'admin'
MAGICNUMBER = 'REPLACE_WITH_RFIDS_0x00C0FFEE'


def init():
    """
	Initalisierung des Personen Modules

    Erstellt die data.json wenn noch keine existiert.
	"""
    

    if not(settings.fileExist(settings.getPath('data.json'))):
        data = {}
        data[PEOPLE] = []
        data[ADMIN] = [MAGICNUMBER]
        settings.saveData(data, 'data.json')
        time.sleep(1)
        logging.warn('File \'data.json\' created')
        print('File \'data.json\' created')
        #TODO Exceptions?

def auth(rfid):
    """
    Authentifiziert einen Admin

    Prueft ob die RFID in der Liste der Admins ist.
    
    .. note:: Loggt fehlgeschlagene Authentifizierungen.

    Args:
        rfid: Die zu ueberpruefende RFID
    
    Returns:
        | True: wenn die RFID in der Liste ist.
        | False: wenn die RFID nicht in der Liste ist.
	"""
    rfid = str(rfid)
    #TODO rfid == admin List settings
    data = settings.getData('data.json')
    admins = data[ADMIN]
    if(len(admins)==1 and admins[0] == MAGICNUMBER):
        print('Es sind noch keine Admin RFIDs hinterlegt!')
        return True
    if(rfid in admins):
        return True
    else:
        logging.warning('Fehlgeschlagener Login mit '+str(rfid) + ' ' + getName(rfid))
        print('Fehlgeschlagener Login von '+str(rfid) + ' ' + getName(rfid))
        return False

def addPerson(name, rfid):
    """
	Fuegt einen neuen Nutzenden hinzu.

    .. note:: Loggt den Versuch eine bereits vergebene RFID erneut anzulegen.

    Args:
        | name: Der Name des Nutzenden
        | rfid: Die RFID des Nutzenden
    
    Returns:
        | 1: wenn der Nutzende erfolgreich hinzugefuegt wurde.
        | -1: Wenn der Name bereits vergeben ist.
        | -2: Wenn die RFID bereits vergeben ist.
        | -3: Wenn ein interner Fehler aufgetreten ist.
	"""
    
    if(rfidExists(rfid)):
        logging.warning('Versuch RFID doppelt anzulegen '+str(rfid) + ' '+str(name))
        print('RFID bereits vorhanden, Vorgang wird abgebrochen')
        return -2
    elif(nameExists(name)):
        print('Name bereits vorhanden')
        return -1
    else:
        if(__addNameRFID(name, rfid)):
            return 1
    return -3

def rfidExists(rfid):
    """
    Prueft ob eine RFID existiert.

    Args:
        rfid: Die zu ueberpruefende RFID
    
    Returns:
        | True: Wenn die RFID bereits exisitiert.
        | False: Wenn die RFID noch nicht existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return True
    return False

def nameExists(name):
    """
    Prueft ob ein Name existiert.

    Args:
        name: Der zu ueberpruefende Name
    
    Returns:
        | True: Wenn der Name bereits exisitiert.
        | False: Wenn der Name noch nicht existiert.
    """
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[NAME] == name:
            return True
    return False

def __addNameRFID(name, rfid):
    """
    Private Funktion um eine neue Person anzulegen beziehungsweise die Werte in die Datei zu schreiben.
    
    .. note:: Diese Aktion wird geloggt
    
    .. warning:: Bevor die Daten in die Datei gespeichert werden, muss geprueft werden, ob bereits ein Name oder eine RFID mit den Werten hinterlegt ist.

    Args:
        | name: Der Name des Nutzenden
        | rfid: Die RFID des Nutzenden
    
    Returns:
        True: Wenn die Person erfolgreich angelegt wurde.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    data[PEOPLE].append({
        NAME:name,
	MONEY: 0,
        RFID:str(rfid),
        SEEN: time.strftime('%d/%m/%Y')
    })
    settings.saveData(data, 'data.json')
    time.sleep(1)
    #TODO Log this
    print('Name \'%s\' mit RFID \'%s\' wurde hinzugefuegt' %(name, rfid))
    return True

def getName(rfid):
    """
    Gibt den Namen zu einer RFID zurueck.

    Args:
        rfid: Die RFID des Nutzenden
    
    Returns:
        | Den Namen zu der RFID.
        | 'Unknown' wenn die RFID nicht existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[NAME]
    return 'Unknown'

def getRFID(name):
    """
    Gibt die RFID zu einem Namen zurueck.

    Args:
        name: Der Name des Nutzenden
    
    Returns:
        | Die RFID zu dem Namen RFID.
        | 'NoRFID' wenn der Name nicht existiert.
    """
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[NAME] == name:
            return i[RFID]
    return 'NoRFID'

def lastSeen(rfid):
    """
    Gibt das Datum zurueck an dem zuletzt mit der RFID eingekauft wurde.

    Args:
        rfid: Die RFID des Nutzenden
    
    Returns:
        | Das Datum an dem die RFID zuletzt gesehen wurde.
        | 'NotFound' wenn noch kein Datum existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[SEEN]
    return 'NotFound'
