from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.analysis import *
from qgis.core import *
from qgis.gui import *
from ui_pointsurveydialogbase import Ui_PointSurveyDialogBase
from surveyproperties import SurveyProperties
from surveyutils import fillLayerComboBox
from surveyutils import fillAttributeComboBox
from surveyutils import writePointShapeAsGPX
from surveyutils import writeStratumCSV
from surveyutils import writeStratumBoundaryCSV
from surveyutils import writeSurveyCSV
from surveyutils import writeStationCSV
from surveyutils import writeCatchCSV
from surveyutils import writeLengthCSV

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
        fillAttributeComboBox( self.mStrataIdComboBox,  layer )
        
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
        
        comboIndex = self.mStrataLayerComboBox.currentIndex()
        strataLayerId = self.mStrataLayerComboBox.itemData( comboIndex )
        strataLayer = QgsMapLayerRegistry.instance().mapLayer( strataLayerId )
        if strataLayer is None:
            return
            
        minDistanceAttribute = self.mMinimumDistanceAttributeComboBox.currentText()
        nSamplePointsAttribute = self.mNSamplePointsComboBox.currentText()
        
        if len( minDistanceAttribute ) == 0 or len( nSamplePointsAttribute ) == 0:
            return

        outputShape =  saveDir + "/point_sample.shp"

        p = QgsPointSample (  strataLayer, outputShape, nSamplePointsAttribute, minDistanceAttribute )
        p.createRandomPoints( None )
        
        #Store strata feature id / textual id in a dict
        strataIdDict = {}
        strataLayerId = self.mStrataLayerComboBox.itemData( comboIndex )
        strataLayer = QgsMapLayerRegistry.instance().mapLayer( strataLayerId )
        if not strataLayer is None:
            strataIt = strataLayer.getFeatures()
            for stratum in strataIt:
                strataIdDict[stratum.id()] = stratum.attribute( self.mStrataIdComboBox.currentText() )
        
        #Add attribute station_co, e.g. A_2 usw.
        samplePointLayer = QgsVectorLayer( outputShape,  "samplePoint",  "ogr" )
        samplePointLayer.startEditing()
        samplePointLayer.addAttribute( QgsField( 'stratumid',  QVariant.String,  "String" ) )
        samplePointLayer.addAttribute( QgsField( 'station_co',  QVariant.String,  "String" )  )
        newId = samplePointLayer.fieldNameIndex( 'station_co' )
        newStratumId = samplePointLayer.fieldNameIndex( 'stratumid' )
        iter = samplePointLayer.getFeatures()
        for feature in iter:
            stratumId = str( strataIdDict[ feature.attribute( "stratum_id" ) ] )
            stationId = str( feature.attribute( "station_id" ) )
            samplePointLayer.changeAttributeValue( feature.id(),  newStratumId,  stratumId )
            samplePointLayer.changeAttributeValue( feature.id(), newId,  stratumId + '_' + stationId )
        samplePointLayer.commitChanges()

        gpxFileInfo = QFileInfo( outputShape )
        gpxFileName = gpxFileInfo.path() + '/' + gpxFileInfo.baseName() + '.gpx'
        writePointShapeAsGPX( outputShape, 'station_co', gpxFileName )
        
        #write csv files
        writeSurveyCSV( saveDir,  surveyProps.survey(),  surveyProps.projectCode(), surveyProps.date_s() , surveyProps.date_f(),  surveyProps.contactName(),  surveyProps.areas(), surveyProps.mainspp(),  surveyProps.comments() )
        writeStratumCSV( saveDir, strataLayer, self.mStrataIdComboBox.currentText(),  surveyProps.survey() )
        writeStratumBoundaryCSV( saveDir, strataLayer, self.mStrataIdComboBox.currentText(),  surveyProps.survey() )
        writeStationCSV( saveDir,  samplePointLayer, "stratumid",  "station_id",  surveyProps.survey() )
        writeCatchCSV( saveDir )
        writeLengthCSV( saveDir )
        
        self.iface.addVectorLayer( outputShape, 'point_sample', 'ogr' )
