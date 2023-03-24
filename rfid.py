#-*- coding:utf-8 -*-
"""
rfid.py

Dieses Modul ist die Schnittstelle zum RFID Reader Modul.

Typisches Anwendungsbeispiel:
rfid = read()
"""
import reader

def read(): 
    """
    Initalisiert das reader Modul und wartet auf entsprechende zurückgegebene Werte des RFID-Lesers
    """
    reader1 = reader.Reader(0x13ba, 0x0018, 12, 8, should_reset=False, debug=True)
    reader1.initialize()
    rfids =str(reader1.read().strip())
    reader1.disconnect()
    rfids = rfids.split('\n')[0]
    return str(rfids)
    
