:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Forms
********************************************************************************

Custom entry form
================================================================================

#. Choose :menuselection:`File --> Open Project...` from the menu bar

#. Select :file:`QGIS-NaturalEarth-Example.qgs` and press :guilabel:`Open`


#. Zoom in somewhere to speed up redrawing

#. Click :menuselection:`Layer --> Add PostGIS Layer...`.

#. Press :guilabel:`Connect` on NaturalEarth connection

#. Select :file:`10m_populated_places_simple` in the table list

#. Press :guilabel:`Add` and :guilabel:`Close`

#. Double click :file:`10m_populated_places_simple` in the Layers tree

#. Go to the tab :guilabel:`Fields` and set the Edit widget types:

   .. image:: ../images/forms_fields.png
     :scale: 70 %

#. For the field :file:`ISO_A2` create a value map loading data from a layer:

   .. image:: ../images/forms_valuemap.png
     :scale: 70 %

#. Activate the edit mode and digitize a point to see the new edit form:

   .. image:: ../images/forms_digitizing.png
     :scale: 70 %


Forms with QT Designer
================================================================================

.. - Mit Attributenamen versehene Bearbeitungselemente werden mit Attributwerten initialisiert
.. - Knöpfe mit Aktionsnamen mit Aktionen verknüpft.
.. - Optionalle Python-Funktion für weitere Initialisierung
.. - Bearbeitungsfelder mit Namenspräfix „expr_“ mit Feldrechnerausdrücken

QGIS supports also custom forms, created with the QT GUI Designer.
QGIS relies on naming conventions for data fields and expressions.
This allows QGIS to run forms created with QT designer without compilation.

For installing QT designer, open a terminal:

#. Click :menuselection:`Applications --> Accessories --> Terminal Emulator`

#. Type :command:`sudo apt-get install qt4-designer` (Password: user)


Now we create a custom form with QT Designer:

#. Click :menuselection:`Applications --> Development --> QT 4 Designer`

#. Select “Dialog with Buttons Bottom”

   We follow the article on http://woostuff.wordpress.com/2011/09/05/qgis-tips-custom-feature-forms-with-python-logic/

   In our case we create an entry form "My custom places" with an entry field :file:`name` and a read only key field :file:`gid`

#. Save it as :file:`places.ui` in /home/user


Open QGIS again and:

#. Double click :file:`10m_populated_places_simple` in the Layers tree

#. Go to the tab :guilabel:`General`, choose :file:`/home/user/places.ui` as :guilabel:`Edit UI` and press :guilabel:`OK`

#. Activate the edit mode and digitize a point to see your new custom form
