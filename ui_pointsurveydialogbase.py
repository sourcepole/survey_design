# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pointsurveydialogbase.ui'
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

class Ui_PointSurveyDialogBase(object):
    def setupUi(self, PointSurveyDialogBase):
        PointSurveyDialogBase.setObjectName(_fromUtf8("PointSurveyDialogBase"))
        PointSurveyDialogBase.resize(443, 300)
        self.gridLayout_2 = QtGui.QGridLayout(PointSurveyDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(296, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PointSurveyDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 3)
        self.mCreateSampleButton = QtGui.QPushButton(PointSurveyDialogBase)
        self.mCreateSampleButton.setObjectName(_fromUtf8("mCreateSampleButton"))
        self.gridLayout_2.addWidget(self.mCreateSampleButton, 1, 2, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mMinDistanceLabel = QtGui.QLabel(PointSurveyDialogBase)
        self.mMinDistanceLabel.setObjectName(_fromUtf8("mMinDistanceLabel"))
        self.gridLayout.addWidget(self.mMinDistanceLabel, 3, 0, 1, 1)
        self.mNSamplePointsComboBox = QtGui.QComboBox(PointSurveyDialogBase)
        self.mNSamplePointsComboBox.setObjectName(_fromUtf8("mNSamplePointsComboBox"))
        self.gridLayout.addWidget(self.mNSamplePointsComboBox, 4, 1, 1, 1)
        self.mStrataLayerLabel = QtGui.QLabel(PointSurveyDialogBase)
        self.mStrataLayerLabel.setObjectName(_fromUtf8("mStrataLayerLabel"))
        self.gridLayout.addWidget(self.mStrataLayerLabel, 1, 0, 1, 1)
        self.mSurveyAreaLayerComboBox = QtGui.QComboBox(PointSurveyDialogBase)
        self.mSurveyAreaLayerComboBox.setObjectName(_fromUtf8("mSurveyAreaLayerComboBox"))
        self.gridLayout.addWidget(self.mSurveyAreaLayerComboBox, 0, 1, 1, 1)
        self.mMinimumDistanceAttributeComboBox = QtGui.QComboBox(PointSurveyDialogBase)
        self.mMinimumDistanceAttributeComboBox.setObjectName(_fromUtf8("mMinimumDistanceAttributeComboBox"))
        self.gridLayout.addWidget(self.mMinimumDistanceAttributeComboBox, 3, 1, 1, 1)
        self.mSurveyAreaLabel = QtGui.QLabel(PointSurveyDialogBase)
        self.mSurveyAreaLabel.setObjectName(_fromUtf8("mSurveyAreaLabel"))
        self.gridLayout.addWidget(self.mSurveyAreaLabel, 0, 0, 1, 1)
        self.mStrataLayerComboBox = QtGui.QComboBox(PointSurveyDialogBase)
        self.mStrataLayerComboBox.setObjectName(_fromUtf8("mStrataLayerComboBox"))
        self.gridLayout.addWidget(self.mStrataLayerComboBox, 1, 1, 1, 1)
        self.mNSamplePointsAttribute = QtGui.QLabel(PointSurveyDialogBase)
        self.mNSamplePointsAttribute.setObjectName(_fromUtf8("mNSamplePointsAttribute"))
        self.gridLayout.addWidget(self.mNSamplePointsAttribute, 4, 0, 1, 1)
        self.mStrataIdComboBox = QtGui.QComboBox(PointSurveyDialogBase)
        self.mStrataIdComboBox.setObjectName(_fromUtf8("mStrataIdComboBox"))
        self.gridLayout.addWidget(self.mStrataIdComboBox, 2, 1, 1, 1)
        self.mStrataIdLabel = QtGui.QLabel(PointSurveyDialogBase)
        self.mStrataIdLabel.setObjectName(_fromUtf8("mStrataIdLabel"))
        self.gridLayout.addWidget(self.mStrataIdLabel, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        self.mExportCsvFilesButton = QtGui.QPushButton(PointSurveyDialogBase)
        self.mExportCsvFilesButton.setObjectName(_fromUtf8("mExportCsvFilesButton"))
        self.gridLayout_2.addWidget(self.mExportCsvFilesButton, 1, 1, 1, 1)

        self.retranslateUi(PointSurveyDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PointSurveyDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PointSurveyDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(PointSurveyDialogBase)

    def retranslateUi(self, PointSurveyDialogBase):
        PointSurveyDialogBase.setWindowTitle(_translate("PointSurveyDialogBase", "Point Survey", None))
        self.mCreateSampleButton.setText(_translate("PointSurveyDialogBase", "Create sample sites", None))
        self.mMinDistanceLabel.setText(_translate("PointSurveyDialogBase", "Minimum distance attribute", None))
        self.mStrataLayerLabel.setText(_translate("PointSurveyDialogBase", "Strata layer", None))
        self.mSurveyAreaLabel.setText(_translate("PointSurveyDialogBase", "Survey area layer", None))
        self.mNSamplePointsAttribute.setText(_translate("PointSurveyDialogBase", "N sample points attribute", None))
        self.mStrataIdLabel.setText(_translate("PointSurveyDialogBase", "Strata id", None))
        self.mExportCsvFilesButton.setText(_translate("PointSurveyDialogBase", "Export csv files", None))

