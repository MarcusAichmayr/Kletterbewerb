# Kletterbewerb

Das Ziel dieses Projekts ist es, die Organisation von (Kletter)bewerben zu vereinfachen.
Es werden z.B. Urkunden und Laufzettel generiert.

Um das Projekt zu verwenden, werden LaTeX und Python benötigt.

## Daten eingeben

* Kopiere den Ordner `data_template` und nenne ihn auf `data` um.
* Passe die CSV-Dateien in diesem Ordner an.

## Dokumente generieren

* Führe `set_data.py` aus.
* Kompiliere entsprechende Tex-Dateien.

* Alternativ kann man auf Linux das Skript `make_pdfs.sh` ausführen.

## Auswertung

TODO

1. Trage Punkte der Teilnehmer ein.
2. Führe Skript TODO aus.

## Installation

All dependencies are listed in `pyproject.toml`.
To install them with [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer),
call `poetry install` (or `poetry install --only main` if you don't need development dependencies) 
In your IDE, you may want to set the python interpreter used to be the one in the created environment.
