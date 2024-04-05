# TODO

* Auswertung
  * [ ] Spalte für Ränge
  * [ ] Button, um Urkunden zu generieren
    * f"Urkunden sind in {GENERATED_DIR}"
  * [ ] Linien, um Routen zu trennen
  * [ ] Button, um PDF der Urkunden zu öffnen

* try weights could be set in code
  * depends on number of tries

* [ ] python files in new directory `src/`
* [ ] remove redundant files
  * `testing.py`
  * `make_urkunden.py`
* [ ] unit tests

## Makefile (oder Ähnliches)

* [ ] Befehle für
  * Routenzettel
  * Etiketten
  * Laufzettel
    * `generated/routen.csv` mit Python generieren und `pdflatex` ausführen 
  * Urkunden
    * Falls `generated/teilnehmer.json` existiert, Ränge abspeichern `generated/ergebnisse.csv` und `pdflatex` ausführen

## Andere Features

* [ ] Anzahl Versuche
  * pro Gruppe
  * in `gruppen.csv`
  * [ ] `laufzettel.tex` anpassen

* [ ] Was ist, wenn 2 Teilnehmer den selben Namen haben?
  * ID für Teilnehmer

* [ ] Alter und Gruppe der Teilnehmer automatisch bestimmen
  * [ ] verwende Datum in `bewerb.csv`

## Farben in Auswertung

* andere Farben für Routen
