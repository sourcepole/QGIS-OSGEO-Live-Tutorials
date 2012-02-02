:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Table join
********************************************************************************

Table Join Admin1 -> Admin0
================================================================================

#. Choose :menuselection:`File --> Open Project...` from the menu bar

#. Select :file:`QGIS-NaturalEarth-Example.qgs` and press :guilabel:`Open`

#. Zoom in somewhere to speed up redrawing

#. Click :menuselection:`Layer --> Add PostGIS Layer...`.

#. Press :guilabel:`Connect` on NaturalEarth connection

#. Select :file:`10m_admin_0_countries` and  :file:`10m_admin_1_states_provinces` in the table list

#. Press :guilabel:`Add` and :guilabel:`Close`

#. Double click :file:`10m_admin_1_states_provinces` in the Layers tree

#. Go to the tab :guilabel:`Joins` and press the :guilabel:`+` button

#. Select :file:`10m_admin_0_countries`, :file:`adm0_a3`, :file:`adm0_a3` and press :guilabel:`OK`:

   .. image:: ../images/tablejoin.png
     :scale: 70 %

#. To see the joined information, right click :file:`10m_admin_1_states_provinces` in the Layers tree and select :menuselection:`Open attribute table`

   * You should see all admin0 attributes at the end of a admin line
