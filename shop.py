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
import money
import logging
import rfid
import person
import warnings
import logging

shoppingcart ={}

def addToCart(name, amount):
    shoppingcart[name] = shoppingcart.get(name, 0) + amount
    if(shoppingcart[name] == 0):
        shoppingcart.pop(name)
    return True

def getCart():
    return shoppingcart

def resetCart():
    shoppingcart.clear()
    return True

def getCartValue():
    sum = 0
    for a in shoppingcart:
        sum += shoppingcart[a]*getPrice(a)
    return sum

def checkoutCart(rfid):
    if (buy(rfid, getCartValue())):
        for a in shoppingcart.keys():
            if not(updateAmount(a, -1)):
                logging.warn("New Amount of %s cannot be updated with %d", a, -1)
                return resetCart()
    return False

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
        if(money.withdraw(rfid, amount)):
            name = person.getName(rfid)
            prices = str(amount)
            #TODO #14 bessere Formatierung der String übergebung
            logging.info(name +'('+rfid+') hat fuer '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
            print(name +'('+rfid+') hat  fuer '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
            return True
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
    data = settings.getData('settings.json')
    if (name in data['article']['drinks']):
        return data['article']['drinks'][name]['price']
    if (name in data['article']['alk']):
        return data['article']['alk'][name]['price']
    if (name in data['article']['food']):
        return data['article']['food'][name]['price']
    return False



def updateAmount(name, amount):
    data = settings.getData('settings.json')
    
    if (name in data['article']['drinks']):
        data['article']['drinks'][name]['amount'] += amount
    elif (name in data['article']['alk']):
        data['article']['alk'][name]['amount'] += amount
    elif (name in data['article']['food']):
        data['article']['food'][name]['amount'] += amount
    else:
        return False
    settings.saveData(data,'settings.json')
    return True

def getArticleList(category):
    data = settings.getData('settings.json')
    return data['article'][category].keys()