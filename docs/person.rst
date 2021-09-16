person module
=============

Typisches Anwendungsbeispiel:

| person.init()
| auth = auth(RFID)
| check = addPerson(String, RFID)
| check = rfidExists(RFID)
| check = nameExists(String)
| name = getName(RFID)
| rfid = getRFID(String)
| date = lastSeen(RFID) 

.. automodule:: person
   :members:
   :undoc-members:
   :show-inheritance:
   
.. py:function:: addNameRFID(name, rfid)

      Private Funktion um eine neue Person anzulegen.
      Private Funktion um die Daten in die Datei zu schreiben.
      ..note:: Diese Aktion wird geloggt
    
      ..warning:: Bevor die Daten in die Datei zu speichern muss davor geprüft werden, ob bereits ein Name oder eine RFID mit den Werten angelegt wurde.
      Args:
         | name: Der Name des Nutzenden
         | rfid: Die RFID des Nutzenden
    
       Returns:
         True: Wenn die Person erfolgreich angelegt wurde.

