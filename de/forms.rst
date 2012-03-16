:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Formulare
********************************************************************************

Formulare mit Benutzerdefinierten Elementen
================================================================================

#. Wählen sie :menuselection:`Datei --> Projekt öffnen...` vom Menü

#. Wählen sie die Datei :file:`QGIS-NaturalEarth-Example.qgs` und drücken sie :guilabel:`Open`

#. Zoomen sie auf einen kleineren Ausschnitt, damit das Neuzeichnen der Kartenansicht schneller geht

#. Klicken sie :menuselection:`Layer --> PostGIS-Layer hinzufügen...`.

#. Drücken sie :guilabel:`Verbinden` bei der NaturalEarth Verbindung

#. Wählen sie :file:`10m_populated_places_simple` in der Liste

#. Drücken sie :guilabel:`Hinzufügen` und :guilabel:`Schliessen`

#. Doppelklick auf :file:`10m_populated_places_simple` im Layerbaum

#. Gehen sie zum Reiter :guilabel:`Felder` und wählen sie die gewünschten Bearbeitungselemente:

   .. image:: ../images/forms_fields.png
     :scale: 70 %

#. Erzeugen sie für das Feld :file:`ISO_A2` eine Wertabbildung und laden sie Daten aus einem Layer:

   .. image:: ../images/forms_valuemap.png
     :scale: 70 %

#. Schalten sie den Bearbeitungsmodus ein und fügen sie einen Punkt hinzu, um das neue Editierformular zu sehen:

   .. image:: ../images/forms_digitizing.png
     :scale: 70 %


Formulare mit dem QT Designer
================================================================================

.. - Mit Attributenamen versehene Bearbeitungselemente werden mit Attributwerten initialisiert
.. - Knöpfe mit Aktionsnamen mit Aktionen verknüpft.
.. - Optionalle Python-Funktion für weitere Initialisierung
.. - Bearbeitungsfelder mit Namenspräfix „expr_“ mit Feldrechnerausdrücken

QGIS unterstützt auch vollständig benutzerdefinierte Formualre, die mit dem Qt Desinger erstellt worden sind.
Es werden Namenskonventionen für Datenfelder und Ausdrücke verwendet. 
Dadurch kann QGIS die Formulare verwenden, ohne dass Code kompiliert werden muss.

Öffnen sie eine Konsole, um Qt designer zu installieren:

#. Gehen sie zum Menüeintrag :menuselection:`Applications --> Accessories --> Terminal Emulator`
#. Geben sie folgenden Text in der Konsole ein :command:`sudo apt-get update && sudo apt-get install qt4-designer` (Password: user)

Nun erzeugen wir ein benutzerdefiniertes Formular mit dem QT Designer:

#. Wählen sie :menuselection:`Applications --> Development --> QT 4 Designer`

#. Wählen sie “Dialog with Buttons Bottom”

   Wir führen die Schritte im Artikel http://woostuff.wordpress.com/2011/09/05/qgis-tips-custom-feature-forms-with-python-logic/ aus.

   In our case we create an entry form "My custom places" with an entry field :file:`name` and a read only key field :file:`gid`

#. Speichern sie das Formular als :file:`places.ui` im Verzeichnis /home/user


Öffnen sie QGIS erneut und:

#. Doppelklicken sie den Eintrag :file:`10m_populated_places_simple` im Layerbaum

#. Gehen sie zum Reiter :guilabel:`Allgemein` und wählen sie :file:`/home/user/places.ui` als :guilabel:`UI zur Bearbeitung`. Drücken sie :guilabel:`OK`

#. Schalten sie den Bearbeitungsmodus ein und fügen sie einen Punkt hinzu, um das neue Formular zu sehen.