# SmartFridge

## Beschreibung
Dieses Projekt dient Jugendlichen den Zugang zu technischem sowie logischem Denken zu bieten sowie einen Anreiz zu bieten sich weiter mit dem Thema zu beschäftigen.

Durch das Projekt - welches mit dieser Anleitung auch ohne Vorkenntnisse möglich ist - wird das Problem mit der Bezahlung von Getränken und Essen behoben.

## Aufbau
Durch das Projekt werden die Grundbausteine gesetzt, welche dann durch die Jugendlichen weiter ausgebaut, verändert sowie ergänzt werden können.
Als Grundlage dient ein Raspberry Pi (getestet auf Version #TODO), ein Touchscreen und ein RFID-Reader. 
Durch eine simple Benutzeroberfläche können Jugendliche in ihrem Jugendtreff, Vereinsheim oder auch in Privaten Räumen ihre Getränke bezahlen, ohne das passende Geld dabei zu haben.\
Die Jugendlichen können sich einen RFID-Chip oder -Karte bei einem Verantwortlichen registrieren lassen und können dann Geld auf diese laden. Nun müssen die Jugendlichen nur noch den Chip beim bezahlvorgang an das Gerät halten, und der Betrag wird automatisch von ihrem Konto abgezogen.\
*Optional kann auch ein Magnetschloss am Kühlschrank oder entsprechendes Mobiliar montiert werden, welcher nach dem Bezahlvorgang das Schloss entriegelt*

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
