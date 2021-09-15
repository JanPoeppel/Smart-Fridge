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
Touchscreen Display


## Installation (ohne Vorwissen)

Download der .zip Datei\
Alle nötigen Vorraussetzungen installieren
```shell
pip3 install -r requirements.txt
```
Den Raspberry rebooten.
```shell
sudo reboot -r now
```
Das Programm sollte sich nun automatisch beim starten öffnen.\
Manuell kann es aber auch mit folgendem Befehl gestartet werden
```shell
python main.py
```
## Installation (mit Vorwissen)
Clonen des Github Projekt
```shell
$ git clone https://github.com/JanPoeppel/Smart-Fridge.git
```
Installation aller Vorraussetzungen
```shell
TODO python 3 als standart
```



Verlinkung zum doc und noch füllen

- Auflösung des Display setzten
- Anzeigeeinstellungen auf medium 

- python 3 als standart

wenn programmierer: gpg fehler lösung:https://canox.net/2018/10/gpg-unpassender-ioctl-i-o-control-fuer-das-geraet-fehler-beheben/

## Kauflinks (keine Affiliate Links)
Hier eine Liste an Komponenten wie sie im Projekt genutzt und getestet wurden. (Wir bekommen keine Vergütung wenn über diese Links ein Produkt gekauft wird)\
[Raspberry Pi](https://www.reichelt.de/DE/DE/raspberry-pi-4-b-4x-1-5-ghz-2-gb-ram-wlan-bt-rasp-pi-4-b-2gb-p259919.html?r=1&src=raspberrypi "reichelt.de"){:target="_blank" rel="noopener"} 
[go](http://stackoverflow.com){:target="_blank" rel="noopener"} 
<a href="http://stackoverflow.com" target="_blank">external link</a>
