"""
rfid.py

Dieses Modul ist die Schnittstelle zum RFID Reader Modul.

Typisches Anwendungsbeispiel:
rfid = read()
"""
import reader

def read(): 
    
    try:
        ret = input("Please scan RFID Chip:\n")
        return ret

    except KeyboardInterrupt:
        print('Abbruch')
        return False
    
