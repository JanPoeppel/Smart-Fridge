# SmartFridge

## Beschreibung
Dieses Projekt bietet Jugendlichen den Zugang zu technischem sowie logischem Denken sowie einen Anreiz sich weiter in dem Themengebiet fortzubilden.\

## Problematiken in den Jugendtreffs
Jeder Jugendtreff möchte seinen Besuchern und Mitgliedern Getränke oder auch etwas zu Essen anbieten. Dafür wird in den meisten Fällen jedoch eine Aufischtsperson für die Kasse und die Korrekte Bezahlung benötigt.\
Dieses Problem soll duch dieses Projekt gelöst werden, indem man für jeden ein internes Konto anlegt, auf dem direkt ein Betrag eingezahlt werden kann und beim bezahlen das Guthaben auf dem Konto verringert wird.\

Die Grundfunktionen können auch ohne Vorkenntnisse eingerichtet werden.

## Aufbau
Durch das Projekt dient als Grundbausteine, welches dann durch die Jugendlichen weiter ausgebaut, verändert sowie ergänzt werden kann.\
Als Platform dient ein Raspberry Pi (getestet auf Version #TODO), ein Touchscreen und ein RFID-Reader. 
Durch eine simple Benutzeroberfläche können Jugendliche in ihrem Jugendtreff, Vereinsheim oder auch in Privaten Räumen ihre Getränke bezahlen.\
Die Jugendlichen können sich einen RFID-Chip oder -Karte bei einem Verantwortlichen registrieren lassen und können dann Geld auf diese laden. Nun müssen die Jugendlichen nur noch den Chip beim bezahlvorgang an das Gerät halten, und der Betrag wird automatisch von ihrem Konto abgezogen.\
*Optional kann auch ein Magnetschloss am Kühlschrank oder entsprechendes Mobiliar montiert werden, welcher nach dem Bezahlvorgang das Schloss entriegelt*

## Hardeware Anforderungen
[Raspberry Pi](https://www.raspberrypi.org/ "raspberrypi.org")
Touchscreen Display (in dieser Anleitung wird das unten verlinkte Display verwendet, bei anderen Herstellern muss auf


## Installation

1. Die Micro SD Karte an einem Computer mit dem bereitgestellten Image beschreiben und das Display auf dem Raspberry Pi anbringen. 
   Eine Anleitung sowie der Downloadlink für das Image ist [hier](https://joy-it.net/files/files/Produkte/RB-TFT3.5/RB-TFT-Anleitung_04082020.pdf "joy-it.net") zu      finden.\
   Beim Beschreiben der SD-Karte kann beim RaspberryPi Imager über die Tastenkombination STRG+SHIFT+X direkt eine SSH Verbindung, sowie der hostname vergeben werden.\
   Nach erfolgreichem Schreiben sollte es dann so ausschauen:\  
   ![](images/imag_succ.png?raw=true)
   
   
2. Befolge die Installationsanweisungen auf dem Display\
   Am Ende muss der RaspberryPi neugestartet werden.
3. a) mit Internetverbindung:\
      Kopiere die Dateien aus dem Gitrepository über folgenden Befehl:
      ```shell
      git clone https://github.com/JanPoeppel/Smart-Fridge.git
      ```
      ![](images/clone.png?raw=true)
   b) ohne Internetverbindung
       Die [.zip Datei](https://github.com/JanPoeppel/Smart-Fridge/archive/refs/heads/main.zip) downloaden und auf einem USB Stick entpacken.\
       Dannach die Dateien auf den Raspberrypi kopieren
5. In der aktuellen Version ist Python2 als Standart gesetzt. Da dieses Projekt schon auf den Nachfolger Python3 setzt, muss dies manuell geupdated werden.\
   Ebenfalls gibt es eine neue Version des Betriebssystems, wesshalb ein update des RaspberryPi über apt-get update nicht möglich ist.\
   Beide Umstände lassen sich jedoch durch folgenden Befehl beheben, da im neuen Betriebssystem Python3 als Standartversion gesetzt ist.
   ```shell
   sudo apt-get --allow-releaseinfo-change update
   ```
   ```shell
   sudo apt-get upgrade
   ```
   
   Das neue Betriebssystem soll jedoch laut Support des Displayherstellers in einem nächsten Update des Images direkt verwendet werden.
 
6. Installieren von PyUSB 1.0
   ```shell
   sudo apt-get install python-usb python3-usb
   ```
7. Starten des Programmes mit dem Befehl
   ```shell
   sudo python Smart-Fridge/main.py
   ```

## Einrichtung des Magnetschlosses

1. Anschluss aller GPIO Pins an das Display über Kabel\
   Dabei den 5V Anschluss von Pin 4 nicht mit dem Display verbinden
2. Das Relais mit den GPIO Pins wie im folgenden Bild verkabeln\
   a) Braunes Kabel zu GND (Pin 39)\
   b) Orangenes Kabel zu 5V (Pin 4)\
   c) Rotes Kabel zu GPIO 19 (Pin 35)\
   Dies sollte nun wie folgt Aussehen:\
   ![](images/relais_rasp.png?raw=true)
