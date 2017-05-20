from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.analysis import *
from qgis.core import *
from qgis.gui import *
from ui_pointsurveydialogbase import Ui_PointSurveyDialogBase
from surveyutils import fillLayerComboBox
from surveyutils import fillAttributeComboBox
from surveyutils import writePointShapeAsGPX

class PointSurveyDialog( QDialog,  Ui_PointSurveyDialogBase ):
    def __init__( self,  parent,  iface ):
        QDialog.__init__( self, parent )
        self.iface = iface
        self.setupUi(self)
        
        fillLayerComboBox( self.mSurveyAreaLayerComboBox,  QGis.Polygon,  True )
        fillLayerComboBox( self.mStrataLayerComboBox,  QGis.Polygon,  False )
        self.strataLayerComboBoxChanged()
        
        QObject.connect( self.mStrataLayerComboBox,  SIGNAL('currentIndexChanged (int)'),  self.strataLayerComboBoxChanged )
        QObject.connect( self.mCreateSampleButton,  SIGNAL( 'clicked()' ),  self.createSample )
    
    def strataLayerComboBoxChanged(self):
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        if comboIndex is None:
            return
        layerId = self.mStrataLayerComboBox.itemData( comboIndex )
        layer = QgsMapLayerRegistry.instance().mapLayer( layerId )
        if layer is None:
            return
            
        fillAttributeComboBox( self.mMinimumDistanceAttributeComboBox,  layer )
        fillAttributeComboBox( self.mNSamplePointsComboBox,  layer )
        
    def createSample( self ):        
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        strataLayerId = self.mStrataLayerComboBox.itemData( comboIndex )
        strataLayer = QgsMapLayerRegistry.instance().mapLayer( strataLayerId )
        if strataLayer is None:
            return
            
        minDistanceAttribute = self.mMinimumDistanceAttributeComboBox.currentText()
        nSamplePointsAttribute = self.mNSamplePointsComboBox.currentText()
        
        if len( minDistanceAttribute ) == 0 or len( nSamplePointsAttribute ) == 0:
            return

        s = QSettings()
        saveDir = s.value( '/SurveyPlugin/SaveDir','')

        outputShape = QFileDialog.getSaveFileName( self, QCoreApplication.translate( 'SurveyDesignDialog', 'Select output shape file' ), saveDir, QCoreApplication.translate( 'SurveyDesignDialog', 'Shapefiles (*.shp)' ) )
        print ( outputShape )
        if not outputShape:
            return

        p = QgsPointSample (  strataLayer, outputShape, nSamplePointsAttribute, minDistanceAttribute )
        p.createRandomPoints( None )

        s.setValue( '/SurveyPlugin/SaveDir', QFileInfo( outputShape ).absolutePath() )
        self.iface.addVectorLayer( outputShape, 'sample', 'ogr' )
        
        gpxFileInfo = QFileInfo( outputShape )
        gpxFileName = gpxFileInfo.path() + '/' + gpxFileInfo.baseName() + '.gpx'
        writePointShapeAsGPX( outputShape, 'id',   gpxFileName )
