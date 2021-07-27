# Terminkalender
Abschlussprojekt 12. Klasse Informatik Leistungskurs Jahrgang 2020/2021. Terminkalender zum organisieren von Treffen zwischen verschiedenen Gruppen.

Bedingung des Kalenders.
In der Mitte Ihres Fensters können sie einen Kalender erkennen. Indem Sie oben link oder oben Recht auf die Pfeile des Kalenders klicken können Sie einen Monat nach vorne oder einen Monat nach hinten Springen. In welchem Monat und Jahr Sie sich gerade befinden können sie oben in der Mitte des Kalenders ablesen. Unter dieser Zeile gibt es eine Zeile, wo die Wochentage abgekürzt aufgeschrieben sind. Wenn Sie diese Spalten nach unter verfolgen können Sie ablesen, welches genaue Datum der Wochentag hat. Der aktuelle Wochen Tag ist gelb hinterlegt. Wenn Sie mit der Maus über einer bestimmten Zahl (Datum) sind erscheint ihnen ein Fenster. In diesem Fenster können Sie Informationen zu dem Termin angeben. Schreiben Sie dazu Ihre Information in das Feld indem grau “Informationen” steht und klicken sie auf den Butten mit der Bezeichnung “Abschicken”.
Anmelden / Neuer Benutzer 
Wenn Sie sich Anmelden möchten oder sich einen neuen Account zulegen wollen klicken Sie untern recht in der Ecke auf den Button mit der Bezeichnung Anmelden. Wenn sie schon einen Account haben können sie hier nun Ihren Benutzername und das Passwort eingeben und auf den Button mit der Bezeichnung “Anmelden” klicken.
Sie möchten sich einen neuen Account zulegen? 
Klicken Sie dazu auf den Button mit der Bezeichnung “Neuer Benutzer”. Sie werden nun zu einem neuen Fenster weitergeleitet wo Sie sich einen Namen und ein Passwort überlegen sollen. Denken Sie daran ein möglichst Langes Passwort zu Wählen mit Sonderzeichen, Zahlen und Groß- und Kleinbuchstaben damit Ihr Account möglichst Sicher vor Angriffen ist. Wenn sie Ihr Passwort zweimal richtig Eingegeben haben können Sie auf den Butten mit der Bezeichnung “Neuen Benutzer erstellen” klicken. 
Wo sehe ich ob ich angemeldet bin?
Um zu überprüfen ob Sie angemeldet sind schauen Sie in die Rechte obere Ecke. Wenn dort ihr Benutzername steht sind Sie aktuell angemeldet.

Abmelden
Um sich abzumelden klicken Sie bitte oben recht auf Ihren Benutzername und dann auf den Button mit der Bezeichnung “Abmelden”. Wenn Ihr Benutzername oben recht nicht mehr zu sehen ist und der Text “Hier Benutzername einfügen” dort steht sind Sie abgemeldet.
Home-Button
Durch einen Klick auf den Blauen Home-Button oben links in der Ecke können Sie immer wieder zu Startseite zurückkehren.
Gruppenname / Neue Gruppe 
Um sich die Namen der Gruppe anzeigen zu lassen oder eine neue Gruppe zu erstellen klicken Sie bitte recht neben dem Home-Button auf den Button mit der Bezeichnung “Gruppen”. Dort haben Sie dann einmal die Möglichkeit auf den Button mit der Bezeichnung “Gruppenname” zu klicken, dann werden Ihnen die Namen der Gruppen angezeigt, in denen Sie aktuell sind. Um eine neue Gruppe zu erstellen klicken Sie bitte auf den Button mit der Bezeichnung “Neue Gruppe”. Hier werden Sie dann wieder auf eine andere Seite verwiesen, wo Sie Ihren Gruppennamen und Gruppenmitglieder angeben können. Die Gruppenmitglieder beim Hinzufügen bitte mit einem Komma voneinander getrennt hinschreiben. Nun noch auf den Button mit der Bezeichnung “Neue Gruppe erstellen” klicken und die Gruppe ist erstellt. Mit einem Klick auf den Button mit der Bezeichnung “Home” kommen Sie nun wieder zurück ins Startmenu.

Close Button
Mithilfe des Buttons mit der Bezeichnung “Close” können Sie die Dropdown Menus jederzeit wieder schließen.

Einrichtung

Zuerst muss der Apache Server installiert werden. Dafür die Datei vom 1. Link downloaden (httpd-2.2.25-win32-x86-no_ssl.msi). Öffnen sie diese und folgen sie den Anweisungen.
Anschließend Python 2.5 vom 2. Link installieren und den Anweisungen folgen. Ist dies geschehen kann nun der Python Mod von Apache installiert werden. Python 2.5 wird von nun an nicht mehr gebraucht. Der Python Mod wird benötigt, um die geöffneten Dateien einem Interpreter zuweisen zu können. Damit diese Änderung auch wirksam wird muss die Datei “httpd.conf” im Ordner “C:\Program Files (x86)\Apache Software Foundation\Apache2.2\conf” geöffnet werden. Dort sollte die Zeile “#LoadModule python_module modules/mod_python.so” zu finden sein. Das “#” muss entfernt werden, um die Mod zu aktivieren. 
Zum Schluss müssen sie Python 3.7.8 installieren (Maschineninstallation empfohlen. Möglich bei erweiterten Einstellungen und dann der Haken bei “für alle User installieren”). Ist dies geschehen bleibt noch den Pfad zu ihrer “python.exe” von Python 3.7.8 in die erste Zeile der Datei “python.py” (Skript-Ordner) zu schreiben (#!C:/Pfad/Python37_64/python.exe). Diesen Pfad können sie sich gleich merken. Im selben Ordner wie die “python.exe” sollte der Ordner “Scripts” sein. Zu diesem müssen sie im Terminal (als Administrator ausgeführt) navigieren. Installieren sie nun, wenn nicht bereits geschehen “pip”, indem die “pip install pip” in die Kommandozeile eintragen. Nun muss ein Python Modul mit dem Befehl “pip install websockets” installiert werden. 
Ist dies ebenfalls erledigt müssen sie den Ordner “C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs” öffnen. Dort sollte sich die Datei “index.html” befinden. Löschen sie diese und kopieren sie alle Dateien aus dem Skript-Ordner in den Ordner “htdocs”. Nun sind sie in der Lage, wie in der Präsentation, unser Projekt nutzen zu können. Geben sie einfach in einen Internetbrowser (wahlweise MS Edge) “localhost” oder “127.0.0.1” ein und starten sie ihr Erlebnis. Aufgrund der diversen Auswahlmöglichkeiten bei der Umsetzung von Python Skript in HTML ist diese Variante etwas umständlicher. 
Anmerkung: Bereits heruntergeladene Setups finden sie anbei.
Links:
https://archive.apache.org/dist/httpd/binaries/win32/httpd-2.2.25-win32-x86-no_ssl.msi
https://www.python.org/ftp/python/2.5/python-2.5.msi
https://archive.apache.org/dist/httpd/modpython/win/3.3.1/mod_python-3.3.1.win32-py2.5-Apache2.2.exe
https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64.exe
