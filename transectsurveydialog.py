from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.analysis import *
from qgis.core import *
from qgis.gui import *
from ui_transectsurveydialogbase import Ui_TransectSurveyDialogBase
from surveyproperties import SurveyProperties
from surveyutils import fillLayerComboBox
from surveyutils import fillAttributeComboBox
from surveyutils import writePointShapeAsGPX
from surveyutils import writeStratumCSV
from surveyutils import writeStratumBoundaryCSV
from surveyutils import writeStationCSV
from surveyutils import writeSurveyCSV

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
        surveyProps = SurveyProperties( self )
        if surveyProps.exec_() == QDialog.Rejected:
            return
        
        fileDialog = QFileDialog(  self,  QCoreApplication.translate( 'SurveyDesignDialog', 'Select output directory for result files' )  )
        fileDialog.setFileMode( QFileDialog.Directory )
        fileDialog.setOption( QFileDialog.ShowDirsOnly )
        if fileDialog.exec_() != QDialog.Accepted:
            return
            
        saveDir = fileDialog.selectedFiles()[0]

        outputPointShape = saveDir + '/transect_points.shp' 
        outputLineShape = saveDir + '/transect_lines.shp' 
        usedBaselineShape = saveDir + '/used_baselines.shp'
        
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
        '', outputPointShape, outputLineShape,  usedBaselineShape,  self.mMinimumTransectLengthSpinBox.value(),  -1.0,  -1.0 )
        pd = QProgressDialog(  'Calculating transects...', 'Abort',  0,  0,  self )
        pd.setWindowTitle( 'Transect generation' )
        pd.show();
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        transectSample.createSample( pd )
        
        gpxFileInfo = QFileInfo( outputPointShape )
        gpxFileName = gpxFileInfo.path() + '/' + gpxFileInfo.baseName() + '.gpx'
        writePointShapeAsGPX( outputPointShape, 'station_co',   gpxFileName )
        
        #write csv files
        #Survey.csv
        writeSurveyCSV( fileDialog.selectedFiles()[0],  surveyProps.survey(),  surveyProps.projectCode(), surveyProps.date_s() , surveyProps.date_f(),  surveyProps.contactName(),  surveyProps.areas(), surveyProps.mainspp(),  surveyProps.comments() )
        transectLayer = QgsVectorLayer( outputLineShape,  "transect",  "ogr" )
        writeStationCSV( saveDir,  transectLayer, "stratum_id",  "station_id",  surveyProps.survey() )
        writeStratumCSV( fileDialog.selectedFiles()[0], self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  surveyProps.survey() )
        writeStratumBoundaryCSV( fileDialog.selectedFiles()[0], self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  surveyProps.survey() )
        
        self.iface.addVectorLayer( outputLineShape, 'transects', 'ogr' )
        self.iface.addVectorLayer( outputPointShape,  'transect_stations',  'ogr' )
        
        QApplication.restoreOverrideCursor()

    def stratumLayer(self):
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        strataLayerId = self.mStrataLayerComboBox.itemData( comboIndex )
        strataMapLayer = QgsMapLayerRegistry.instance().mapLayer( strataLayerId )
        return strataMapLayer

