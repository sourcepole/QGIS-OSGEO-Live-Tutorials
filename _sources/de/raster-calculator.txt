:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Rasterrechner
********************************************************************************

Verwendung des Rasterrechners
================================================================================

#. Wählen sie :menuselection:`Datei --> Neues Projekt`

#. Klicken sie auf :menuselection:`Layer --> Rasterlayer hinzufügen...`

#. Öffnen sie die Datei :file:`/home/user/data/raster/SRTM_u03_n041e002.tif`

#. Klicken sie auf :menuselection:`Raster --> Rasterrechner...`

#. Geben sie eine Formel und eine Datei für das Resultat ein:

   .. image:: ../images/rastercalc_mountains.png
     :scale: 70 %

#. Doppelklicken sie :file:`mountains` Im Layerbaum und setzen sie :guilabel: `Einkanaleigenschaften -->Farbabbildung` auf :guilabel:`Pseudofarben`

   .. image:: ../images/rastercalc_colormap.png
     :scale: 70 %

#. Kombinieren sie beide Raster, um alle Punkte unter 1000 Meter zu löschen:

   .. image:: ../images/rastercalc_srtm_mountains_only.png
     :scale: 70 %

#. Das Resultat ist ein DEM ohne Punkte unter 1000 Meter:

   .. image:: ../images/rastercalc_srtm_mountains_only_pseudocolor.png
     :scale: 70 %
