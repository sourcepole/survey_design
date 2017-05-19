from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from pointsurveydialog import PointSurveyDialog
from transectsurveydialog import TransectSurveyDialog

class SurveyDesignPlugin:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        menuBar = self.iface.mainWindow().menuBar()
        surveyDesignMenu = QMenu( QCoreApplication.translate("SurveyDesignPlugin","Survey") ,  menuBar)

        self.actionTransectSurvey = QAction( 'Transect survey',  self.iface.mainWindow() )
        QObject.connect( self.actionTransectSurvey, SIGNAL("triggered()"), self.transectSurvey )
        
        self.actionPointSurvey = QAction( 'Point survey',  self.iface.mainWindow() )
        QObject.connect( self.actionPointSurvey,  SIGNAL("triggered()"),  self.pointSurvey )

        surveyDesignMenu.addAction( self.actionTransectSurvey )
        surveyDesignMenu.addAction( self.actionPointSurvey )
        self.surveyDesignAction = menuBar.addMenu( surveyDesignMenu )

    def unload(self):
        self.iface.mainWindow().menuBar().removeAction( self.surveyDesignAction )

    def transectSurvey(self):
        self.transectSurveyDialog = TransectSurveyDialog( self.iface.mainWindow(),  self.iface )
        self.transectSurveyDialog.show()
        
    def pointSurvey(self):
        self.pointSurveyDialog = PointSurveyDialog( self.iface.mainWindow(),  self.iface )
        self.pointSurveyDialog.show()
