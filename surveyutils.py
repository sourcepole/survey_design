from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *

def fillLayerComboBox( comboBox,  geometryType,  noneEntry ):
        comboBox.clear()
        if noneEntry == True:
            comboBox.addItem( comboBox.tr( 'None' ) )

        mapLayers = QgsMapLayerRegistry.instance().mapLayers()
        for id in mapLayers:
            currentLayer = mapLayers[id]
            if currentLayer.type() != QgsMapLayer.VectorLayer:
                continue

            if currentLayer.geometryType() == geometryType:
                comboBox.addItem( currentLayer.name(), currentLayer.id() )
                
def fillAttributeComboBox( comboBox,  vectorLayer ):
    comboBox.clear()
    if not vectorLayer is None:
        if not vectorLayer.type() == QgsMapLayer.VectorLayer:
            return

        fieldList = vectorLayer.pendingFields().toList()
        for field in fieldList:
            comboBox.addItem( field.name() )
            
def writePointShapeAsGPX( shapePath,  nameAttribute,  outputFileName ):
    #open shape layer
    layer = QgsVectorLayer( shapePath,  "gpx",  "ogr" )
    if not layer.isValid() or layer.geometryType() != QGis.Point:
        return
        
    #open output file
    outputFile = QFile( outputFileName )
    if not outputFile.open( QIODevice.WriteOnly ):
        return
    
    #create xml in memory
    gpxDoc = QDomDocument()
    gpxElem = gpxDoc.createElementNS( "http://www.topografix.com/GPX/1/1", "gpx" )
    gpxDoc.appendChild( gpxElem )
    
    #all points have to be transformed to wgs84
    coordTransform = QgsCoordinateTransform( layer.crs(),  QgsCoordinateReferenceSystem( 'EPSG:4326' ) )
    
    #iterate through the vector layer
    iter = layer.getFeatures()
    for feature in iter:
        waypointElem = gpxDoc.createElementNS(  "http://www.topografix.com/GPX/1/1",  "wpt" )
        geom = feature.geometry()
        geom.transform( coordTransform )
        pointGeom = geom.asPoint()
        waypointElem.setAttribute( "lon",  str( pointGeom.x() ) )
        waypointElem.setAttribute( "lat",  str( pointGeom.y() ) )
        
        nameElem = gpxDoc.createElementNS( "http://www.topografix.com/GPX/1/1",  "name" )
        nameText = gpxDoc.createTextNode( str( feature.attribute( nameAttribute ) ) )
        nameElem.appendChild( nameText )
        waypointElem.appendChild( nameElem )
        
        gpxElem.appendChild( waypointElem )
        
    #save gpx document
    outStream = QTextStream( outputFile )
    gpxDoc.save( outStream,  2 )
    