3. Ein 12V Netzteil mit einem Adapter auf Klemmen verbinden.
4. Die Klemmen mit einem Kabel des Magnetschloss sowie dem Eingang des Releais verbinden.
5. Das andere Kabel des Magnetschlosses mit dem Ausgang des Relais verbinden\
   Dies sollte so Aussehen:\
   ![](images/relais_lock.png?raw=true)
   
## Setup von Node-RED
Eine genaue Anleitung ist auf dieser [Website](https://nodered.org/docs/getting-started/raspberrypi#installing-and-upgrading-node-red) zu finden, alle relevanten Befehle sind jedoch hier beschrieben:\
1. Installation von Node-RED
   ```shell
   bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered) --nodered-version="1.3.5"
   ```
2. Autostart on boot
   ```shell
   sudo systemctl enable nodered.service
   ```
3. Wenn man Norde-RED direkt benutzt möchte muss man es manuell starten:\
   ```shell
   node-red-start
   ```
4. Dann ist der Editor über
   http://http://raspberrypi.local:1880
   erreichbar
   
5. Im vorletzten Schritt müssen wir noch das requests Package installieren um Nachrichten über das node.py Modul schicken zu können
   ```shell
   python -m pip install requests
   ```
6. Im lettzen Schritt müssen wir noch die Twitter Nodes installieren
   ```shell
   cd .node-red/
   ```
   ```shell
   npm install node-red-node-twitter
   ```

   
   
   
## Kauflinks (keine Affiliate Links)
Hier eine Liste an Komponenten wie sie im Projekt genutzt und getestet wurden. (Wir bekommen keine Vergütung wenn über diese Links ein Produkt gekauft wird)\
[Komplette Liste](https://www.reichelt.de/my/1877276 "reichelt.de")\
Einzelne Produkte:\
* [Raspberry Pi](https://www.reichelt.de/DE/DE/raspberry-pi-4-b-4x-1-5-ghz-2-gb-ram-wlan-bt-rasp-pi-4-b-2gb-p259919.html?r=1&src=raspberrypi "reichelt.de")
* [Netzteil](https://www.reichelt.de/raspberry-pi-netzteil-5-1-v-3-0-a-usb-type-c-eu-stecker-s-rpi-ps-15w-bk-eu-p260010.html?&nbc=1&trstct=lsbght_sldr::259919 "reichelt.de")
* [Touchscreen Display](https://www.reichelt.de/raspberry-pi-shield-display-lcd-touch-3-5-480x320-pixel-xp-rasp-pi-3-5td-p202827.html "reichelt.de")
* [Gehäuse für Raspberry Pi mit Display](https://www.reichelt.de/gehaeuse-fuer-raspberry-pi-4-3-5-display-rpi-case-3-5-tr-p272260.html?&nbc=1&trstct=lsbght_sldr::202827 "reichelt.de")
* [Micro SD Karte, Rasp OS vorinstalliert](https://www.reichelt.de/raspberry-pi-os-3-7-16gb-microsd-karte-vorinstalliert-rasp-os-16gb-p165071.html?&trstct=pol_1&nbc=1 "reichelt.de")
* Optional [Kühlsatz](https://www.reichelt.de/raspberry-pi-4-kuehlsatz-4-teilig-silber-rpi-cool-4xsi-p261927.html?&nbc=1&trstct=lsbght_sldr::259919 "reichelt.de")

