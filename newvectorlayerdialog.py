from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from  qgis.gui import *
from ui_newvectorlayerdialogbase import Ui_NewVectorLayerDialogBase

class NewVectorLayerDialog( QDialog, Ui_NewVectorLayerDialogBase ):

    def __init__( self,  parent,  iface ):
        QDialog.__init__(  self,  parent )
        self.setupUi( self )
        self.iface = iface
        
        self.mFileEncoding.addItems( QgsVectorDataProvider.availableEncodings() )
        self.mFileEncoding.setCurrentIndex(  self.mFileEncoding.findText("UTF-8") )
        
        #setup type combo box
        self.mTypeBox.addItem( "String" )
        self.mTypeBox.addItem( "Integer" )
        self.mTypeBox.addItem("Real")
        
        self.mButtonBox.button( QDialogButtonBox.Ok ).setEnabled( False )
        
        self.mCRS = self.iface.mapCanvas().mapSettings().destinationCrs()
        self.mCrsButton.setText(  self.mCRS.authid() )
        
    def saveFilePath(self):
        return self.mFilePathLineEdit.text()
        
    def encoding(self):
        return self.mFileEncoding.currentText()
        
    def crs(self):
        return self.mCRS
        
    def fields(self):
        fields = QgsFields()
        fieldCount = self.mAttributeView.topLevelItemCount()
        for i in range(0,  fieldCount ):
            item = self.mAttributeView.topLevelItem( i )
            variantType = QVariant.String
            typeName = 'text'
            typeString = item.text( 1 )
            if typeString == "Integer":
                variantType = QVariant.Int
                typeName = 'int'
            elif typeString == "Real":
                variantType = QVariant.Double
                typeName = 'double'
            lengthInt = 0
            lengthText = item.text( 2 )
            if len( lengthText ) < 1:
                lengthInt = int(lengthText)
                
            precInt = 0
            precText = item.text( 3 )
            if len( precText ) < 1:
                precInt = int(precText)
                
            field = QgsField( item.text( 0 ),  variantType,  typeName,  lengthInt,  precInt )
            fields.append( field )
        return fields
        
    def addAttribute(self,  name,  type,  length,  precision):
        item = QTreeWidgetItem()
        item.setText( 0,  name )
        item.setText( 1,  type )
        if not (length is None ):
            item.setText( 2,  str(length) )
        if not ( precision  is None):
            item.setText( 3,  str(precision) )
        self.mAttributeView.addTopLevelItem( item )
        
    @pyqtSignature("on_mAddAttributeButton_clicked()")
    def on_mAddAttributeButton_clicked(self):
        item = QTreeWidgetItem()
        item.setText( 0, self.mNameEdit.text() )
        item.setText( 1,  self.mTypeBox.currentText() )
        item.setText( 2, self.mWidth.text() )
        item.setText( 3,  self.mPrecision.text() )
        self.mAttributeView.addTopLevelItem( item )
        
    @pyqtSignature("on_mRemoveAttributeButton_clicked()")
    def on_mRemoveAttributeButton_clicked( self ):
        currentItem = self.mAttributeView.currentItem()
        currentIndex = self.mAttributeView.indexOfTopLevelItem( currentItem )
        deleteItem = self.mAttributeView.takeTopLevelItem( currentIndex )
        del deleteItem
     
    @pyqtSignature("on_mBrowseFilePathButton_clicked()" )
    def on_mBrowseFilePathButton_clicked(self):
        newFilePath = QFileDialog.getSaveFileName( self, QObject.tr( self, "Select output file") )
        if not newFilePath is None:
            self.mFilePathLineEdit.setText( newFilePath )
            
    def on_mFilePathLineEdit_textChanged(self,  string ):
        filePath = self.mFilePathLineEdit.text()
        fileInfo = QFileInfo( filePath )
        dirFilePath = fileInfo.absolutePath();
        print (dirFilePath)
        dirFileInfo = QFileInfo( dirFilePath )
        if dirFileInfo.exists():
            self.mButtonBox.button( QDialogButtonBox.Ok ).setEnabled( True )
        else:
            self.mButtonBox.button( QDialogButtonBox.Ok ).setEnabled( False )
    
    @pyqtSignature("on_mCrsButton_clicked()" )
    def on_mCrsButton_clicked(self):
        crsDialog = QgsGenericProjectionSelector(  self )
        
        crsDialog.setSelectedAuthId( self.mCRS.authid() )
        if crsDialog.exec_() == QDialog.Accepted:
            authId = crsDialog.selectedAuthId()
            self.mCRS.createFromString( authId )
            self.mCrsButton.setText(  self.mCRS.authid() )
            
            
    
        
        
