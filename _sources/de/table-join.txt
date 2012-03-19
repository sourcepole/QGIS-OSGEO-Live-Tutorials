:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Tabellen verbinden
********************************************************************************

Verbinden der Tabellen Admin1 -> Admin0
================================================================================

#. Wählen sie :menuselection:`Datei --> Projekt öffnen...`

#. Selektieren sie die Datei :file:`QGIS-NaturalEarth-Example.qgs` und drücken sie auf :guilabel:`Open`

#. Zoomen sie auf einen kleineren Ausschnitt, damit das Neuzeichnen der Kartenansicht schneller geht

#. Klicken sie :menuselection:`Layer --> PostGIS-Layer hinzufügen...`.

#. Drücken sie :guilabel:`Verbinden` bei der NaturalEarth Verbindung

#. Wählen sie :file:`10m_admin_0_countries` und :file:`10m_admin_1_states_provinces` in der Liste der Tabellen

#. Drücken sie :guilabel:`Hinzufügen` und :guilabel:`Schliessen`

#. Doppelclicken sie :file:`10m_admin_1_states_provinces` im Layerbaum

#. Gehen sie zum Reiter :guilabel:`Verknüpfungen` und drücken sie den :guilabel:`+`-Knopf

#. Selektieren sie :file:`10m_admin_0_countries`, :file:`adm0_a3`, :file:`adm0_a3` and drücken sie :guilabel:`OK`:

   .. image:: ../images/tablejoin.png
     :scale: 70 %

#. Klicken sie mit der rechten Maustaste auf den Eintrag :file:`10m_admin_1_states_provinces` im Layerbaum und wählen sie :menuselection:`Open attribute table`. Die Verknüpfungen sind jetzt in der Tabelle enthalten.
