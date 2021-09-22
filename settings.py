"""
settings.py

Dieses Modul kümmert sich um das Verwalten der Einstellungen

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
    ARTICLE = 'article'
    ALK = 'alk'
    DRINKS = 'drinks'
    FOOD = 'food'
    if not(fileExist(dir_path)):
        data = {}

        #init settingsfile
        data['data.json'] = os.path.dirname(os.path.realpath(__file__))+'/data.json'
        data['log.log'] = os.path.dirname(os.path.realpath(__file__))+'/log.log'
        data[ARTICLE] = {}
        data[ARTICLE][ALK] = {}
        data[ARTICLE][DRINKS] = {}
        data[ARTICLE][FOOD] = {}
        data[ARTICLE][ALK]['Bier'] = {}
        data[ARTICLE][ALK]['Bier']['price'] = 1
        data[ARTICLE][ALK]['Bier']['amount'] = 0
        drinks = ['Cola', 'Limo', 'Spezi', 'Eistee', 'Apfelschorle', 'Energy']
        for d in drinks:
            data[ARTICLE][DRINKS][d] = {}
            data[ARTICLE][DRINKS][d]['price'] = 1
            data[ARTICLE][DRINKS][d]['amount'] = 0
        data[ARTICLE][FOOD]['Pizza']= {}
        data[ARTICLE][FOOD]['Pizza']['price'] = 2
        data[ARTICLE][FOOD]['Pizza']['amount'] = 0
        data[ARTICLE][FOOD]['Brezel']= {}
        data[ARTICLE][FOOD]['Brezel']['price'] = 0.25
        data[ARTICLE][FOOD]['Brezel']['amount'] = 0


        with open(dir_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        time.sleep(1)
        logging.warn('File \'settings.json\' created')
        print('File \'settings.json\' created')
        #TODO #21 Exceptions?
def getPath(name):
    if(name == 'settings.json'):
        return dir_path
    if not(fileExist(dir_path)):
        return None
    with open(dir_path, 'r') as namejson:
        data = json.load(namejson)
        return data[name]
    

def getData(name):
    """
	Läd die Datei

	"""
      #TODO #22 Can not read on windows, test on rasp!
    path = getPath(name)
    if not(fileExist(path)):
        return None
    with open(path, 'r') as namejson:
        return json.load(namejson)

def saveData(data, name):
    with open(getPath(name), 'w') as namejson:
        json.dump(data, namejson, indent=4)
  
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

def fileExist(name):
    return os.path.exists(name)
