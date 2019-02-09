from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
import csv
from xlsxwriter import *

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
            
def writeXLSXRow( worksheet, rowIndex, contentList ):
    for index in range( len(contentList) ):
        worksheet.write( rowIndex, index, contentList[index] )

def writePointShapeAsGPX( shapePath,  nameAttribute,  commentAttribute,  outputFileName ):
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

        encodedNameAttribute = feature.attribute( nameAttribute )
        if isinstance( encodedNameAttribute, unicode ):
            encodedNameAttribute = encodedNameAttribute.encode( "UTF-8" )


        nameElem = gpxDoc.createElementNS( "http://www.topografix.com/GPX/1/1",  "name" )
        nameText = gpxDoc.createTextNode( str( encodedNameAttribute ) )
        nameElem.appendChild( nameText )
        waypointElem.appendChild( nameElem )

        if len( commentAttribute ) > 0:
            commentElem = gpxDoc.createElementNS( "http://www.topografix.com/GPX/1/1",  "cmt" )
            commentText = gpxDoc.createTextNode( str( feature.attribute( commentAttribute ) ) )
            commentElem.appendChild( commentText )
            waypointElem.appendChild( commentElem )

        gpxElem.appendChild( waypointElem )

    #save gpx document
    outStream = QTextStream( outputFile )
    gpxDoc.save( outStream,  2 )

def writeStratumCSV( outputDirectory,  stratumLayer,  stratumIdAttribute,  surveyId ):
    outputFilePath = outputDirectory + "/" + "Stratum.csv"
    csvWriter = csv.writer( open( outputFilePath,  "wb" ) )
    #write header
    csvWriter.writerow( ["survey","stratum","area_m2","year","description"] )

    iter = stratumLayer.getFeatures()
    for feature in iter:
        geomArea = 0
        geom = feature.geometry()
        if not geom is None:
            geomArea = geom.area()
        stratumId = feature.attribute( stratumIdAttribute )

        if isinstance( stratumId, unicode ):
            stratumId = stratumId.encode( "utf-8" )

        encodedSurveyId = surveyId
        if isinstance( surveyId, unicode ):
            encodedSurveyId = encodedSurveyId.encode( "utf-8" )

        csvWriter.writerow( [encodedSurveyId,  stratumId,  geomArea,  QDate.currentDate().year(), ""] )
        
def writeStratumXLSX( workbook, stratumLayer, stratumIdAttribute, surveyId ):
    stratumWorksheet = workbook.add_worksheet( 'Stratum' )
    #write header
    writeXLSXRow( stratumWorksheet, 0, ["survey","stratum","area_m2","year","description"] )
    
    currentRow = 1
    iter = stratumLayer.getFeatures()
    for feature in iter:
        geomArea = 0
        geom = feature.geometry()
        if not geom is None:
            geomArea = geom.area()
        
        stratumId = feature.attribute( stratumIdAttribute )
        writeXLSXRow( stratumWorksheet, currentRow, [surveyId, stratumId, geomArea, QDate.currentDate().year()] )
        currentRow += 1

def writeStratumBoundaryCSV( outputDirectory,  stratumLayer,  stratumIdAttribute,  surveyId ):
    if stratumLayer is None:
        return

    outputFilePath = outputDirectory + "/" + "StratumBoundaries.csv"
    csvWriter = csv.writer( open( outputFilePath,  "wb" ) )
    #write header
    csvWriter.writerow( ["long","lat","stratum","survey"] )

    #all points have to be transformed to wgs84
    coordTransform = QgsCoordinateTransform( stratumLayer.crs(),  QgsCoordinateReferenceSystem( 'EPSG:4326' ) )

    iter = stratumLayer.getFeatures()
    for feature in iter:
        stratumId = feature.attribute( stratumIdAttribute )
        if isinstance( stratumId, unicode ):
            stratumId = stratumId.encode( "utf-8" )

        encodedSurveyId = surveyId
        if isinstance( surveyId, unicode ):
            encodedSurveyId = encodedSurveyId.encode( "utf-8" )

        geom = feature.geometry()
        geom.transform( coordTransform )

        if not geom is None:
            featureCoords = geom.geometry().coordinateSequence()
            for part in featureCoords:
                for ring in part:
                    for vertex in ring:
                        csvWriter.writerow( [vertex.x(),  vertex.y(),  stratumId, encodedSurveyId] )
            pass
        
