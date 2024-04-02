# TODO

## Punkte eintragen

* Es gibt mehrere Möglichkeiten:
  * [x] Interface machen, um Punkte einzutragen
    * Python oder Godot
  * In CSV-Datei eintragen und laden.

## Makefile (oder Ähnliches)

* [ ] Befehle für
  * Routenzettel
  * Etiketten
  * Laufzettel
    * `generated/routen.csv` mit Python generieren und `pdflatex` ausführen 
  * Urkunden
    * Falls `generated/teilnehmer.json` existiert, Ränge abspeichern `generated/ergebnisse.csv` und `pdflatex` ausführen

## Andere Features

* [x] Punkte, Ergebnisse und Ränge abspeichern
  * in csv?

* [ ] Anzahl Versuche
  * pro Gruppe
  * in `gruppen.csv`
  * [ ] `laufzettel.tex` anpassen

* [ ] Was ist, wenn 2 Teilnehmer den selben Namen haben?

* [ ] Alter und Gruppe der Teilnehmer automatisch bestimmen
  * [ ] verwende Datum in `bewerb.csv`
