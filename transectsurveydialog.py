from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.analysis import *
from qgis.core import *
from qgis.gui import *
from ui_transectsurveydialogbase import Ui_TransectSurveyDialogBase
from surveyproperties import SurveyProperties
from surveyutils import *

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
        
        #open line shape and create a dict station_id / bearing
        #first find out 'station_co' attribute name
        transectLineLayer = QgsVectorLayer( outputLineShape,  'transectLineLayer',  'ogr' )
        fields = transectLineLayer.pendingFields()
        stationCodeFieldName = "station_co"
        for field in fields:
            if field.name().startswith( "station_co" ):
                stationCodeFieldName = field.name()
                break
        
        bearingDict = {}
        
        transectLineIt = transectLineLayer.getFeatures()
        for transectLineFeature in transectLineIt:
            station_co = transectLineFeature.attribute( stationCodeFieldName )
            bearing = transectLineFeature.attribute( 'bearing' )
            bearingDict[station_co] = bearing
        
        #write bearing into output point shape
        transectPointLayer = QgsVectorLayer( outputPointShape,  'transectPointLayer',  'ogr' )
        transectPointLayer.startEditing()
        transectPointLayer.addAttribute( QgsField( 'bearing',  QVariant.Double,  "Double" ) )
        bearingIndex = transectPointLayer.fieldNameIndex( 'bearing' )
        transectPointIt = transectPointLayer.getFeatures()
        for transectPointFeature in transectPointIt:
            station_co = transectPointFeature.attribute( stationCodeFieldName )
            transectPointLayer.changeAttributeValue( transectPointFeature.id(),  bearingIndex,  bearingDict[ station_co] )
        transectPointLayer.commitChanges()
        
        #write gpx file
        gpxFileInfo = QFileInfo( outputPointShape )
        gpxFileName = gpxFileInfo.path() + '/' + gpxFileInfo.baseName() + '.gpx'
        writePointShapeAsGPX( outputPointShape,  stationCodeFieldName, 'bearing',   gpxFileName )
        
        transectLayer = QgsVectorLayer( outputLineShape,  "transect",  "ogr" )
        
        #write XLSX output
        workbook = Workbook( saveDir + '/survey.xlsx')
        writeSurveyXLSX( workbook, surveyProps.survey(),  surveyProps.projectCode(), surveyProps.date_s() , surveyProps.date_f(),  surveyProps.contactName(),  surveyProps.areas(), surveyProps.mainspp(),  surveyProps.comments() )
        writeStationXLSX( workbook, transectLayer, "stratum_id",  "station_id",  surveyProps.survey() )
        writeStratumXLSX( workbook, self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  surveyProps.survey() )
        writeStratumBoundaryXLSX( workbook, self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  surveyProps.survey() )
        writeCatchXLSX( workbook )
        writeLengthXLSX( workbook )
        workbook.close()
        
        #write csv files
        #Survey.csv
        writeSurveyCSV( fileDialog.selectedFiles()[0],  surveyProps.survey(),  surveyProps.projectCode(), surveyProps.date_s() , surveyProps.date_f(),  surveyProps.contactName(),  surveyProps.areas(), surveyProps.mainspp(),  surveyProps.comments() )
        writeStationCSV( saveDir,  transectLayer, "stratum_id",  "station_id",  surveyProps.survey() )
        writeStratumCSV( fileDialog.selectedFiles()[0], self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  surveyProps.survey() )
        writeStratumBoundaryCSV( fileDialog.selectedFiles()[0], self.stratumLayer(), self.mStrataIdAttributeComboBox.currentText(),  surveyProps.survey() )
        writeCatchCSV( saveDir )
        writeLengthCSV( saveDir )
        
        self.iface.addVectorLayer( outputLineShape, 'transects', 'ogr' )
        self.iface.addVectorLayer( outputPointShape,  'transect_stations',  'ogr' )
        
        QApplication.restoreOverrideCursor()

    def stratumLayer(self):
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        strataLayerId = self.mStrataLayerComboBox.itemData( comboIndex )
        strataMapLayer = QgsMapLayerRegistry.instance().mapLayer( strataLayerId )
        return strataMapLayer

