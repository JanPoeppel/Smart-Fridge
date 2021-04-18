import money
import logging
import rfid
import person

def buy(rfid, amount):
    if(float(money.getMoney(rfid))>= float(amount)):
        money.withdraw(rfid, amount)
        name = person.getName(rfid)
        prices = str(amount)
        logging.info(name +'('+rfid+') hat fuer '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
        print(name +'('+rfid+') hat  fuer '+prices+' eingekauft, neuer Stand: '+str(money.getMoney(rfid)))
        return 1
    else:
        return -1
    
"""    
def getPrice(id):
    switcher = {
        #id: Preis
        0: 1,
        1: 1,
        2: 4,
        3: 5
    }
    return switcher.get(id, -1)
"""
def getPrice(name):
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
    return switcher.get(name, 0)

def startbuy(id):
    rfid.readuid()

def getNamefromID(id):
    switcher = {
        0: "Cola",
        1: "Bier",
        2: "PizzaSchwank",
        3: "Limo"
    }
    return switcher.get(id, -1)
def getIDfromName(name):
    switcher = {
        #id: Preis
        "Cola": 1,
        "Bier": 2,
        "PizzaSchwank": 3,
        "Gelbes_Limo": 4
    }
    return switcher.get(name, "Error")
