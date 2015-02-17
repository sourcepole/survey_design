# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveyevaluationdialogbase.ui'
#
# Created: Thu Feb  5 10:58:57 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SurveyEvaluationDialogBase(object):
    def setupUi(self, SurveyEvaluationDialogBase):
        SurveyEvaluationDialogBase.setObjectName(_fromUtf8("SurveyEvaluationDialogBase"))
        SurveyEvaluationDialogBase.resize(286, 252)
        self.gridLayout_2 = QtGui.QGridLayout(SurveyEvaluationDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mStratumIdComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mStratumIdComboBox.setObjectName(_fromUtf8("mStratumIdComboBox"))
        self.gridLayout.addWidget(self.mStratumIdComboBox, 2, 1, 1, 1)
        self.mVavailComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mVavailComboBox.setObjectName(_fromUtf8("mVavailComboBox"))
        self.gridLayout.addWidget(self.mVavailComboBox, 7, 1, 1, 1)
        self.mDistLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mDistLabel.setObjectName(_fromUtf8("mDistLabel"))
        self.gridLayout.addWidget(self.mDistLabel, 5, 0, 1, 1)
        self.mWidthLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mWidthLabel.setObjectName(_fromUtf8("mWidthLabel"))
        self.gridLayout.addWidget(self.mWidthLabel, 6, 0, 1, 1)
        self.mSampleLayerLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mSampleLayerLabel.setObjectName(_fromUtf8("mSampleLayerLabel"))
        self.gridLayout.addWidget(self.mSampleLayerLabel, 0, 0, 1, 1)
        self.mDistComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mDistComboBox.setObjectName(_fromUtf8("mDistComboBox"))
        self.gridLayout.addWidget(self.mDistComboBox, 5, 1, 1, 1)
        self.mCatchLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mCatchLabel.setObjectName(_fromUtf8("mCatchLabel"))
        self.gridLayout.addWidget(self.mCatchLabel, 4, 0, 1, 1)
        self.mSampleLayerComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mSampleLayerComboBox.setObjectName(_fromUtf8("mSampleLayerComboBox"))
        self.gridLayout.addWidget(self.mSampleLayerComboBox, 0, 1, 1, 1)
        self.mStratumIdLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mStratumIdLabel.setObjectName(_fromUtf8("mStratumIdLabel"))
        self.gridLayout.addWidget(self.mStratumIdLabel, 2, 0, 1, 1)
        self.mVavailLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mVavailLabel.setObjectName(_fromUtf8("mVavailLabel"))
        self.gridLayout.addWidget(self.mVavailLabel, 7, 0, 1, 1)
        self.mWidthComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mWidthComboBox.setObjectName(_fromUtf8("mWidthComboBox"))
        self.gridLayout.addWidget(self.mWidthComboBox, 6, 1, 1, 1)
        self.mCatchComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mCatchComboBox.setObjectName(_fromUtf8("mCatchComboBox"))
        self.gridLayout.addWidget(self.mCatchComboBox, 4, 1, 1, 1)
        self.mArealAvailabliltyLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mArealAvailabliltyLabel.setObjectName(_fromUtf8("mArealAvailabliltyLabel"))
        self.gridLayout.addWidget(self.mArealAvailabliltyLabel, 3, 0, 1, 1)
        self.mArealAvailabilityComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mArealAvailabilityComboBox.setObjectName(_fromUtf8("mArealAvailabilityComboBox"))
        self.gridLayout.addWidget(self.mArealAvailabilityComboBox, 3, 1, 1, 1)
        self.mBaselineLayerClipComboBox = QtGui.QComboBox(SurveyEvaluationDialogBase)
        self.mBaselineLayerClipComboBox.setObjectName(_fromUtf8("mBaselineLayerClipComboBox"))
        self.gridLayout.addWidget(self.mBaselineLayerClipComboBox, 1, 1, 1, 1)
        self.mBaselineClipLayerLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mBaselineClipLayerLabel.setObjectName(_fromUtf8("mBaselineClipLayerLabel"))
        self.gridLayout.addWidget(self.mBaselineClipLayerLabel, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mSpeciesVulnerabilityLabel = QtGui.QLabel(SurveyEvaluationDialogBase)
        self.mSpeciesVulnerabilityLabel.setObjectName(_fromUtf8("mSpeciesVulnerabilityLabel"))
        self.horizontalLayout.addWidget(self.mSpeciesVulnerabilityLabel)
        self.mSpeciesVulnerabilitySpinBox = QtGui.QDoubleSpinBox(SurveyEvaluationDialogBase)
        self.mSpeciesVulnerabilitySpinBox.setMaximum(1.0)
        self.mSpeciesVulnerabilitySpinBox.setSingleStep(0.1)
        self.mSpeciesVulnerabilitySpinBox.setProperty("value", 1.0)
        self.mSpeciesVulnerabilitySpinBox.setObjectName(_fromUtf8("mSpeciesVulnerabilitySpinBox"))
        self.horizontalLayout.addWidget(self.mSpeciesVulnerabilitySpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SurveyEvaluationDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(SurveyEvaluationDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SurveyEvaluationDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SurveyEvaluationDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SurveyEvaluationDialogBase)

    def retranslateUi(self, SurveyEvaluationDialogBase):
        SurveyEvaluationDialogBase.setWindowTitle(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Survey evaluation", None, QtGui.QApplication.UnicodeUTF8))
        self.mDistLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Dist", None, QtGui.QApplication.UnicodeUTF8))
        self.mWidthLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.mSampleLayerLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Sample layer", None, QtGui.QApplication.UnicodeUTF8))
        self.mCatchLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Catch", None, QtGui.QApplication.UnicodeUTF8))
        self.mStratumIdLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Stratum id", None, QtGui.QApplication.UnicodeUTF8))
        self.mVavailLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Vertical availability", None, QtGui.QApplication.UnicodeUTF8))
        self.mArealAvailabliltyLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Areal availability", None, QtGui.QApplication.UnicodeUTF8))
        self.mBaselineClipLayerLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Baseline clip layer", None, QtGui.QApplication.UnicodeUTF8))
        self.mSpeciesVulnerabilityLabel.setText(QtGui.QApplication.translate("SurveyEvaluationDialogBase", "Species vulnerability", None, QtGui.QApplication.UnicodeUTF8))

