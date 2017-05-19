from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_transectsurveydialogbase import Ui_TransectSurveyDialogBase

class TransectSurveyDialog( QDialog,  Ui_TransectSurveyDialogBase ):
    def __init__(self,  parent,  iface ):
        QDialog.__init__( self,  parent )
        self.iface = iface
        self.setupUi(self)

