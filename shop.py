"""
shop.py

Dieses Modul kümmert sich um das Kaufen von Produkten

Typisches Anwendungsbeispiel:
check = buy(RFID, Double)
price = getPrice(String)

Attribute:
    DATAPATH: Pfad zur data.json
"""
import settings
import json
import money
import logging
import rfid
import person
import warnings
import logging

data = None

def buy(rfid, amount):
    """
    Zieht Geld vom Konto ab

    Überprüft ob genügend Geld auf dem Konto ist und zieht die gegebene Summe ab.
    Loggt das Event.

    Args:
        rfid: Die RFID zum Konto
        amount: Die Menge an Geld


    Returns:
        True: Wenn es erfolgreich war.
        False: Wenn ein Fehler aufgetreten ist oder nicht genügend Geld auf dem Konto war.
    """
    if(float(money.getMoney(rfid))>= float(amount)):
        money.withdraw(rfid, amount)
        name = person.getName(rfid)
        prices = str(amount)
        #TODO #14 bessere Formatierung der String übergebung
        logging.info(name +'('+rfid+') hat fuer '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
        print(name +'('+rfid+') hat  fuer '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
        return True
    else:
        return False
    
def getPrice(name):
    """
    Gibt den Preis von einem Produkt zurück

    Sucht anhand des Namens von einem Produkt den dazugehörigen Preis.

    Args:
        name: Der Name vom Produkt

    Returns:
        Integer: den Preis.
        False: Wenn ein Fehler aufgetreten ist oder das Produkt nicht gefunden wurde.
    """
    #TODO #13 Move to file
    if(data == None):
        data = settings.getData('settings.json')

    price = data['article'][name]
    if(price == None):
        return False
    return price



def updateAmount(name, amount):
    data = settings.getData('settings.json')
    data[name]['articel']['amount'] = data[name]['articel']['amount'] + amount
    settings.saveData(data,'settings.json')
    return True

def buyArticel(rfid, articels):
    #articels[0] = name
    #articels[1] = amount
    sum = 0
    for a in articels:
        sum += articels[1]*getPrice(articels[0])
    if not(buy(rfid, sum)):
        return False
    for a in articels:
        if not(updateAmount(articels[0], articels[1]*-1)):
            logging.warn("New Amount of %d cannot be updated with %d", articels[0], articels[1]*-1)
    return True

def __startbuy(id):
    rfid.readUID()
    warnings.warn(
            "__startbuy is deprecated and will be removed in further versions",
            DeprecationWarning
        )

def getNamefromID(id):
    switcher = {
        0: "Cola",
        1: "Bier",
        2: "PizzaSchwank",
        3: "Limo"
    }
    warnings.warn(
            "deprecated and will be removed in further versions",
            DeprecationWarning
        )
    return switcher.get(id, -1)
def getIDfromName(name):
    switcher = {
        #id: Preis
        "Cola": 1,
        "Bier": 2,
        "PizzaSchwank": 3,
        "Gelbes_Limo": 4
    }
    warnings.warn(
            "__startbuy is deprecated and will be removed in further versions",
            DeprecationWarning
        )
    return switcher.get(name, "Error")
