:Author: Pirmin Kalberer
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Raster calculator
********************************************************************************

Using the raster calculator
================================================================================

#. Choose :menuselection:`File --> New Project`

#. Click :menuselection:`Layer --> Add Raster Layer...`

#. Open :file:`/home/user/data/raster/SRTM_u03_n041e002.tif`

#. Click :menuselection:`Raster --> Raster calculator...`

#. Enter output raster file and a formula:

   .. image:: ../images/rastercalc_mountains.png
     :scale: 70 %

#. Double click :file:`mountains` in the Layers tree and set the color map style to :guilabel:`Pseudocolor`

   .. image:: ../images/rastercalc_colormap.png
     :scale: 70 %

#. Combine both rasters to remove all points lower than 1000 meters:

   .. image:: ../images/rastercalc_srtm_mountains_only.png
     :scale: 70 %

#. The resulting raster is a DEM without the points lower than 1000 meters:

   .. image:: ../images/rastercalc_srtm_mountains_only_pseudocolor.png
     :scale: 70 %
