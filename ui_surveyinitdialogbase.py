# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveyinitdialogbase.ui'
#
# Created: Sun Mar 15 10:23:54 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SurveyInitDialogBase(object):
    def setupUi(self, SurveyInitDialogBase):
        SurveyInitDialogBase.setObjectName(_fromUtf8("SurveyInitDialogBase"))
        SurveyInitDialogBase.resize(464, 569)
        self.gridLayout_5 = QtGui.QGridLayout(SurveyInitDialogBase)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mSurveyAreaLayerLabel = QtGui.QLabel(SurveyInitDialogBase)
        self.mSurveyAreaLayerLabel.setObjectName(_fromUtf8("mSurveyAreaLayerLabel"))
        self.horizontalLayout_3.addWidget(self.mSurveyAreaLayerLabel)
        self.mSurveyAreaLayerComboBox = QtGui.QComboBox(SurveyInitDialogBase)
        self.mSurveyAreaLayerComboBox.setObjectName(_fromUtf8("mSurveyAreaLayerComboBox"))
        self.horizontalLayout_3.addWidget(self.mSurveyAreaLayerComboBox)
        self.mNewSurveyLayerButton = QtGui.QToolButton(SurveyInitDialogBase)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/survey_design/mActionNewVectorLayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mNewSurveyLayerButton.setIcon(icon)
        self.mNewSurveyLayerButton.setObjectName(_fromUtf8("mNewSurveyLayerButton"))
        self.horizontalLayout_3.addWidget(self.mNewSurveyLayerButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.mBaselineGroupBox = QtGui.QGroupBox(SurveyInitDialogBase)
        self.mBaselineGroupBox.setObjectName(_fromUtf8("mBaselineGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.mBaselineGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mStratumIdComboBox = QtGui.QComboBox(self.mBaselineGroupBox)
        self.mStratumIdComboBox.setObjectName(_fromUtf8("mStratumIdComboBox"))
        self.gridLayout_2.addWidget(self.mStratumIdComboBox, 1, 1, 1, 1)
        self.mBaselineLayerLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineLayerLabel.setObjectName(_fromUtf8("mBaselineLayerLabel"))
        self.gridLayout_2.addWidget(self.mBaselineLayerLabel, 0, 0, 1, 1)
        self.mNewBaselineLayerButton = QtGui.QToolButton(self.mBaselineGroupBox)
        self.mNewBaselineLayerButton.setIcon(icon)
        self.mNewBaselineLayerButton.setObjectName(_fromUtf8("mNewBaselineLayerButton"))
        self.gridLayout_2.addWidget(self.mNewBaselineLayerButton, 0, 2, 1, 1)
        self.mBaselineBufferDistanceLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineBufferDistanceLabel.setObjectName(_fromUtf8("mBaselineBufferDistanceLabel"))
        self.gridLayout_2.addWidget(self.mBaselineBufferDistanceLabel, 2, 0, 1, 1)
        self.mSurveyBaselineLayerComboBox = QtGui.QComboBox(self.mBaselineGroupBox)
        self.mSurveyBaselineLayerComboBox.setObjectName(_fromUtf8("mSurveyBaselineLayerComboBox"))
        self.gridLayout_2.addWidget(self.mSurveyBaselineLayerComboBox, 0, 1, 1, 1)
        self.mBaselineBufferDistanceSpinBox = QtGui.QDoubleSpinBox(self.mBaselineGroupBox)
        self.mBaselineBufferDistanceSpinBox.setMinimum(-1.0)
        self.mBaselineBufferDistanceSpinBox.setMaximum(999999999.0)
        self.mBaselineBufferDistanceSpinBox.setProperty("value", -1.0)
        self.mBaselineBufferDistanceSpinBox.setObjectName(_fromUtf8("mBaselineBufferDistanceSpinBox"))
        self.gridLayout_2.addWidget(self.mBaselineBufferDistanceSpinBox, 2, 1, 1, 1)
        self.mStratumIdToolButton = QtGui.QToolButton(self.mBaselineGroupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/survey_design/mActionNewAttribute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mStratumIdToolButton.setIcon(icon1)
        self.mStratumIdToolButton.setObjectName(_fromUtf8("mStratumIdToolButton"))
        self.gridLayout_2.addWidget(self.mStratumIdToolButton, 1, 2, 1, 1)
        self.mStratumIdLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mStratumIdLabel.setObjectName(_fromUtf8("mStratumIdLabel"))
        self.gridLayout_2.addWidget(self.mStratumIdLabel, 1, 0, 1, 1)
        self.mBaselineSimplificationToleranceLabel = QtGui.QLabel(self.mBaselineGroupBox)
        self.mBaselineSimplificationToleranceLabel.setObjectName(_fromUtf8("mBaselineSimplificationToleranceLabel"))
        self.gridLayout_2.addWidget(self.mBaselineSimplificationToleranceLabel, 3, 0, 1, 1)
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
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.mAddBaselineLabel = QtGui.QLabel(self.mSurveyDesignGroupBox)
        self.mAddBaselineLabel.setObjectName(_fromUtf8("mAddBaselineLabel"))
        self.gridLayout_3.addWidget(self.mAddBaselineLabel, 2, 0, 1, 1)
        self.mAddBaselineToolButton = QtGui.QToolButton(self.mSurveyDesignGroupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/survey_design/mActionToggleEditing.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mAddBaselineToolButton.setIcon(icon2)
        self.mAddBaselineToolButton.setCheckable(True)
        self.mAddBaselineToolButton.setObjectName(_fromUtf8("mAddBaselineToolButton"))
        self.gridLayout_3.addWidget(self.mAddBaselineToolButton, 2, 1, 1, 1)
        self.mAddStratumLabel = QtGui.QLabel(self.mSurveyDesignGroupBox)
        self.mAddStratumLabel.setObjectName(_fromUtf8("mAddStratumLabel"))
        self.gridLayout_3.addWidget(self.mAddStratumLabel, 1, 0, 1, 1)
        self.mAddStratumToolButton = QtGui.QToolButton(self.mSurveyDesignGroupBox)
        self.mAddStratumToolButton.setIcon(icon2)
        self.mAddStratumToolButton.setCheckable(True)
        self.mAddStratumToolButton.setObjectName(_fromUtf8("mAddStratumToolButton"))
        self.gridLayout_3.addWidget(self.mAddStratumToolButton, 1, 1, 1, 1)
        self.mAddSurveyAreaLabel = QtGui.QLabel(self.mSurveyDesignGroupBox)
        self.mAddSurveyAreaLabel.setObjectName(_fromUtf8("mAddSurveyAreaLabel"))
        self.gridLayout_3.addWidget(self.mAddSurveyAreaLabel, 0, 0, 1, 1)
        self.mAddSurveyAreaToolButton = QtGui.QToolButton(self.mSurveyDesignGroupBox)
        self.mAddSurveyAreaToolButton.setIcon(icon2)
        self.mAddSurveyAreaToolButton.setCheckable(True)
        self.mAddSurveyAreaToolButton.setObjectName(_fromUtf8("mAddSurveyAreaToolButton"))
        self.gridLayout_3.addWidget(self.mAddSurveyAreaToolButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mPointSurveyRadioButton = QtGui.QRadioButton(self.mSurveyDesignGroupBox)
        self.mPointSurveyRadioButton.setObjectName(_fromUtf8("mPointSurveyRadioButton"))
        self.horizontalLayout.addWidget(self.mPointSurveyRadioButton)
        self.mTransectSurveyRadioButton = QtGui.QRadioButton(self.mSurveyDesignGroupBox)
        self.mTransectSurveyRadioButton.setObjectName(_fromUtf8("mTransectSurveyRadioButton"))
        self.horizontalLayout.addWidget(self.mTransectSurveyRadioButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(240, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mShareBaselineCheckBox = QtGui.QCheckBox(self.mSurveyDesignGroupBox)
        self.mShareBaselineCheckBox.setChecked(False)
        self.mShareBaselineCheckBox.setObjectName(_fromUtf8("mShareBaselineCheckBox"))
        self.horizontalLayout_2.addWidget(self.mShareBaselineCheckBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.mCreateSampleButton = QtGui.QPushButton(self.mSurveyDesignGroupBox)
        self.mCreateSampleButton.setObjectName(_fromUtf8("mCreateSampleButton"))
        self.gridLayout_4.addWidget(self.mCreateSampleButton, 4, 1, 1, 1)
        self.mMinimumTransectLengthLabel = QtGui.QLabel(self.mSurveyDesignGroupBox)
        self.mMinimumTransectLengthLabel.setObjectName(_fromUtf8("mMinimumTransectLengthLabel"))
        self.gridLayout_4.addWidget(self.mMinimumTransectLengthLabel, 3, 0, 1, 1)
        self.mMinimumTransectLengthSpinBox = QtGui.QDoubleSpinBox(self.mSurveyDesignGroupBox)
        self.mMinimumTransectLengthSpinBox.setMaximum(99999999.0)
        self.mMinimumTransectLengthSpinBox.setObjectName(_fromUtf8("mMinimumTransectLengthSpinBox"))
        self.gridLayout_4.addWidget(self.mMinimumTransectLengthSpinBox, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.mSurveyDesignGroupBox, 5, 0, 1, 1)
        self.mStrataGroupBox = QtGui.QGroupBox(SurveyInitDialogBase)
        self.mStrataGroupBox.setObjectName(_fromUtf8("mStrataGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.mStrataGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mStrataIdAttributeComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mStrataIdAttributeComboBox.setObjectName(_fromUtf8("mStrataIdAttributeComboBox"))
        self.gridLayout.addWidget(self.mStrataIdAttributeComboBox, 4, 1, 1, 1)
        self.mStrataIdAttributeLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mStrataIdAttributeLabel.setObjectName(_fromUtf8("mStrataIdAttributeLabel"))
        self.gridLayout.addWidget(self.mStrataIdAttributeLabel, 4, 0, 1, 1)
        self.mNSamplePointsComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mNSamplePointsComboBox.setObjectName(_fromUtf8("mNSamplePointsComboBox"))
        self.gridLayout.addWidget(self.mNSamplePointsComboBox, 3, 1, 1, 1)
        self.mMinDistanceLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mMinDistanceLabel.setObjectName(_fromUtf8("mMinDistanceLabel"))
        self.gridLayout.addWidget(self.mMinDistanceLabel, 1, 0, 1, 1)
        self.mStrataLayerComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mStrataLayerComboBox.setObjectName(_fromUtf8("mStrataLayerComboBox"))
        self.gridLayout.addWidget(self.mStrataLayerComboBox, 0, 1, 1, 1)
        self.mMinimumDistanceAttributeComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mMinimumDistanceAttributeComboBox.setObjectName(_fromUtf8("mMinimumDistanceAttributeComboBox"))
        self.gridLayout.addWidget(self.mMinimumDistanceAttributeComboBox, 1, 1, 1, 1)
        self.mNewStrataLayerButton = QtGui.QToolButton(self.mStrataGroupBox)
        self.mNewStrataLayerButton.setIcon(icon)
        self.mNewStrataLayerButton.setObjectName(_fromUtf8("mNewStrataLayerButton"))
        self.gridLayout.addWidget(self.mNewStrataLayerButton, 0, 2, 1, 1)
        self.mNSamplePointsAttribute = QtGui.QLabel(self.mStrataGroupBox)
        self.mNSamplePointsAttribute.setObjectName(_fromUtf8("mNSamplePointsAttribute"))
        self.gridLayout.addWidget(self.mNSamplePointsAttribute, 3, 0, 1, 1)
        self.mStrataLayerLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mStrataLayerLabel.setObjectName(_fromUtf8("mStrataLayerLabel"))
        self.gridLayout.addWidget(self.mStrataLayerLabel, 0, 0, 1, 1)
        self.mStrataMinDistToolButton = QtGui.QToolButton(self.mStrataGroupBox)
        self.mStrataMinDistToolButton.setIcon(icon1)
        self.mStrataMinDistToolButton.setObjectName(_fromUtf8("mStrataMinDistToolButton"))
        self.gridLayout.addWidget(self.mStrataMinDistToolButton, 1, 2, 1, 1)
        self.mStrataNSamplePointsToolButton = QtGui.QToolButton(self.mStrataGroupBox)
        self.mStrataNSamplePointsToolButton.setIcon(icon1)
        self.mStrataNSamplePointsToolButton.setObjectName(_fromUtf8("mStrataNSamplePointsToolButton"))
        self.gridLayout.addWidget(self.mStrataNSamplePointsToolButton, 3, 2, 1, 1)
        self.mStrataIdAttributeToolButton = QtGui.QToolButton(self.mStrataGroupBox)
        self.mStrataIdAttributeToolButton.setIcon(icon1)
        self.mStrataIdAttributeToolButton.setObjectName(_fromUtf8("mStrataIdAttributeToolButton"))
        self.gridLayout.addWidget(self.mStrataIdAttributeToolButton, 4, 2, 1, 1)
        self.mMinDistanceUnitsComboBox = QtGui.QComboBox(self.mStrataGroupBox)
        self.mMinDistanceUnitsComboBox.setObjectName(_fromUtf8("mMinDistanceUnitsComboBox"))
        self.gridLayout.addWidget(self.mMinDistanceUnitsComboBox, 2, 1, 1, 1)
        self.mMinDistanceUnitsLabel = QtGui.QLabel(self.mStrataGroupBox)
        self.mMinDistanceUnitsLabel.setObjectName(_fromUtf8("mMinDistanceUnitsLabel"))
        self.gridLayout.addWidget(self.mMinDistanceUnitsLabel, 2, 0, 1, 1)
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
        SurveyInitDialogBase.setWindowTitle(QtGui.QApplication.translate("SurveyInitDialogBase", "Survey design", None, QtGui.QApplication.UnicodeUTF8))
        self.mSurveyAreaLayerLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Survey area layer", None, QtGui.QApplication.UnicodeUTF8))
        self.mNewSurveyLayerButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mBaselineGroupBox.setTitle(QtGui.QApplication.translate("SurveyInitDialogBase", "Baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.mBaselineLayerLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Survey baseline layer", None, QtGui.QApplication.UnicodeUTF8))
        self.mNewBaselineLayerButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mBaselineBufferDistanceLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Buffer distance", None, QtGui.QApplication.UnicodeUTF8))
        self.mStratumIdToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mStratumIdLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Stratum id field", None, QtGui.QApplication.UnicodeUTF8))
        self.mBaselineSimplificationToleranceLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Simplification tolerance", None, QtGui.QApplication.UnicodeUTF8))
        self.mSurveyDesignGroupBox.setTitle(QtGui.QApplication.translate("SurveyInitDialogBase", "Survey design", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddBaselineLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Add baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddBaselineToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddStratumLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Add stratum", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddStratumToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddSurveyAreaLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Add survey area", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddSurveyAreaToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mPointSurveyRadioButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Point survey", None, QtGui.QApplication.UnicodeUTF8))
        self.mTransectSurveyRadioButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Transect survey", None, QtGui.QApplication.UnicodeUTF8))
        self.mShareBaselineCheckBox.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Share baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.mCreateSampleButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Create sample sites", None, QtGui.QApplication.UnicodeUTF8))
        self.mMinimumTransectLengthLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Minimum transect length", None, QtGui.QApplication.UnicodeUTF8))
        self.mStrataGroupBox.setTitle(QtGui.QApplication.translate("SurveyInitDialogBase", "Strata", None, QtGui.QApplication.UnicodeUTF8))
        self.mStrataIdAttributeLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "ID attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.mMinDistanceLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Minimum distance attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.mNewStrataLayerButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mNSamplePointsAttribute.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "N sample points attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.mStrataLayerLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Strata layer", None, QtGui.QApplication.UnicodeUTF8))
        self.mStrataMinDistToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mStrataNSamplePointsToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mStrataIdAttributeToolButton.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mMinDistanceUnitsLabel.setText(QtGui.QApplication.translate("SurveyInitDialogBase", "Distance units", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
