from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from surveyinitdialog import SurveyInitDialog

class SurveyDesignPlugin:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        menuBar = self.iface.mainWindow().menuBar()
        surveyDesignMenu = QMenu( QCoreApplication.translate("SurveyDesignPlugin","Survey") ,  menuBar)

        self.actionSurveyProperties = QAction( 'Survey design',  self.iface.mainWindow() )
        QObject.connect( self.actionSurveyProperties, SIGNAL("triggered()"), self.initSurveyDesign)

        surveyDesignMenu.addAction(  self.actionSurveyProperties )
        self.surveyDesignAction = menuBar.addMenu( surveyDesignMenu )

    def unload(self):
        self.iface.mainWindow().menuBar().removeAction( self.surveyDesignAction )

    def initSurveyDesign(self):
        self.initDialog = SurveyInitDialog( self.iface.mainWindow(),  self.iface)
        mainWindowGeom = self.iface.mainWindow().frameGeometry()
        self.initDialog.move( mainWindowGeom.width() / 2.0,  mainWindowGeom.top() )
        self.initDialog.show()
