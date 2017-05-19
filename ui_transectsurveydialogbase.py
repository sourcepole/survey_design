# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transectsurveydialogbase.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TransectSurveyDialogBase(object):
    def setupUi(self, TransectSurveyDialogBase):
        TransectSurveyDialogBase.setObjectName(_fromUtf8("TransectSurveyDialogBase"))
        TransectSurveyDialogBase.resize(574, 373)
        self.gridLayout_2 = QtGui.QGridLayout(TransectSurveyDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mStrataGroupBox = QtGui.QGroupBox(TransectSurveyDialogBase)
        self.mStrataGroupBox.setObjectName(_fromUtf8("mStrataGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.mStrataGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mMinimumDistanceAttributeComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mMinimumDistanceAttributeComboBox.setObjectName(_fromUtf8("mMinimumDistanceAttributeComboBox"))
        self.gridLayout.addWidget(self.mMinimumDistanceAttributeComboBox, 1, 1, 1, 1)
        self.mNSamplePointsAttribute = QtGui.QLabel(self.mStrataGroupBox)
        self.mNSamplePointsAttribute.setObjectName(_fromUtf8("mNSamplePointsAttribute"))
        self.gridLayout.addWidget(self.mNSamplePointsAttribute, 3, 0, 1, 1)
        self.mStrataIdAttributeLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mStrataIdAttributeLabel.setObjectName(_fromUtf8("mStrataIdAttributeLabel"))
        self.gridLayout.addWidget(self.mStrataIdAttributeLabel, 4, 0, 1, 1)
        self.mNSamplePointsComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mNSamplePointsComboBox.setObjectName(_fromUtf8("mNSamplePointsComboBox"))
        self.gridLayout.addWidget(self.mNSamplePointsComboBox, 3, 1, 1, 1)
        self.mStrataLayerComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mStrataLayerComboBox.setObjectName(_fromUtf8("mStrataLayerComboBox"))
        self.gridLayout.addWidget(self.mStrataLayerComboBox, 0, 1, 1, 1)
        self.mStrataIdAttributeComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mStrataIdAttributeComboBox.setObjectName(_fromUtf8("mStrataIdAttributeComboBox"))
        self.gridLayout.addWidget(self.mStrataIdAttributeComboBox, 4, 1, 1, 1)
        self.mMinDistanceLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mMinDistanceLabel.setObjectName(_fromUtf8("mMinDistanceLabel"))
        self.gridLayout.addWidget(self.mMinDistanceLabel, 1, 0, 1, 1)
        self.mMinDistanceUnitsLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mMinDistanceUnitsLabel.setObjectName(_fromUtf8("mMinDistanceUnitsLabel"))
        self.gridLayout.addWidget(self.mMinDistanceUnitsLabel, 2, 0, 1, 1)
        self.mMinDistanceUnitsComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mMinDistanceUnitsComboBox.setObjectName(_fromUtf8("mMinDistanceUnitsComboBox"))
        self.gridLayout.addWidget(self.mMinDistanceUnitsComboBox, 2, 1, 1, 1)
        self.mStrataLayerLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mStrataLayerLabel.setObjectName(_fromUtf8("mStrataLayerLabel"))
        self.gridLayout.addWidget(self.mStrataLayerLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.mStrataGroupBox, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(427, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.mCreateSampleButton = QtGui.QPushButton(TransectSurveyDialogBase)
        self.mCreateSampleButton.setObjectName(_fromUtf8("mCreateSampleButton"))
        self.gridLayout_2.addWidget(self.mCreateSampleButton, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TransectSurveyDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(TransectSurveyDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TransectSurveyDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TransectSurveyDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(TransectSurveyDialogBase)

    def retranslateUi(self, TransectSurveyDialogBase):
        TransectSurveyDialogBase.setWindowTitle(_translate("TransectSurveyDialogBase", "Transect Survey", None))
        self.mStrataGroupBox.setTitle(_translate("TransectSurveyDialogBase", "Strata", None))
        self.mNSamplePointsAttribute.setText(_translate("TransectSurveyDialogBase", "N sample points attribute", None))
        self.mStrataIdAttributeLabel.setText(_translate("TransectSurveyDialogBase", "ID attribute", None))
        self.mMinDistanceLabel.setText(_translate("TransectSurveyDialogBase", "Minimum distance attribute", None))
        self.mMinDistanceUnitsLabel.setText(_translate("TransectSurveyDialogBase", "Distance units", None))
        self.mStrataLayerLabel.setText(_translate("TransectSurveyDialogBase", "Strata layer", None))
        self.mCreateSampleButton.setText(_translate("TransectSurveyDialogBase", "Create sample sites", None))

