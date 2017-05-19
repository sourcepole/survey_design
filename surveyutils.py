from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def fillLayerComboBox( comboBox,  geometryType,  noneEntry ):
        comboBox.clear()
        if noneEntry == True:
            comboBox.addItem( comboBox.tr( 'None' ) )

        mapLayers = QgsMapLayerRegistry.instance().mapLayers()
        for id in mapLayers:
            currentLayer = mapLayers[id]
            if currentLayer.type() != QgsMapLayer.VectorLayer:
                continue

            if currentLayer.geometryType() == geometryType:
                comboBox.addItem( currentLayer.name(), currentLayer.id() )
                
def fillAttributeComboBox( comboBox,  vectorLayer ):
    comboBox.clear()
    if not vectorLayer is None:
        if not vectorLayer.type() == QgsMapLayer.VectorLayer:
            return

        fieldList = vectorLayer.pendingFields().toList()
        for field in fieldList:
            comboBox.addItem( field.name() )
