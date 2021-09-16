"""
person.py

Dieses Modul kümmert sich um das Verwalten der Nutzer

Typisches Anwendungsbeispiel:
person.init()
auth = auth(RFID)
check = addPerson(String, RFID)
check = rfidExists(RFID)
check = nameExists(String)
name = getName(RFID)
rfid = getRFID(String)
date = lastSeen(RFID)

:param addr: Device MAC address, defaults to None
:type addr: str, optional

:param DATAPATH: Pfad zur data.json
:param init:
:param auth:
:type auth: RFID
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
        data[RFID] = []
        data[ADMIN] = [MAGICNUMBER]
        settings.saveData(data, 'data.json')
        time.sleep(1)
        logging.warn('File \'data.json\' created')
        print('File \'data.json\' created')
        #TODO Exceptions?

def auth(rfid):
    """
	Authentifiziert einen Admin

    Prüft ob die RFID in der Liste der Admins ist.
    Loggt fehlgeschlagene Authentifizierungen.

    Args:
        rfid: Die zu überprüfende RFID
    
    Returns:
        true: wenn die RFID in der Liste ist.
        false: wenn die RFID nicht in der Liste ist.
	"""
    rfid = str(rfid)
    #TODO rfid == admin List settings
    data = settings.getData('data.json')
    admins = data[ADMIN]
    if(len(admins)==1 and admins[0] == MAGICNUMBER):
        return True
    if(rfid in admins):
        return True
    else:
        logging.warning('Fehlgeschlagener Login mit '+str(rfid) + ' ' + getName(rfid))
        print('Fehlgeschlagener Login von '+str(rfid) + ' ' + getName(rfid))
        return False

def addPerson(name, rfid):
    """
	Fügt eine*n neue*n Nutzer*in hinzu.

    Loggt den Versuch eine bereits vergebene RFID erneut anzulegen.

    Args:
        name: Der Name des*der Nutzer*in
        rfid: Die RFID des*der Nutzer*in
    
    Returns:
        1: wenn der*die Nutzer*in erfolgreich hinzugefügt wurde.
        -1: Wenn der Name bereits vergeben ist.
        -2: Wenn die RFID bereits vergeben ist.
        -3: Wenn ein interner Fehler aufgetreten ist.
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
    Prüft ob eine RFID existiert.

    Args:
        rfid: Die zu überprüfende RFID
    
    Returns:
        True: Wenn die RFID bereits Exisitiert.
        False: Wenn die RFID noch nicht Existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[RFID]:
        if i[RFID] == rfid:
            return True
    return False

def nameExists(name):
    """
    Prüft ob ein Name existiert.

    Args:
        name: Der zu überprüfende Name
    
    Returns:
        True: Wenn der Name bereits Exisitiert.
        False: Wenn der Name noch nicht Existiert.
    """
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[NAME] == name:
            return True
    return False

def __addNameRFID(name, rfid):
    """
    Private Funktion um eine neue Person anzulegen.

    Private Funktion um die Daten in die Datei zu schreiben.
    Loggt das Ereignis.

    Args:
        name: Der Name des*der Nutzer*in
        rfid: Die RFID des*der Nutzer*in
    
    Returns:
        True: Wenn die Person erfolgreich angelegt wurde.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    data[PEOPLE].append({
        NAME:name,
        RFID:str(rfid),
        SEEN: time.strftime('%d/%m/%Y')
    })
    data[RFID].append({
        RFID:rfid,
        MONEY: 0
    })
    settings.saveData(data, 'data.json')
    time.sleep(1)
    #TODO Log this
    print('Name \'%s\' mit RFID \'%s\' wurde hinzugefuegt' %(name, rfid))
    return True

def getName(rfid):
    """
    Gibt den Namen zu einer RFID zurück.

    Args:
        rfid: Die RFID des*der Nutzer*in
    
    Returns:
        Den Namen zu der RFID.
        'NoName' wenn die RFID nicht existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[NAME]
    return 'Unknown'

def getRFID(name):
    """
    Gibt die RFID zu einem Namen zurück.

    Args:
        name: Der Name des*der Nutzer*in
    
    Returns:
        Die RFID zu dem Namen RFID.
        'NoRFID' wenn der Name nicht existiert.
    """
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[NAME] == name:
            return i[RFID]
    return 'NoRFID'

def lastSeen(rfid):
    """
    Gibt das Datum zurück an dem zuletzt mit der RFID eingekauft wurde.

    Args:
        rfid: Die RFID des*der Nutzer*in
    
    Returns:
        Das Datum an dem die RFID zuletzt gesehen wurde.
        'NotFound' wenn noch kein Datum existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[SEEN]
    return 'NotFound'
