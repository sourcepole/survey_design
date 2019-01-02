# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveyinitdialogbase.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_SurveyInitDialogBase(object):
    def setupUi(self, SurveyInitDialogBase):
        SurveyInitDialogBase.setObjectName(_fromUtf8("SurveyInitDialogBase"))
        SurveyInitDialogBase.resize(464, 766)
        self.gridLayout_5 = QtGui.QGridLayout(SurveyInitDialogBase)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mSurveyAreaLayerLabel = QtGui.QLabel(SurveyInitDialogBase)
        self.mSurveyAreaLayerLabel.setObjectName(_fromUtf8("mSurveyAreaLayerLabel"))
        self.horizontalLayout_3.addWidget(self.mSurveyAreaLayerLabel)
        self.mSurveyAreaLayerComboBox = QtGui.QComboBox(SurveyInitDialogBase)
        self.mSurveyAreaLayerComboBox.setObjectName(_fromUtf8("mSurveyAreaLayerComboBox"))
        self.horizontalLayout_3.addWidget(self.mSurveyAreaLayerComboBox)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.mBaselineGroupBox = QtGui.QGroupBox(SurveyInitDialogBase)
        self.mBaselineGroupBox.setObjectName(_fromUtf8("mBaselineGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.mBaselineGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mSurveyBaselineLayerComboBox = QtGui.QComboBox(self.mBaselineGroupBox)
        self.mSurveyBaselineLayerComboBox.setObjectName(_fromUtf8("mSurveyBaselineLayerComboBox"))
        self.gridLayout_2.addWidget(self.mSurveyBaselineLayerComboBox, 0, 1, 1, 1)
        self.mBaselineSimplificationToleranceLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineSimplificationToleranceLabel.setObjectName(_fromUtf8("mBaselineSimplificationToleranceLabel"))
        self.gridLayout_2.addWidget(self.mBaselineSimplificationToleranceLabel, 3, 0, 1, 1)
        self.mStratumIdComboBox = QtGui.QComboBox(self.mBaselineGroupBox)
        self.mStratumIdComboBox.setObjectName(_fromUtf8("mStratumIdComboBox"))
        self.gridLayout_2.addWidget(self.mStratumIdComboBox, 1, 1, 1, 1)
        self.mStratumIdLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mStratumIdLabel.setObjectName(_fromUtf8("mStratumIdLabel"))
        self.gridLayout_2.addWidget(self.mStratumIdLabel, 1, 0, 1, 1)
        self.mBaselineLayerLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineLayerLabel.setObjectName(_fromUtf8("mBaselineLayerLabel"))
        self.gridLayout_2.addWidget(self.mBaselineLayerLabel, 0, 0, 1, 1)
        self.mBaselineBufferDistanceSpinBox = QtGui.QDoubleSpinBox(self.mBaselineGroupBox)
        self.mBaselineBufferDistanceSpinBox.setMinimum(-1.0)
        self.mBaselineBufferDistanceSpinBox.setMaximum(999999999.0)
        self.mBaselineBufferDistanceSpinBox.setProperty("value", -1.0)
        self.mBaselineBufferDistanceSpinBox.setObjectName(_fromUtf8("mBaselineBufferDistanceSpinBox"))
        self.gridLayout_2.addWidget(self.mBaselineBufferDistanceSpinBox, 2, 1, 1, 1)
        self.mBaselineBufferDistanceLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineBufferDistanceLabel.setObjectName(_fromUtf8("mBaselineBufferDistanceLabel"))
        self.gridLayout_2.addWidget(self.mBaselineBufferDistanceLabel, 2, 0, 1, 1)
        self.mBaselineSimplificationToleranceSpinBox = QtGui.QDoubleSpinBox(self.mBaselineGroupBox)
        self.mBaselineSimplificationToleranceSpinBox.setMinimum(-1.0)
        self.mBaselineSimplificationToleranceSpinBox.setMaximum(999999999.0)
        self.mBaselineSimplificationToleranceSpinBox.setProperty("value", -1.0)
        self.mBaselineSimplificationToleranceSpinBox.setObjectName(_fromUtf8("mBaselineSimplificationToleranceSpinBox"))
        self.gridLayout_2.addWidget(self.mBaselineSimplificationToleranceSpinBox, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.mBaselineGroupBox, 1, 0, 1, 1)
        self.mSurveyDesignGroupBox = QtGui.QGroupBox(SurveyInitDialogBase)
        self.mSurveyDesignGroupBox.setObjectName(_fromUtf8("mSurveyDesignGroupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.mSurveyDesignGroupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(240, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mPointSurveyRadioButton = QtGui.QRadioButton(self.mSurveyDesignGroupBox)
        self.mPointSurveyRadioButton.setObjectName(_fromUtf8("mPointSurveyRadioButton"))
        self.horizontalLayout.addWidget(self.mPointSurveyRadioButton)
        self.mTransectSurveyRadioButton = QtGui.QRadioButton(self.mSurveyDesignGroupBox)
        self.mTransectSurveyRadioButton.setObjectName(_fromUtf8("mTransectSurveyRadioButton"))
        self.horizontalLayout.addWidget(self.mTransectSurveyRadioButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.mMinimumTransectLengthLabel = QtGui.QLabel(self.mSurveyDesignGroupBox)
        self.mMinimumTransectLengthLabel.setObjectName(_fromUtf8("mMinimumTransectLengthLabel"))
        self.gridLayout_4.addWidget(self.mMinimumTransectLengthLabel, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mShareBaselineCheckBox = QtGui.QCheckBox(self.mSurveyDesignGroupBox)
        self.mShareBaselineCheckBox.setChecked(False)
        self.mShareBaselineCheckBox.setObjectName(_fromUtf8("mShareBaselineCheckBox"))
        self.horizontalLayout_2.addWidget(self.mShareBaselineCheckBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.mMinimumTransectLengthSpinBox = QtGui.QDoubleSpinBox(self.mSurveyDesignGroupBox)
        self.mMinimumTransectLengthSpinBox.setDecimals(3)
        self.mMinimumTransectLengthSpinBox.setMaximum(99999999.0)
        self.mMinimumTransectLengthSpinBox.setObjectName(_fromUtf8("mMinimumTransectLengthSpinBox"))
        self.gridLayout_4.addWidget(self.mMinimumTransectLengthSpinBox, 2, 1, 1, 1)
        self.mCreateSampleButton = QtGui.QPushButton(self.mSurveyDesignGroupBox)
        self.mCreateSampleButton.setObjectName(_fromUtf8("mCreateSampleButton"))
        self.gridLayout_4.addWidget(self.mCreateSampleButton, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.mSurveyDesignGroupBox, 5, 0, 1, 1)
        self.mStrataGroupBox = QtGui.QGroupBox(SurveyInitDialogBase)
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
        self.gridLayout_5.addWidget(self.mStrataGroupBox, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SurveyInitDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_5.addWidget(self.buttonBox, 6, 0, 1, 1)

        self.retranslateUi(SurveyInitDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SurveyInitDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SurveyInitDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SurveyInitDialogBase)

    def retranslateUi(self, SurveyInitDialogBase):
        SurveyInitDialogBase.setWindowTitle(_translate("SurveyInitDialogBase", "Survey design", None))
        self.mSurveyAreaLayerLabel.setText(_translate("SurveyInitDialogBase", "Survey area layer", None))
        self.mBaselineGroupBox.setTitle(_translate("SurveyInitDialogBase", "Baseline", None))
        self.mBaselineSimplificationToleranceLabel.setText(_translate("SurveyInitDialogBase", "Simplification tolerance", None))
        self.mStratumIdLabel.setText(_translate("SurveyInitDialogBase", "Stratum id field", None))
        self.mBaselineLayerLabel.setText(_translate("SurveyInitDialogBase", "Survey baseline layer", None))
        self.mBaselineBufferDistanceLabel.setText(_translate("SurveyInitDialogBase", "Buffer distance", None))
        self.mSurveyDesignGroupBox.setTitle(_translate("SurveyInitDialogBase", "Survey design", None))
        self.mPointSurveyRadioButton.setText(_translate("SurveyInitDialogBase", "Point survey", None))
        self.mTransectSurveyRadioButton.setText(_translate("SurveyInitDialogBase", "Transect survey", None))
        self.mMinimumTransectLengthLabel.setText(_translate("SurveyInitDialogBase", "Minimum transect length", None))
        self.mShareBaselineCheckBox.setText(_translate("SurveyInitDialogBase", "Share baseline", None))
        self.mCreateSampleButton.setText(_translate("SurveyInitDialogBase", "Create sample sites", None))
        self.mStrataGroupBox.setTitle(_translate("SurveyInitDialogBase", "Strata", None))
        self.mNSamplePointsAttribute.setText(_translate("SurveyInitDialogBase", "N sample points attribute", None))
        self.mStrataIdAttributeLabel.setText(_translate("SurveyInitDialogBase", "ID attribute", None))
        self.mMinDistanceLabel.setText(_translate("SurveyInitDialogBase", "Minimum distance attribute", None))
        self.mMinDistanceUnitsLabel.setText(_translate("SurveyInitDialogBase", "Distance units", None))
        self.mStrataLayerLabel.setText(_translate("SurveyInitDialogBase", "Strata layer", None))

