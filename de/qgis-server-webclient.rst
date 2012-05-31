:Author: Marco Hugentobler
:License: Creative Commons Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)

********************************************************************************
Webkarten mit QGIS Server und QGIS Webclient
********************************************************************************

WMS mit QGIS Server
================================================================================

#. Öffnen sie einen Webbrowser (z.B. Firefox)

#. Geben sie in der Adresszeile folgende URL ein http://localhost/cgi-bin/qgis_mapserv.fcgi?map=/home/$USER/QGIS-NaturalEarth-Example.qgs&SERVICE=WMS&REQUEST=GetCapabilities. Der Server Antwortet mit einem Capabilities Dokument, in dem u.a. Informationen zum Service und den verfügbaren Ebenen enthalten sind. Das QGIS Projekt, welches publiziert wird, muss als Parameter mitgegeben werden.

#. Nun fragen wir einen Kartenabschnitt an: http://localhost/cgi-bin/qgis_mapserv.fcgi?map=/home/$USER/QGIS-NaturalEarth-Example.qgs&SERVICE=WMS&REQUEST=GetMap&WIDTH=300&HEIGHT=300&BBOX=30,0,50,20&FORMAT=image/png&LAYERS=HYP_50M_SR_W&STYLES=default. Modifizieren sie die Parameter und schauen sie, wie sich die Karte verändert.

#. Für Informationen zu den Elementen in der Karte gibt es die GetFeatureInfo Anfrage: http://localhost/cgi-bin/qgis_mapserv.fcgi?map=/home/$USER/QGIS-NaturalEarth-Example.qgs&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetFeatureInfo&LAYERS=&QUERY_LAYERS=10m_populated_places_simple&STYLES=&BBOX=3.442999,43.068871,8.964614,49.504661&FEATURE_COUNT=10&HEIGHT=528&WIDTH=453&FORMAT=image/jpeg&INFO_FORMAT=text/xml&SRS=EPSG:4326&X=332&Y=213

#. Um diese Informationen nicht immer von Hand eingeben zu müssen, benutzen wir nun einen komfortablen WMS Client. Starten sie QGIS.
 
#. Wählen sie :menuselection:`Layer --> WMS Layer hinzufügen...` vom Menü.

#. Drücken sie auf 'Neu' und geben sie die WMS Adresse ein: http://localhost/cgi-bin/qgis_mapserv.fcgi?map=/home/$USER/QGIS-NaturalEarth-Example.qgs& . Kreuzen sie die Optionen 'Gemeldete GetMap-URI aus Diensteigenschaften ignorieren' und 'Gemeldete GetFeatureInfo-URI ignorieren an.

   .. image:: ../images/wms_connection.png
    :scale: 70%

#. Drücken sie auf 'Verbinden'. Eine Liste mit den verfügbaren Ebenen erscheint.

   .. image:: ../images/wms_client.png
    :scale: 70%

#. Wählen sie Ebenen aus und drücken sie auf 'Hinzufügen'. Der WMS Dienst ist nun als Ebene in QGIS eingebunden.

QGIS Webclient
=================================================================================

#. Öffnen sie einen Webbrowser (z.B. Firefox)

#. Für die Webkarte geben sie in der Adresszeile folgende URL ein: http://$USER.localhost/qgis-web-client/site/qgiswebclient.html?map=/home/geo01/QGIS-NaturalEarth-Example.qgs&format=image/png&visibleLayers=HYP_50M_SR_W

   .. image:: ../images/qgis_webclient.png
    :scale: 70%

Die Webkarte aufpeppen
=================================================================================

#. Starten sie QGIS und öffnen sie das Projekt 'QGIS-NaturalEarth-Example.qgs'.

#. Öffnen sie den Projekteigenschaftendialog :menuselection:`Einstellungen --> Projekteinstellungen...` und gehen sie zum Reiter 'OWS Server'.

#. Füllen sie ihre Kontaktangaben ein.

#. Selektieren sie die Ebene '10m_populated_places_simple' und öffnen sie den Eigenschaftendialog (:menuselection:`Layer --> Eigenschaften...`), Tab 'Felder'

#. Füllen sie besser lesbare Attributnamen (Aliase) ein.

#. Erzeugen sie eine neue Spalte mit dem Namen 'tooltip' mit dem Feldrechner. Diese Spalte wird von QGIS client als tooltip angezeigt.

#. Speichern sie das Projekt und laden sie die Webkarte im Browser neu ( Ctrl + F5 )

QGIS Cloud
=================================================================================

#. Starten sie das QGIS Cloud plugin ( :menuselection:`Erweiterungen --> Cloud --> Cloud settings` ).

Suche und Selektion 
=================================================================================

#. Im folgenden modifizieren wir die Datei /home/$USER/www/qgiswebclient/js/Globaloptions.js. Machen sie vorher eine Sicherheitskopie.