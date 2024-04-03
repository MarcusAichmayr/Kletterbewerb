# Kletterbewerb

Das Ziel dieses Projekts ist es, die Organisation von (Kletter)bewerben zu vereinfachen.
Es werden z.B. Urkunden und Laufzettel generiert.
Außerdem macht es eine Anwendung für die Eingabe der Punkte einfach, die Ränge der Teilnehmer zu bestimmen und Urkunden zu generieren.

Um das Projekt zu verwenden, werden LaTeX und Python benötigt.

## Verwendung

### Daten eingeben

* Kopiere den Ordner `data_template` und nenne ihn auf `data` um.
* Passe die CSV-Dateien in diesem Ordner an.

### Dokumente generieren

* Führe `set_data.py` aus.
* Kompiliere entsprechende Tex-Dateien.

* Alternativ kann man auf Linux das Skript `make_pdfs.sh` ausführen.

### Auswertung und Urkunden

Um die Anwendung zu starten, TODO

1. Starte die Anwendung TODO
2. Trage die Punkte der Teilnehmer ein.
3. Drücke entsprechende Buttons, um die Ergebnisse zu speichern und die Urkunden zu generieren.

## Installation

### Python

Alle Voraussetzungen für Python sind in `pyproject.toml`.
Um sie mit [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) zu installieren, führe `poetry install` bzw. `poetry install --only main`, wenn keine Entwicklungsvoraussetzungen gebraucht werden, aus.
Verwende den Python-Interpreter der durch Poetry erzeugten Umgebung (z.B. in einer IDE).

### Latex

Installiere Latex und entsprechende Pakete.
