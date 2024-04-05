# Kletterbewerb

Das Ziel dieses Projekts ist es, die Organisation von (Kletter)bewerben zu vereinfachen.
Es werden z.B. Urkunden und Laufzettel generiert.
Außerdem macht es eine Anwendung für die Eingabe der Punkte einfach, die Ränge der Teilnehmer zu bestimmen und Urkunden zu generieren.

Um das Projekt zu verwenden, werden LaTeX und Python benötigt.

## Verwendung

### Daten eingeben

* Kopiere den Ordner `data/template/` und nenne ihn um.
* Erstelle die Datei `data/aktuell.txt`, die als Inhalt den Namen des Ordners haben soll.
* Fülle die CSV-Dateien in diesem Ordner mit den Daten der Veranstaltung.

### Dokumente generieren

* Führe `set_data.py` aus.
* Kompiliere entsprechende Tex-Dateien.

* Alternativ kann man auf Linux das Skript `make_pdfs.sh` ausführen.

### Auswertung und Urkunden

1. Führe `auswertung.py` aus.
2. Trage die Punkte der Teilnehmer ein.
3. Klicke auf "Speichern", um die Ränge zu berechnen und die Ergebnisse zu speichern.
4. Erstelle die Urkunden in `latex/urkunden/` mit `pdflatex urkunden.tex`. `pdflatex` muss zweimal ausgeführt werden.

## Installation

### Python

Alle Voraussetzungen für Python sind in `pyproject.toml`.
Um sie mit [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) zu installieren, führe `poetry install` bzw. `poetry install --only main`, wenn keine Entwicklungsvoraussetzungen gebraucht werden, aus.
Verwende den Python-Interpreter der durch Poetry erzeugten Umgebung (z.B. in einer IDE).

### Latex

Installiere Latex und entsprechende Pakete.
