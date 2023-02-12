#-*- coding:utf-8 -*-
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
import node
import warnings
import logging

shoppingcart ={}

def addToCart(name, amount):
    """
    Fügt einen Artikel zum Warenkorb hinzu.
    
    Fügt die angegebene Anzahl vom angegebenen Artikel zum Warenkorb hinzu.
    
    Args:
        name: Der Name des Artikels
        amount: Die Menge des Artikels
    
    Returns:
       Boolean.  Die Rückgabewerte::
       
          True -- Bei erfolgreichem hinzufügen
    """
    shoppingcart[name] = shoppingcart.get(name, 0) + amount
    if(shoppingcart[name] == 0):
        shoppingcart.pop(name)
    return True

def getCart():
    """
    Gibt den aktuellen Warenkorb zurück.
    
    Returns:
       Array.  Die Rückgabewerte::
       
          Array -- Der aktuelle Warenkorb
    """
    return shoppingcart

def resetCart():
    """
    Löscht den aktuellen Warenkorb
    
    Returns:
       Boolean.  Die Rückgabewerte::
       
          True -- Bei erfolgreichem löschen
    """
    shoppingcart.clear()
    return True

def getCartValue():
    """
    Gibt den aktuellen Wert des Warenkorbs zurück
    
    Summiert die Preise aller im Warenkorb befindlichen Artikel. Hierbei werden die Preise über die getPrice() Funktion abgefragt.
    
    Returns:
       Double.  Die Rückgabewerte::
       
          Double -- Der Wert des aktuellen Warenkorbs
    """
    sum = 0
    for a in shoppingcart:
        sum += shoppingcart[a]*getPrice(a)
    return sum

def checkoutCart(rfid):
    """
    Zieht den aktuellen Wert des Warenkorbs vom angegeben Konto ab und löscht den Warenkorb.
    
    Ruft die buy(RFID, amount) Funktion auf und setzt den Warenkorb über die resetCart() Funktion zurück.
    Sollte nicht genug Geld auf dem Konto sein, oder ein Fehler beim Zurücksetzen des Warenkorbs auftreten, wird False zurückgegeben.
    Bei erfolgreichem Kauf wird eine Nachricht an das node Modul geschickt.
    
    Args:
        rfid: Die RFID der kaufenden Person
    
    Returns:
       Boolean.  Die Rückgabewerte::
       
          True -- Bei erfolgreichem Kauf
          False -- Bei einem Fehler.
    """
    if (buy(rfid, getCartValue())):
        node.sendMessage("%s hat gerade für %d eingekauft." %(rfid, getCartValue()))
        for a in shoppingcart.keys():
            if not(updateAmount(a, -1)):
                logging.warn("New Amount of %s cannot be updated with %d", a, -1)
                return resetCart()
        return True
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
       Boolean.  Die Rückgabewerte::
       
        True -- Wenn es erfolgreich war.
        False -- Wenn ein Fehler aufgetreten ist oder nicht genügend Geld auf dem Konto war.
    """
    if(float(money.getMoney(rfid))>= float(amount)):
        if(money.withdraw(rfid, amount)):
            name = person.getName(rfid)
            prices = str(amount)
            #TODO #14 bessere Formatierung der String übergebung
            logging.info(name +'('+rfid+') hat für '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
            print(name +'('+rfid+') hat  für '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
            return True
    return False
    
def getPrice(name):
    """
    Gibt den Preis von einem Produkt zurück

    Sucht anhand des Namens von einem Produkt den dazugehörigen Preis.

    Args:
        name: Der Name vom Produkt

    Returns:
       Boolean oder Integer.  Die Rückgabewerte::
       
        Integer -- der Preis des Artikels.
        False -- Wenn ein Fehler aufgetreten ist oder das Produkt nicht gefunden wurde.
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
    """
    Ändert die noch verfügbare Menge eines Produktes

    Args:
        name: Der Name vom Produkt
        amount: Die zu ändernde Anzahl

    Returns:
       Boolean.  Die Rückgabewerte::
       
        True -- Wenn die Anzahl erfolgreich gespeichert werden konnte.
        False -- Wenn ein Fehler aufgetreten ist oder das Produkt nicht gefunden wurde.
    """
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
    """
    Gibt die Liste an Produkten einer bestimmten Kategorie zurück

    Args:
        category: Die Kategorie

    Returns:
       Array.  Die Rückgabewerte::
       
        Array -- Eine Liste aller Produkte einer Kategorie.
    """
    data = settings.getData('settings.json')
    return data['article'][category].keys()
