"""
rfid.py

Dieses Modul ist die Schnittstelle zum RFID Reader Modul.

Typisches Anwendungsbeispiel:
rfid = read()
"""

def read():
    #TODO #11 Quelle
    try:
        print("Reading uid")
        ret = input("Please scan RFID Chip:\n")
        return ret

    except KeyboardInterrupt:
        print('Abbruch')
        return False
