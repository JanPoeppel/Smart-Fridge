"""
shop.py

Dieses Modul kümmert sich um das Kaufen von Produkten

Typisches Anwendungsbeispiel:
check = buy(RFID, Double)
price = getPrice(String)

Attribute:
    DATAPATH: Pfad zur data.json
"""
import money
import logging
import rfid
import person
import warnings

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
    switcher = {
        'Greif': 1,
        'Gaas-Seidla': 1,
        'Zwickel': 1,
        'Weisses_Limo': 1,
        'Gelbes_Limo': 1,
        'Spezi':1,
        'Pfirsich-Eistee':0.5,
        'Zitronen-Eistee':0.5,
        'Monster-Energy':1.5,
        'Redbull':1,
        'Brezel': 0.25,
        'Pizza':2,
        'Pizza-Schwank':4,
        'Wasser': 0.5,
        'Apfelschorle':1,
        'Cola_0,5l':1,
        'Weizen':1,
        'Cola_0,3l': 0.7,
        'Cola_1l':2,
        'Capri-Sun':0.5,
        'Trigger-Energy':0.7,
        '0.5_Bier':0.5
    }
    return switcher.get(name, False)

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
