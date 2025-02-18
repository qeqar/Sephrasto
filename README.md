# Sephrasto
Ein Charaktergenerator für das DSA-Hausregelsystem Ilaris, erstellt von Aeolitus. So vollständig wie möglich. Eine Gebrauchsanweisung findest du, wenn du im Hauptfenster auf den Hilfe-Button clickst.

## Features
* Automatisches Befüllen des Ilaris Charakterbogens (Benötigt pdftk : Gratis-Download für Windows @ https://www.pdflabs.com/tools/pdftk-server/, Mac- und Linux-Installation siehe unten)
* Einfaches Einarbeiten von Hausregeln wie neuen Fertigkeiten, Vorteilen etc. durch frei editierbare Regelbasis
* Fast alle relevanten Regeln sind im Tool enthalten

Bei Fragen / Änderungswünschen / Feedback einfach Bescheid sagen - im dsaforum oder hier!

## Verwendete Pakete und Programme
* Um Sephrasto mit Python zu verwenden, wird mindestens Version 3.6 benötigt, Version 3.7+ wird aber empfohlen. 
* PySide6 (https://www.qt.io/qt-for-python) für die Grafische Oberfläche
* lxml (http://lxml.de/) als xml-parser (unter Linux: `libxml2-dev` und `libxmlsec1-dev` global installieren, wenn lxml via pip installiert werden soll)
* PyYAML (https://pyyaml.org/) als yaml-parser
* requests (https://github.com/psf/requests) für den update checker. Dieses Paket ist abhängig von:
    * charset-normalizer (https://github.com/Ousret/charset_normalizer)
    * certifi (https://github.com/certifi/python-certifi)
    * idna (https://github.com/kjd/idna)
    * urllib3 (https://urllib3.readthedocs.io)
* cx_freeze (optional, https://github.com/marcelotduarte/cx_Freeze) um Sephrasto-Builds zu erstellen

Mitgeliefert werden außerdem:
* fdfgen (https://github.com/ccnmtl/fdfgen) zum Editieren des Charakterbogens
* convert (nur Windows, https://imagemagick.org) zum Einfügen des Charakterbilds in den Charakterbogen
* cpdf (https://www.coherentpdf.com) zur Reduzierung der Dateigröße des Charakterbogens

Die zugehörigen Lizenzen können hier gefunden werden: [Acknowledgements](src/Sephrasto/Doc/Acknowledgements.md)

## Installation Linux (Ubuntu/Debian)
```
sudo apt install python3-pip
sudo apt install openjdk-11-jdk
sudo apt install pdftk
git clone https://github.com/Aeolitus/Sephrasto.git
pip install -r Sephrasto/requirements.txt
```
Alternativ zu pip stehen auch Poetry files zur Verfügung. OpenJDK wird für pdftk benötigt, ohne diese beiden Pakete können keine Charakterbogen-PDFs erzeugt werden. Statt das Sephrasto Repository mit git zu klonen, kannst du es natürlich auch manuell herunterladen und entpacken (unter "Code" den Punkt "Download zip" auswählen).

Gestartet wird Sephrasto dann folgendermaßen:
```
python Sephrasto/src/Sephrasto/Sephrasto.py
```

### Sephrasto Userordner ###
Wenn dich der automatisch generierte Sephrasto-Ordner im Userverzeichnis stört, kannst du ihn von "sephrasto" in ".sephrasto" umbenennen, um ihn zu verstecken. Sephrasto wird dann den "sephrasto" Ordner nicht neu erstellen.

### Charakterbild ###
Das Charakterbild kann im Beschreibung-Details Tab hinzugefügt werden (nur mit langem Charakterbogen sichtbar). Sollte die PDF-Erstellung mit Charakterbild nicht gelingen und wird dir folgende Fehlermeldung angezeigt:
```
Das Einfügen des Charakterbilds ist fehlgeschlagen: Command [...] returned non-zero exit status 1.. Der Charakterbogen wird nun ohne das Bild erstellt.
```
Dann öffne `etc/ImageMagick-{Version}/policy.xml` und füge unten die Zeile
```
<policy domain="coder" rights="read | write" pattern="PDF" />`
```
hinzu. Deine Versionsnummer musst du selbst eintragen. Getestet wurde bisher nur mit ImageMagick-Version 6 und höher. Die Datei ist vermutlich bei dir schreibgeschützt. Du kannst sie beispielsweise mit `sudo nano etc/ImageMagick-{Version}/policy.xml` öffnen, bearbeiten und speichern. Bedenke, dass die Änderung der Policy nicht nur für Sephrasto, sondern auch für andere Programme gilt, die ImageMagick nun für PDF-Bearbeitung frei nutzen können. Stelle via ```gs --version``` sicher, dass deine Ghostscript-Installation mindestens die Version 9.24 hat, ansonsten stellt diese Änderung ein Sicherheitsrisiko dar ([siehe hier](https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion).

## Installation Windows
Für Windows stellen wir unter https://github.com/Aeolitus/Sephrasto/releases builds zur Verfügung.

## Installation macOS
* Lade den neuesten Sephrasto Sourcecode herunter (https://github.com/Aeolitus/Sephrasto/releases) und entpacke ihn an einen Ort deiner Wahl. 
* Installiere Python 3: https://www.python.org/downloads/macos/
* Control-Click auf den Sephrasto-Ordner und wähle "New Terminal at Folder"
* Tippe im Terminal: ```python3 -m ensurepip```
* ... gefolgt von: ```python3 -m pip install -r requirements.txt```
* Installiere pdftk von folgendem Link: https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk_server-2.02-mac_osx-10.11-setup.pkg
 WICHTIG: Nutze bitte den genannten Link. Der Download-Button auf der Webseite führt zu einer alten Version, die nicht mehr funktioniert (Stand 08/22).
* Wechsle im Sephrasto-Ordner in src/Sephrasto
* Control-Click auf Sephrasto.py -> Get Info -> Open with -> "Python Launcher" auswählen.

Gestartet wird Sephrasto dann folgendermaßen:
* Doppelclick auf Sephrasto.py (natürlich kannst du auch ein Alias erstellen)
* Beim ersten Start musst du über System Preferences -> Security & Privacy noch die Ausführung erlauben. Beim ersten PDF-Export das gleiche für cpdf.
* Optional kannst du im Python Launcher noch "Run in a Terminal window" deaktivieren, um das zusätzliche Terminalfenster loszuwerden

### Charakterbild ###
Für Sephrastos Charakterbildfeature wird imagemagick benötigt, das leider in der aktuellen Version nicht funktioniert wie es soll. Ein Bugreport wurde bereits abgesendet: https://github.com/ImageMagick/ImageMagick/issues/5439. Falls du es dennoch installieren möchtest oder der Bug inzwischen behoben wurde, kannst du den folgenden Befehl nutzen: ```brew install imagemagick```. Benötigt den Homebrew Paketmanager https://brew.sh.

## Für Entwickler

### Erstellen von Windows builds
Stelle sicher, dass alle Pakete aus der requirements.txt installiert sind. Aktuell nutzen wir außerdem Python 3.9.7 und cx_Freeze 6.13.1 zum Erstellen von Windows builds. Nun solltest du build.bat im Sephrasto root ausführen können.

### Einrichtung von Visual Studio als IDE:
* Installiere VS 2019 Community Edition mit dem Python Workload (kann auch nachträglich über den Installer installiert werden)
* Setze den Pfad der Python-Umgebung in der Umgebungsvariable PATH (in der Regel C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64)
* Öffne Sephrasto/src/Sephrasto.sln
* Installiere die dependencies: Solution Explorer -> Python Environments -> Rechtsclick auf Python 3.x -> Install Python Package.
* Stelle zuerst sicher, dass deine pip Version aktuell ist, aktualisiere diese gegebenenfalls und starte Visual Studio neu
* Installiere nun die oben genannten Pakete im gleichen Menu.
* Erstelle die IntelliSense Datenbank: Solution Explorer -> Rechtsclick auf Python Environments -> View all Python environments -> IntelliSense im Dropdown auswahlen und aktivieren/refreshen
* Stelle das Tab-Verhalten auf "Insert Spaces": Tools -> Options -> Text Editor -> Python -> Tabs
* Öffne das Exception Settings Fenster (Debug -> Windows -> Exception Settings) und selektiere alle Python Exceptions, dann deaktiviere <All Python Exceptions not in this list>, BaseException und Exception - damit breaken die custom exceptions nicht, die Sephrasto intern nutzt.

### UI design mit Qt
* Modifiziere niemals Dateien im "src/Sephrasto/UI" Ordner von Hand!
* Stattdessen wird das UI durch ".ui"-XML-Dateien im "designer" Ordner definiert. Optionalerweise können diese mit dem Qt Creator visuell designed werden (enthalten im Qt-Installer unter https://www.qt.io/).
* Aus diesen Dateien wird dann der Python-Code mit Hilfe von "designer/convert.bat" erzeugt.
* Bei Problemen mit convert.bat, stelle sicher, dass:
    * ... der Python Install-Ordner und der Unterordner "Scripts" in deiner PATH-Umgebungsvariable enthalten sind. Dies wird normalerweise vom Python installer automatisch gemacht. (Windows 10: System -> Advanced System Settings -> Environment Variables -> Path - in User oder System)
    * ... "Python/Scripts" die Datei "pyside6-uic.exe" enthält. Diese wird normalerweise durch das Installieren von PySide6 dort angelegt.

## Abschlussbemerkung
Dieses Tool ist das Projekt, an dem ich Python / Qt gelernt habe. Deutliche Schwankungen im Coding-Stil und in der Codequalität sind demnach zu erwarten. Ich werde über die Zeit versuchen, das zu beheben; einige Spuren davon (wie das furchtbare denglisch) werden vermutlich bleiben. 