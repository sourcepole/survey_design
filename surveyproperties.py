from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_surveypropertiesbase import Ui_SurveyPropertiesBase

class SurveyProperties( QDialog,  Ui_SurveyPropertiesBase ):
    def __init__(self,  parent ):
        QDialog.__init__( self,  parent )
        self.setupUi(self)
        self.mDateSEdit.setDate( QDate.currentDate() )
        self.mDateFEdit.setDate( QDate.currentDate() )
        
    def survey(self):
        return self.mSurveyLineEdit.text()

    def projectCode(self):
        return self.mProjectCodeLineEdit.text()
        
    def date_s(self):
        return self.mDateSEdit.date().toString( 'dd/MM/yyyy' )
        
    def date_f(self):
        return self.mDateFEdit.date().toString( 'dd/MM/yyyy' )
        
    def contactName(self):
        return self.mContactNameLineEdit.text()
        
    def areas(self):
        return self.mAreasLineEdit.text()
        
    def mainspp(self):
        return self.mMainSppLineEdit.text()
        
    def comments(self):
        return self.mCommentsLIneEdit.text()
        
    
