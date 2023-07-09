# Wetter-Webapp

Diese Anwendung ermöglicht es Benutzern, das Wetter einer bestimmten Stadt abzufragen und die aktuelle Temperatur, die Wetterbedingungen sowie die Vorhersage für die nächsten drei Tage anzuzeigen. Die Daten werden über die OpenWeatherMap-API abgerufen und in einer übersichtlichen Benutzeroberfläche präsentiert.

Die Anwendung ist als Single-Page-Webapp ausgelegt und verwendet Flask für das Backend.

## Designentscheidungen

Die Wahl fiel auf Flask als Backend-Webframework, weil es leicht und einfach zu verwenden ist, was perfekt für eine Single-Page-Anwendung ist. Flask eignet sich auch gut für Projekte, bei denen API-Anfragen benötigt werden.

Die Frontend-Entwicklung basiert auf HTML und CSS mit Bootstrap, um eine reaktionsfähige Benutzeroberfläche zu erstellen, die auf verschiedenen Geräten gut aussieht.

Die Verwendung der OpenWeatherMap-API wurde wegen ihrer umfangreichen Dokumentation und Zuverlässigkeit bevorzugt.

## Installation

Stellen Sie sicher, dass Python 3.7 oder höher auf Ihrem System installiert ist.

Klonen Sie das Repository:

```console
git clone https://github.com/IhrUsername/wetter-webapp.git
```

Wechseln Sie in das Projektverzeichnis:

```console
cd wetter-webapp
```

Installieren Sie die benötigten Pakete:

```console
pip install -r requirements.txt
```

Erstellen Sie eine .env-Datei im Hauptverzeichnis und fügen Sie Ihren OpenWeatherMap-API-Schlüssel hinzu:

```console
OPENWEATHER_API_KEY=Ihr_API_Schlüssel
```

## Ausführung des Projekts

Starten Sie das Projekt mit folgendem Befehl:

```console
python app.py
```

Öffnen Sie anschließend einen Webbrowser und navigieren Sie zu http://localhost:5000.

## Fehlerbehandlung

Im Falle eines Fehlers bei der API-Anfrage wird eine entsprechende Fehlermeldung zurückgegeben. Sowohl clientseitige als auch serverseitige Fehler werden berücksichtigt, um sicherzustellen, dass die Anwendung stabil bleibt. Insbesondere bei Fehlern im Zusammenhang mit der API-Anfrage werden geeignete Fehlermeldungen ausgegeben.

## Sicherheitspraktiken

API-Schlüssel und sensible Informationen werden nicht im Code gespeichert, sondern in Umgebungsvariablen.
Fehler werden behandelt, um sicherzustellen, dass die Anwendung stabil bleibt und keine sensiblen Informationen preisgibt.
Alle Anfragen an die API sind http(s), um die Datenübertragung zu sichern.