def writeStratumBoundaryXLSX( workbook, stratumLayer,  stratumIdAttribute,  surveyId ):
    if stratumLayer is None:
        return
    
    worksheet = workbook.add_worksheet( 'StratumBoundaries' )
    
    #header
    writeXLSXRow( worksheet, 0, ["long","lat","stratum","survey"] )
    
    #all points have to be transformed to wgs84
    coordTransform = QgsCoordinateTransform( stratumLayer.crs(),  QgsCoordinateReferenceSystem( 'EPSG:4326' ) )
    
    iter = stratumLayer.getFeatures()
    for feature in iter:
        stratumId = feature.attribute( stratumIdAttribute )
        
        geom = feature.geometry()
        geom.transform( coordTransform )
        
        currentRow = 1

        if not geom is None:
           featureCoords = geom.geometry().coordinateSequence()
           for part in featureCoords:
               for ring in part:
                   for vertex in ring:
                       writeXLSXRow( worksheet, currentRow, [vertex.x(),  vertex.y(),  stratumId, surveyId])
                       currentRow += 1

def writeStationCSV( outputDirectory,  transectLayer,  stratumIdAttribute,  transectIdAttribute,  surveyId ):
    if transectLayer is None:
        return

    #all points have to be transformed to wgs84
    coordTransform = QgsCoordinateTransform( transectLayer.crs(),  QgsCoordinateReferenceSystem( 'EPSG:4326' ) )

    outputFilePath = outputDirectory + "/" + "Station.csv"
    csvWriter = csv.writer( open( outputFilePath,  "wb" ) )

    csvWriter.writerow( ["survey","stratum","transect","quadrat","area_m2","depth","start_lat","start_long","end_lat","end_long","in_out_bed","comments"] )

    encodedSurveyId = surveyId
    if isinstance( surveyId, unicode ):
        encodedSurveyId = encodedSurveyId.encode( "utf-8" )

    iter = transectLayer.getFeatures()
    for feature in iter:
        geom = feature.geometry()
        if geom is None:
            continue

        encodedStratumId = feature.attribute( stratumIdAttribute )
        if isinstance( encodedStratumId, unicode ):
            encodedStratumId = encodedStratumId.encode( "utf-8" )

        encodedTransectId = feature.attribute( transectIdAttribute )
        if isinstance( encodedTransectId, unicode ):
            encodedTransectId = encodedTransectId.encode( "utf-8" )

        if geom.type() == QGis.Line:
            startPoint = geom.geometry().startPoint()
            startPoint.transform( coordTransform )
            endPoint = geom.geometry().endPoint()
            endPoint.transform( coordTransform )
            csvWriter.writerow([ str( encodedSurveyId ),  str( encodedStratumId ),  str( encodedTransectId ),  "", "",  "",  startPoint.y(),  startPoint.x(),  endPoint.y(), endPoint.x(),  "", "" ])
        elif geom.type() == QGis.Point:
            point = geom.geometry()
            point.transform( coordTransform )
            csvWriter.writerow([ str( encodedSurveyId ),  str( encodedStratumId ),  str( encodedTransectId ),  "", "",  "",  point.y(),  point.x(),  '',  '',  '', '' ] )
            
