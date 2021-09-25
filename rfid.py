"""
rfid.py

Dieses Modul ist die Schnittstelle zum RFID Reader Modul.

Typisches Anwendungsbeispiel:
rfid = read()
"""
import reader

def read():
    reader1 = reader.Reader(0x13ba, 0x0018, 10, 8, should_reset=False)
    reader1.initialize()
    rfids =str(reader1.read().strip())
    reader1.disconnect()
    rfids = rfids.split('\n')[0]
    return str(rfids)
    
    
    """
    try:
        ret = input("Please scan RFID Chip:\n")
        return ret

    except KeyboardInterrupt:
        print('Abbruch')
        return False
        """
