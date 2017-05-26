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
        TransectSurveyDialogBase.resize(531, 479)
        self.gridLayout_3 = QtGui.QGridLayout(TransectSurveyDialogBase)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mSurveyAreaLabel = QtGui.QLabel(TransectSurveyDialogBase)
        self.mSurveyAreaLabel.setObjectName(_fromUtf8("mSurveyAreaLabel"))
        self.horizontalLayout_2.addWidget(self.mSurveyAreaLabel)
        self.mSurveyAreaLayerComboBox = QtGui.QComboBox(TransectSurveyDialogBase)
        self.mSurveyAreaLayerComboBox.setObjectName(_fromUtf8("mSurveyAreaLayerComboBox"))
        self.horizontalLayout_2.addWidget(self.mSurveyAreaLayerComboBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mMinTransectLengthLabel = QtGui.QLabel(TransectSurveyDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mMinTransectLengthLabel.sizePolicy().hasHeightForWidth())
        self.mMinTransectLengthLabel.setSizePolicy(sizePolicy)
        self.mMinTransectLengthLabel.setObjectName(_fromUtf8("mMinTransectLengthLabel"))
        self.horizontalLayout.addWidget(self.mMinTransectLengthLabel)
        self.mMinimumTransectLengthSpinBox = QtGui.QDoubleSpinBox(TransectSurveyDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mMinimumTransectLengthSpinBox.sizePolicy().hasHeightForWidth())
        self.mMinimumTransectLengthSpinBox.setSizePolicy(sizePolicy)
        self.mMinimumTransectLengthSpinBox.setMinimum(-1.0)
        self.mMinimumTransectLengthSpinBox.setProperty("value", -1.0)
        self.mMinimumTransectLengthSpinBox.setObjectName(_fromUtf8("mMinimumTransectLengthSpinBox"))
        self.horizontalLayout.addWidget(self.mMinimumTransectLengthSpinBox)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.mBaselineGroupBox = QtGui.QGroupBox(TransectSurveyDialogBase)
        self.mBaselineGroupBox.setObjectName(_fromUtf8("mBaselineGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.mBaselineGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mSurveyBaselineLayerComboBox = QtGui.QComboBox(self.mBaselineGroupBox)
        self.mSurveyBaselineLayerComboBox.setObjectName(_fromUtf8("mSurveyBaselineLayerComboBox"))
        self.gridLayout_2.addWidget(self.mSurveyBaselineLayerComboBox, 0, 1, 1, 1)
        self.mBaselineLayerLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineLayerLabel.setObjectName(_fromUtf8("mBaselineLayerLabel"))
        self.gridLayout_2.addWidget(self.mBaselineLayerLabel, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.mBaselineGroupBox, 2, 0, 1, 3)
        self.mStrataGroupBox = QtGui.QGroupBox(TransectSurveyDialogBase)
        self.mStrataGroupBox.setObjectName(_fromUtf8("mStrataGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.mStrataGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mMinDistanceLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mMinDistanceLabel.setObjectName(_fromUtf8("mMinDistanceLabel"))
        self.gridLayout.addWidget(self.mMinDistanceLabel, 1, 0, 1, 1)
        self.mMinimumDistanceAttributeComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mMinimumDistanceAttributeComboBox.setObjectName(_fromUtf8("mMinimumDistanceAttributeComboBox"))
        self.gridLayout.addWidget(self.mMinimumDistanceAttributeComboBox, 1, 1, 1, 1)
        self.mStrataLayerLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mStrataLayerLabel.setObjectName(_fromUtf8("mStrataLayerLabel"))
        self.gridLayout.addWidget(self.mStrataLayerLabel, 0, 0, 1, 1)
        self.mStrataLayerComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mStrataLayerComboBox.setObjectName(_fromUtf8("mStrataLayerComboBox"))
        self.gridLayout.addWidget(self.mStrataLayerComboBox, 0, 1, 1, 1)
        self.mNSamplePointsAttribute = QtGui.QLabel(self.mStrataGroupBox)
        self.mNSamplePointsAttribute.setObjectName(_fromUtf8("mNSamplePointsAttribute"))
        self.gridLayout.addWidget(self.mNSamplePointsAttribute, 2, 0, 1, 1)
        self.mStrataIdAttributeComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mStrataIdAttributeComboBox.setObjectName(_fromUtf8("mStrataIdAttributeComboBox"))
        self.gridLayout.addWidget(self.mStrataIdAttributeComboBox, 3, 1, 1, 1)
        self.mNSamplePointsComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mNSamplePointsComboBox.setObjectName(_fromUtf8("mNSamplePointsComboBox"))
        self.gridLayout.addWidget(self.mNSamplePointsComboBox, 2, 1, 1, 1)
        self.mStrataIdAttributeLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mStrataIdAttributeLabel.setObjectName(_fromUtf8("mStrataIdAttributeLabel"))
        self.gridLayout.addWidget(self.mStrataIdAttributeLabel, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.mStrataGroupBox, 3, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(499, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 4, 0, 1, 1)
        self.mExportCsvButton = QtGui.QPushButton(TransectSurveyDialogBase)
        self.mExportCsvButton.setObjectName(_fromUtf8("mExportCsvButton"))
        self.gridLayout_3.addWidget(self.mExportCsvButton, 4, 1, 1, 1)
        self.mCreateSampleButton = QtGui.QPushButton(TransectSurveyDialogBase)
        self.mCreateSampleButton.setObjectName(_fromUtf8("mCreateSampleButton"))
        self.gridLayout_3.addWidget(self.mCreateSampleButton, 4, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TransectSurveyDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(TransectSurveyDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TransectSurveyDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TransectSurveyDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(TransectSurveyDialogBase)

    def retranslateUi(self, TransectSurveyDialogBase):
        TransectSurveyDialogBase.setWindowTitle(_translate("TransectSurveyDialogBase", "Transect Survey", None))
        self.mSurveyAreaLabel.setText(_translate("TransectSurveyDialogBase", "Survey area layer", None))
        self.mMinTransectLengthLabel.setText(_translate("TransectSurveyDialogBase", "Minimum transect length", None))
        self.mBaselineGroupBox.setTitle(_translate("TransectSurveyDialogBase", "Baseline", None))
        self.mBaselineLayerLabel.setText(_translate("TransectSurveyDialogBase", "Survey baseline layer", None))
        self.mStrataGroupBox.setTitle(_translate("TransectSurveyDialogBase", "Strata", None))
        self.mMinDistanceLabel.setText(_translate("TransectSurveyDialogBase", "Minimum distance attribute", None))
        self.mStrataLayerLabel.setText(_translate("TransectSurveyDialogBase", "Strata layer", None))
        self.mNSamplePointsAttribute.setText(_translate("TransectSurveyDialogBase", "N sample points attribute", None))
        self.mStrataIdAttributeLabel.setText(_translate("TransectSurveyDialogBase", "ID attribute", None))
        self.mExportCsvButton.setText(_translate("TransectSurveyDialogBase", "Export csv files", None))
        self.mCreateSampleButton.setText(_translate("TransectSurveyDialogBase", "Create sample sites", None))

