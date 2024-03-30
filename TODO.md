# TODO

## Punkte eintragen

* Es gibt mehrere Möglichkeiten:
  * [ ] Interface machen, um Punkte einzutragen
    * Python oder Godot
  * In CSV-Datei eintragen und laden.

* mehrere Tabellen, je nach Gruppe

* [ ] Skripte, die Unterlagen generieren

## Andere Features

* [ ] Ordner `generated`, in dem man die PDFs, berechneten Ergebnisse und Logfiles findet

* [ ] Punkte, Ergebnisse und Ränge abspeichern
  * in csv?

* [ ] Metadaten eintragen
  * [ ] Name der Veranstaltung (z.B. Kletterbewerb Toprope)
    * Urkunden
    * Laufzettel
    * Etiketten
  * [ ] Datum
    * auf Laufzetteln und Urkunden verwenden
    * Alter und Gruppe der Teilnehmer bestimmen

* [x] Gruppen IDs auf Gruppennamen in eigener CSV-Datei zuordnen
  * Latex und Python müssen Daten daraus lesen
  * Altersgrenzen für Gruppen einstellen, um Gruppen automatisch zuzuordnen?
    * manuell zuordnen ist flexibler

### Finalrouten

* Wenn es zu einem Finale kommt, muss derzeit `generated/ergebnisse.csv` modifiziert werden.
* Elegant wäre es, wenn wir einfach die Finalroute ergänzen und den Finalisten die Route zuordnen.
  * Die Punkte der anderen Teilnehmer der Gruppe ändern sich aber entsprechend, damit die Ränge gleich bleiben.
