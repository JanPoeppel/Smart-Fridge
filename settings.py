"""
settings.py

Dieses Modul kümmert sich um das Verwalten der Einstellungen

Typisches Anwendungsbeispiel:
settings.init()
check = getSetting(String)

Attribute:
    DATAPATH: Pfad zur setting.json
"""


import json
import os.path
import logging
import time

FILENAME = 'settings.json'

dir_path  = os.path.dirname(os.path.realpath(__file__))+"/"+FILENAME

def init():
    """
	Initalisierung des Einstellungs Modules

    Erstellt die settings.json wenn noch keine existiert.
	"""
    if not(__fileExist(dir_path)):
        data = {}
        data['data.json'] = [os.path.dirname(os.path.realpath(__file__))+'/data.json']
        data['log.log'] = [os.path.dirname(os.path.realpath(__file__))+'/log.log']
        with open(dir_path, 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(1)
        logging.warn('File \'settings.json\' created')
        print('File \'settings.json\' created')
        #TODO #21 Exceptions?
def getData(path):
    """
	Läd die Datei
	"""
      #TODO #22 Can not read on windows, test on rasp!
    with open(path, 'r') as namejson:
        return json.load(namejson)

def saveData(data, path):
    with open(path, 'w') as namejson:
        json.dump(data, namejson)
  
def getSetting(name):
    """
	Gibt den gesetzten Wert zurück
    
    Args:
        name: Die zu überprüfende Einstellung
    """
    return getData(dir_path)[name]

def setSetting(name, value):
    """
	Setzt den Wert zur Einstellung
    
    Args:
        name: Der Name der Einstellung
        value: Der Wert der Einstellung
    """
    data = getData(dir_path)
    data[name] = value
    
    with open(dir_path, 'w') as namejson:
        json.dump(data, namejson)
    time.sleep(1)
    logging.info("The Setting of " + name + " was set to "+value)
    print("The Setting of " + name + " was set to "+value)
    return True

def __fileExist(name):
    return os.path.exists(name)
