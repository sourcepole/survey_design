from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.analysis import *
from qgis.core import *
from qgis.gui import *
from ui_transectsurveydialogbase import Ui_TransectSurveyDialogBase
from surveyutils import fillLayerComboBox
from surveyutils import fillAttributeComboBox
from surveyutils import writePointShapeAsGPX
from surveyutils import writeStratumCSV
from surveyutils import writeStratumBoundaryCSV
from surveyutils import writeStationTransectCSV

class TransectSurveyDialog( QDialog,  Ui_TransectSurveyDialogBase ):
    def __init__(self,  parent,  iface ):
        QDialog.__init__( self,  parent )
        self.iface = iface
        self.setupUi(self)
        
        fillLayerComboBox( self.mSurveyAreaLayerComboBox,  QGis.Polygon,  True )
        fillLayerComboBox( self.mStrataLayerComboBox,  QGis.Polygon,  False )
        fillLayerComboBox( self.mSurveyBaselineLayerComboBox,  QGis.Line,  False )
        
        self.strataLayerComboBoxChanged()
        
        QObject.connect( self.mStrataLayerComboBox,  SIGNAL('currentIndexChanged (int)'),  self.strataLayerComboBoxChanged )
        QObject.connect( self.mCreateSampleButton,  SIGNAL( 'clicked()' ),  self.createSample )
        QObject.connect( self.mExportCsvButton,  SIGNAL( 'clicked()'),  self.exportCSV )
        
    def strataLayerComboBoxChanged( self ):
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        if comboIndex is None:
            return
        layerId = self.mStrataLayerComboBox.itemData( comboIndex )
        layer = QgsMapLayerRegistry.instance().mapLayer( layerId )
        if layer is None:
            return
        
        fillAttributeComboBox( self.mMinimumDistanceAttributeComboBox,  layer )
        fillAttributeComboBox( self.mNSamplePointsComboBox,  layer )
        fillAttributeComboBox( self.mStrataIdAttributeComboBox,  layer )
        
    def createSample( self ):
        s = QSettings()
        saveDir = s.value( '/SurveyPlugin/SaveDir','')

        outputPointShape = QFileDialog.getSaveFileName( self, QCoreApplication.translate( 'SurveyDesignDialog', 'Select output point shape file' ), saveDir, QCoreApplication.translate( 'SurveyDesignDialog', 'Shapefiles (*.shp)' ) )
        if not outputPointShape:
            return
        else:
            saveDir = QFileInfo( outputPointShape ).absolutePath()

        outputLineShape = QFileDialog.getSaveFileName( self, QCoreApplication.translate( 'SurveyDesignDialog', 'Select output line shape file' ), saveDir, QCoreApplication.translate( 'SurveyDesignDialog', 'Shapefiles (*.shp)' ) )
        if not outputLineShape:
            return
        else:
            saveDir = QFileInfo( outputLineShape ).absolutePath()

        usedBaselineShape = QFileDialog.getSaveFileName( self, QCoreApplication.translate( 'SurveyDesignDialog', 'Select output baseline file' ), saveDir, QCoreApplication.translate( 'SurveyDesignDialog', 'Shapefiles (*.shp)' ) )
        if not usedBaselineShape:
            return
        
        #strata map layer
        strataMapLayer = self.stratumLayer()
        if strataMapLayer is None:
            return

        strataMinDistance = self.mMinimumDistanceAttributeComboBox.currentText()
        strataNSamplePoints = self.mNSamplePointsComboBox.currentText()
        strataId = self.mStrataIdAttributeComboBox.currentText()
            
        #baseline map layer
        comboIndex = self.mSurveyBaselineLayerComboBox.currentIndex()
        baselineLayerId = self.mSurveyBaselineLayerComboBox.itemData( comboIndex )
        baselineMapLayer = QgsMapLayerRegistry.instance().mapLayer( baselineLayerId )

        #assume everything is in stratum units
        minDistanceUnits = QgsTransectSample.StrataUnits
        
        transectSample = QgsTransectSample(  strataMapLayer, strataId , strataMinDistance, strataNSamplePoints, minDistanceUnits, baselineMapLayer, True,
        '', outputPointShape, outputLineShape,  usedBaselineShape,  0.0,  -1.0,  -1.0 )
        pd = QProgressDialog(  'Calculating transects...', 'Abort',  0,  0,  self )
        pd.setWindowTitle( 'Transect generation' )
        pd.show();
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        transectSample.createSample( pd )
        
        gpxFileInfo = QFileInfo( outputPointShape )
        gpxFileName = gpxFileInfo.path() + '/' + gpxFileInfo.baseName() + '.gpx'
        writePointShapeAsGPX( outputPointShape, 'station_co',   gpxFileName )
        
        #write station  csv file
        transectLayer = QgsVectorLayer( outputLineShape,  "transect",  "ogr" )
        csvDir = QFileInfo(  outputLineShape ).absolutePath() 
        writeStationTransectCSV( csvDir,  transectLayer, "stratum_id",  "station_id",  "test_survey" )
        
        QApplication.restoreOverrideCursor()
        
    def exportCSV(self):
        fileDialog = QFileDialog(  self,  QCoreApplication.translate( 'SurveyDesignDialog', 'Select output directory for csv files' )  )
        fileDialog.setFileMode( QFileDialog.Directory )
        fileDialog.setOption( QFileDialog.ShowDirsOnly )
        if fileDialog.exec_() == QDialog.Accepted:
            writeStratumCSV( fileDialog.selectedFiles()[0], self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  "test_survey" )
            writeStratumBoundaryCSV( fileDialog.selectedFiles()[0], self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  "test_survey" )
        
    def stratumLayer(self):
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        strataLayerId = self.mStrataLayerComboBox.itemData( comboIndex )
        strataMapLayer = QgsMapLayerRegistry.instance().mapLayer( strataLayerId )
        return strataMapLayer