def writeStationXLSX( workbook, transectLayer,  stratumIdAttribute,  transectIdAttribute,  surveyId ):
    
    if transectLayer is None:
        return
    
    #all points have to be transformed to wgs84
    coordTransform = QgsCoordinateTransform( transectLayer.crs(),  QgsCoordinateReferenceSystem( 'EPSG:4326' ) )
    
    worksheet = workbook.add_worksheet( 'Station' )
    
    #header
    writeXLSXRow( worksheet, 0, ["survey","stratum","transect","quadrat","area_m2","depth","start_lat","start_long","end_lat","end_long","in_out_bed","comments"] )
    
    currentRow = 1
    
    iter = transectLayer.getFeatures()
    for feature in iter:
        geom = feature.geometry()
        if geom is None:
            continue
    
        stratumId = feature.attribute( stratumIdAttribute )
        transectId = feature.attribute( transectIdAttribute )
        
        if geom.type() == QGis.Line:
            coordSeq = geom.geometry().coordinateSequence()
            startPoint = coordSeq[0][0][0]
            startPoint.transform( coordTransform )
            endPoint = coordSeq[-1][-1][-1]
            endPoint.transform( coordTransform )
            writeXLSXRow( worksheet, currentRow, [ surveyId, stratumId, transectId, '','','', startPoint.y(),  startPoint.x(),  endPoint.y(), endPoint.x(),  "", "" ] )
        
        elif geom.type() == QGis.Point:
            point = geom.geometry()
            point.transform( coordTransform )
            writeXLSXRow( worksheet, currentRow, [ surveyId, stratumId, transectId, '','','', point.y(),  point.x(),  '',  '',  '', '' ] )
        
        currentRow += 1

def writeSurveyCSV( outputDirectory,  survey,  projectCode,  date_s,  date_f,  contactName,  area,  mainspp,  comments ):
    outputFilePath = outputDirectory + "/" + "Survey.csv"
    csvWriter = csv.writer( open( outputFilePath,  "wb" ) )
    csvWriter.writerow( ["survey","proj_code","date_s","date_f","contact_name","areas","mainspp","comments"] )
    csvWriter.writerow( [survey.encode( "utf-8" ),  projectCode.encode( "utf-8" ),  date_s,  date_f,  contactName.encode( "utf-8" ),  area.encode( "utf-8" ),  mainspp.encode( "utf-8" ),  comments.encode( "utf-8" )] )
    
def writeSurveyXLSX( workbook, survey,  projectCode,  date_s,  date_f,  contactName,  area,  mainspp,  comments ):
    worksheet = workbook.add_worksheet( 'Survey' )
    writeXLSXRow( worksheet, 0, ["survey","proj_code","date_s","date_f","contact_name","areas","mainspp","comments"] )
    writeXLSXRow( worksheet, 1, [ survey, projectCode, date_s,  date_f,  contactName, area, mainspp, comments] )

def writeCatchCSV( outputDirectory ):
    outputFilePath = outputDirectory + "/Catch.csv"
    csvWriter = csv.writer( open( outputFilePath,  "wb" ) )
    csvWriter.writerow( ["survey","stratum","transect","quadrat","replicate","species","no_fish","lf_taken","samp_meth","meas_meth", "weight","wt_meth", "samp_wt"] )
    
def writeCatchXLSX( workbook ):
    worksheet = workbook.add_worksheet( 'Catch' )
    writeXLSXRow( worksheet, 0, ["survey","stratum","transect","quadrat","replicate","species","no_fish","lf_taken","samp_meth","meas_meth", "weight","wt_meth", "samp_wt"] )

def writeLengthCSV( outputDirectory ):
    outputFilePath = outputDirectory + "/Length.csv"
    csvWriter = csv.writer( open( outputFilePath,  "wb" ) )
    csvWriter.writerow( ["survey","stratum","transect","quadrat","replicate","species","lgth","percent_samp","no_a"] )
    
def writeLengthXLSX( workbook ):
    worksheet = workbook.add_worksheet( 'Length' )
    writeXLSXRow( worksheet, 0, ["survey","stratum","transect","quadrat","replicate","species","lgth","percent_samp","no_a"] )
