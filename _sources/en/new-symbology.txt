:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
New symbology features
********************************************************************************

.. Three new classification modes added to graduated symbol renderer http://linfiniti.com/2010/09/new-class-breaks-for-graduated-symbols-in-qgis/
.. Data-defined rotation and size for categorized and graduated renderer (symbology-ng).

Multiple symbol layers for road symbolization
================================================================================

#. Choose :menuselection:`File --> Open Project...` from the menu bar

#. Select :file:`QGIS-NaturalEarth-Example.qgs` and press :guilabel:`Open`

#. Zoom in somewhere to speed up redrawing

#. Click :menuselection:`Layer --> Add Vector Layer` from the menu bar

#. Press :guilabel:`Browse` and navigate to :file:`/home/user/data/north_carolina/shape/roadsmajor.shp` and press :guilabel:`Open`

#. Go to the tab :guilabel:`Coordinate Reference System (CRS)`, check :guilabel:`Enable 'on the fly' CRS transformation` and press :guilabel:`Ok`

#. Right click :file:`roadsmajor` in the Layers tree and select :menuselection:`Zoom to layer extent`

#. Double click :file:`roadsmajor` in the Layers tree and activate the :guilabel:`Style` tab 

#. Press the :guilabel:`Change` button to edit the line symbol

#. Change the color to black and set 2mm pen width

#. Press :guilabel:`+` to add a second symbol layer

#. Change the color to white and set 1mm pen width

   .. image:: ../images/roadsymbol.png
     :scale: 70 %

#. Press :guilabel:`Ok` and :guilabel:`Apply`

   * You should see the major roads, but with artefacts at the end of line segments

#. Press the :guilabel:`Symbol levels` button and check :menuselection:`Enable symbol levels`

   .. image:: ../images/roadsymbollevels.png
     :scale: 70 %

#. Press :guilabel:`Ok` and :guilabel:`Ok` again to close the Layer properties

   * You should see the major roads with the black symbol layer draws first and the white layer on top
