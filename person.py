"""
Dieses Modul kümmert sich um das Verwalten der Nutzenden

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

    Prüft ob die RFID in der Liste der Admins ist.
    
    .. note:: Loggt fehlgeschlagene Authentifizierungen.

    Args:
        rfid: Die zu überprüfende RFID
    
    Returns:
       Boolean. Die Rückgabewerte::

          True -- bei erfolgreicher Authentifizierung
          False -- bei fehlgeschlagener Authentifizierung
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
    Fügt einen neuen Nutzenden hinzu.

    .. note:: Loggt den Versuch eine bereits vergebene RFID erneut anzulegen.

    Args:
        | name: Der Name des Nutzenden
        | rfid: Die RFID des Nutzenden
    
    Returns:
       Integer. Die Rückgabewerte::
       
          1 -- Wenn der Nutzende erfolgreich hinzugefügt wurde.
         -1 -- Wenn der Name bereits vergeben ist.
         -2 -- Wenn die RFID bereits vergeben ist.
         -3 -- Wenn ein interner Fehler aufgetreten ist.
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
       Boolean. Die Rückgabewerte::
       
        True -- Wenn die RFID bereits exisitiert.
        False -- Wenn die RFID noch nicht existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return True
    return False

def nameExists(name):
    """
    Prüft ob ein Name existiert.

    Args:
        name: Der zu überprüfende Name
    
    Returns:
       Boolean. Die Rückgabewerte::
       
        True -- Wenn der Name bereits exisitiert.
        False -- Wenn der Name noch nicht existiert.
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
    
    .. warning:: Bevor die Daten in die Datei gespeichert werden, muss geprüft werden, ob bereits ein Name oder eine RFID mit den Werten hinterlegt ist.

    Args:
        | name: Der Name des Nutzenden
        | rfid: Die RFID des Nutzenden
    
    Returns:
       Boolean. Die Rückgabewerte::
       
        True -- Wenn die Person erfolgreich angelegt wurde.
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
    print('Name \'%s\' mit RFID \'%s\' wurde hinzugefügt' %(name, rfid))
    return True

def getName(rfid):
    """
    Gibt den Namen zu einer RFID zurück.

    Args:
        rfid: Die RFID des Nutzenden
    
    Returns:
       String. Die Rückgabewerte::
       
        String -- Den Namen zu der RFID.
        'Unknown' -- Wenn die RFID nicht existiert.
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
        name: Der Name des Nutzenden
    
    Returns:
       String. Die Rückgabewerte::
       
        String -- Die RFID zu dem Namen RFID.
        'NoRFID' -- Wenn der Name nicht existiert.
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
        rfid: Die RFID des Nutzenden
    
    Returns:
       Date oder String. Die Rückgabewerte::
       
        Date -- Das Datum an dem die RFID zuletzt gesehen wurde.
        'NotFound' -- Wenn noch kein Datum existiert.
    """
    rfid = str(rfid)
    data = settings.getData('data.json')
    for i in data[PEOPLE]:
        if i[RFID] == rfid:
            return i[SEEN]
    return 'NotFound'
