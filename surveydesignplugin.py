from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from surveyinitdialog import SurveyInitDialog
from surveydesigndialog import SurveyDesignDialog
from surveyevaluation import SurveyEvaluation

class SurveyDesignPlugin:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        menuBar = self.iface.mainWindow().menuBar()
        surveyDesignMenu = QMenu( QCoreApplication.translate("SurveyDesignPlugin","Survey") ,  menuBar)

        isSurveyProject = self.projectContainsSurveyDesign()

        self.actionSurveyProperties = QAction( 'Survey design',  self.iface.mainWindow() )
        QObject.connect( self.actionSurveyProperties, SIGNAL("triggered()"), self.initSurveyDesign)

        self.checkSurveyDesignPossible()
        surveyDesignMenu.addAction(  self.actionSurveyProperties )
        self.surveyDesignAction = menuBar.addMenu( surveyDesignMenu )

        QObject.connect( self.iface, SIGNAL('projectRead()'), self.projectLoaded )

    def unload(self):
        self.iface.mainWindow().menuBar().removeAction( self.surveyDesignAction )

    def initSurveyDesign(self):
        self.initDialog = SurveyInitDialog( self.iface.mainWindow(),  self.iface)
        mainWindowGeom = self.iface.mainWindow().frameGeometry()
        self.initDialog.move( mainWindowGeom.width() / 2.0,  mainWindowGeom.top() )
        self.initDialog.show()

    def openSurveyDesignWidget(self):
        self.designDialog = SurveyDesignDialog( self.iface.mainWindow(),  self.iface )
        self.designDialog.show()

    def checkSurveyDesignPossible( self ):
            projectContainsDesign = self.projectContainsSurveyDesign()
            self.actionSurveyProperties.setEnabled( True )

    def projectContainsSurveyDesign(self):
        surveyAreaLayerId = QgsProject.instance().readEntry( "Survey",  "SurveyAreaLayer" )[0]
        strataLayerId = QgsProject.instance().readEntry( "Survey",  "StrataLayer" )[0]

        if not strataLayerId:
            return False
        else:
            return True

    def projectLoaded( self ):
        self.checkSurveyDesignPossible()
