from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from  qgis.gui import *
from ui_addattrdialogbase import Ui_AddAttrDialogBase

class AddAttrDialog( QDialog, Ui_AddAttrDialogBase ):
    def __init__(self,  parent ):
        QDialog.__init__( self,  parent )
        self.setupUi( self )
        self.mTypeBox.addItem( "String" )
        self.mTypeBox.addItem( "Integer" )
        self.mTypeBox.addItem("Real")
        
    def setFieldName(self,  fieldName ):
        self.mNameEdit.setText( fieldName )
    
    def setLength(self,  length ):
        self.mLength.setValue( length )
        
    def setPrecision(self,  precision ):
        self.mPrec.setValue( precision )
        
    def setType(self,  type):
        self.mTypeBox.setCurrentIndex( self.mTypeBox.findText( type ) )
        
    def field(self):
        variantType = QVariant.String
        typeName = 'text'
        typeString = self.mTypeBox.currentText()
        if typeString == "Integer":
            variantType = QVariant.Int
            typeName = 'int'
        elif typeString == "Real":
            variantType = QVariant.Double
            typeName = 'double'
        
        field = QgsField( self.mNameEdit.text(), variantType ,  typeName,  self.mLength.value(),  self.mPrec.value() )
        return field
