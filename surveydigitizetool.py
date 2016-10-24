from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class SurveyDigitizeTool( QgsMapTool ):

    def __init__( self,  digitizeLayer,  mapCanvas,  snapLayerId, snapTolerancePixels ):
        QgsMapTool.__init__(self,  mapCanvas )
        self.mLayerCoordList = []
        self.mMapCanvas = mapCanvas
        self.mDigitizeLayerId = digitizeLayer
        self.mEditLayer = QgsMapLayerRegistry.instance().mapLayer(  self.mDigitizeLayerId )
        self.mRubberBand = QgsRubberBand( mapCanvas,  self.mEditLayer.geometryType() )
        self.mRubberBand.setColor( QColor( 255,  0,  0 ) )
        self.mRubberBand.setWidth(  2 )
        

        #Configure QgsSnapper with 20 pixel to given snap layer
        snapLayer = QgsSnapper.SnapLayer()
        snapLayer.mTolerance = 20
        snapLayer.mUnitType = QgsTolerance.Pixels
        snapLayer.mSnapTo = QgsSnapper.SnapToVertexAndSegment
        snapLayer.mLayer = QgsMapLayerRegistry.instance().mapLayer(  snapLayerId )
        snapLayerList = []
        snapLayerList.append( snapLayer )
        self.mSnapper = QgsSnapper( mapCanvas.mapRenderer() )
        self.mSnapper.setSnapLayers( snapLayerList )
        self.mSnapper.setSnapMode( QgsSnapper.SnapWithOneResult )
        
        #Tracing to snap layer
        self.mTracer = QgsTracer()
        traceLayerList = []
        traceLayerList.append( QgsMapLayerRegistry.instance().mapLayer( snapLayerId ) )
        self.mTracer.setLayers( traceLayerList )
        self.mTracer.setDestinationCrs( self.mMapCanvas.mapSettings().destinationCrs() )
        
        self.cursor = QCursor(QPixmap(["16 16 3 1",
                                  "      c None",
                                  ".     c #000000",
                                  "+     c #FFFFFF",
                                  "                ",
                                  "       +.+      ",
                                  "      ++.++     ",
                                  "     +.....+    ",
                                  "    +.     .+   ",
                                  "   +.   .   .+  ",
                                  "  +.    .    .+ ",
                                  " ++.    .    .++",
                                  " ... ...+... ...",
                                  " ++.    .    .++",
                                  "  +.    .    .+ ",
                                  "   +.   .   .+  ",
                                  "   ++.     .+   ",
                                  "    ++.....+    ",
                                  "      ++.++     ",
                                  "       +.+      "]))

    def activate( self ):
        QApplication.setOverrideCursor(self.cursor)
        if not self.mEditLayer is None:
            self.mEditLayer.startEditing()

    def deactivate( self ):
        QApplication.restoreOverrideCursor()

        if not self.mEditLayer is None:
            self.mEditLayer.commitChanges()

        QgsMapTool.deactivate( self )

    def canvasMoveEvent(self,  event ):
        currentPoint = self.snappedPoint( event.pos() )
        
        #tracing?
        rubberBandPointCount = self.mRubberBand.partSize( 0 )
        if rubberBandPointCount >= 2:
           lastPoint = self.mRubberBand.getPoint( 0,  rubberBandPointCount - 2 ) 
           if( self.mTracer.isPointSnapped( lastPoint ) and self.mTracer.isPointSnapped( currentPoint ) ):
               tracedPoints = self.mTracer.findShortestPath(  lastPoint,  currentPoint )[0]
               
               if len( tracedPoints ) >= 3:
                   #remove the last point in rubber band and add all the tracing points [1:size - 1]
                   self.mRubberBand.removeLastPoint( 0 )
                   for i in range ( 1,  len( tracedPoints ) - 1 ):
                       self.mRubberBand.addPoint( tracedPoints[i],  False )
                   self.mRubberBand.update()
                   self.mRubberBand.addPoint( tracedPoints[len(tracedPoints)-1]  )
                   
        self.mRubberBand.movePoint( currentPoint )

    def canvasReleaseEvent(self,  event ):
        currentPoint = self.snappedPoint( event.pos() )
        
        #tracing?
        if len( self.mLayerCoordList ) > 0:
            lastMapPoint = self.toMapCoordinates( self.mEditLayer,  self.mLayerCoordList[-1] )
            if self.mTracer.isPointSnapped( currentPoint ) and self.mTracer.isPointSnapped( lastMapPoint ):
                tracedPoints = self.mTracer.findShortestPath( lastMapPoint,  currentPoint )[0]
                if len( tracedPoints ) > 2:
                    for i in range ( 1,  len( tracedPoints ) - 1 ):
                        self.mLayerCoordList.append( self.toLayerCoordinates( self.mEditLayer,  tracedPoints[i] ) )
                
        self.mLayerCoordList.append(  self.toLayerCoordinates(  self.mEditLayer,  currentPoint ) )
        self.mRubberBand.addPoint( currentPoint )
        
        if event.button() == Qt.RightButton:
            if self.mEditLayer is None:
                return
                
            #add default attributes
            fieldMap = self.mEditLayer.pendingFields()
            feature = QgsFeature()
            feature.initAttributes( fieldMap.size() )
            
            for i in range(0, fieldMap.size()):
                    feature.setAttribute( i,  self.mEditLayer.dataProvider().defaultValue( i ) )

            feature.setValid( True )
            attDialog = QgsAttributeDialog(  self.mEditLayer,  feature,  False )
            
            if attDialog.exec_() == QDialog.Accepted:
                feature.setGeometry( self.geometryFromPointList( self.mLayerCoordList ) )
                self.mEditLayer.beginEditCommand('Add feature')
                self.mEditLayer.addFeature( feature )
                self.mEditLayer.endEditCommand()
            self.mRubberBand.reset(  self.mEditLayer.geometryType() == QGis.Polygon )
            del self.mLayerCoordList[:]
            self.mMapCanvas.refresh()


    def snappedPoint(self,  pos ):
        excludeList = []
        result = self.mSnapper.snapPoint(  pos,  excludeList )
        if result[0] == 0 and not len( result[1] ) < 1:
            resultPt = result[1][0].snappedVertex
            return QgsPoint( resultPt.x(),  resultPt.y() )
        else:
            return self.toMapCoordinates( pos )

    def geometryFromPointList(self,  pointList):
        if self.mEditLayer.geometryType() == QGis.Polygon:
            return QgsGeometry.fromPolygon(  [pointList] )
        else:
            return QgsGeometry.fromPolyline( pointList )

    def isEditTool(self):
        return True
