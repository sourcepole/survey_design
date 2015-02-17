# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveydesigndialogbase.ui'
#
# Created: Thu Feb  5 09:59:31 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SurveyDesignDialogBase(object):
    def setupUi(self, SurveyDesignDialogBase):
        SurveyDesignDialogBase.setObjectName(_fromUtf8("SurveyDesignDialogBase"))
        SurveyDesignDialogBase.resize(296, 207)
        self.gridLayout_2 = QtGui.QGridLayout(SurveyDesignDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mAddBaselineLabel = QtGui.QLabel(SurveyDesignDialogBase)
        self.mAddBaselineLabel.setObjectName(_fromUtf8("mAddBaselineLabel"))
        self.gridLayout.addWidget(self.mAddBaselineLabel, 2, 0, 1, 1)
        self.mAddBaselineToolButton = QtGui.QToolButton(SurveyDesignDialogBase)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/survey_design/mActionToggleEditing.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mAddBaselineToolButton.setIcon(icon)
        self.mAddBaselineToolButton.setCheckable(True)
        self.mAddBaselineToolButton.setObjectName(_fromUtf8("mAddBaselineToolButton"))
        self.gridLayout.addWidget(self.mAddBaselineToolButton, 2, 1, 1, 1)
        self.mAddStratumLabel = QtGui.QLabel(SurveyDesignDialogBase)
        self.mAddStratumLabel.setObjectName(_fromUtf8("mAddStratumLabel"))
        self.gridLayout.addWidget(self.mAddStratumLabel, 1, 0, 1, 1)
        self.mAddStratumToolButton = QtGui.QToolButton(SurveyDesignDialogBase)
        self.mAddStratumToolButton.setIcon(icon)
        self.mAddStratumToolButton.setCheckable(True)
        self.mAddStratumToolButton.setObjectName(_fromUtf8("mAddStratumToolButton"))
        self.gridLayout.addWidget(self.mAddStratumToolButton, 1, 1, 1, 1)
        self.mAddSurveyAreaLabel = QtGui.QLabel(SurveyDesignDialogBase)
        self.mAddSurveyAreaLabel.setObjectName(_fromUtf8("mAddSurveyAreaLabel"))
        self.gridLayout.addWidget(self.mAddSurveyAreaLabel, 0, 0, 1, 1)
        self.mAddSurveyAreaToolButton = QtGui.QToolButton(SurveyDesignDialogBase)
        self.mAddSurveyAreaToolButton.setIcon(icon)
        self.mAddSurveyAreaToolButton.setCheckable(True)
        self.mAddSurveyAreaToolButton.setObjectName(_fromUtf8("mAddSurveyAreaToolButton"))
        self.gridLayout.addWidget(self.mAddSurveyAreaToolButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mPointSurveyRadioButton = QtGui.QRadioButton(SurveyDesignDialogBase)
        self.mPointSurveyRadioButton.setObjectName(_fromUtf8("mPointSurveyRadioButton"))
        self.horizontalLayout.addWidget(self.mPointSurveyRadioButton)
        self.mTransectSurveyRadioButton = QtGui.QRadioButton(SurveyDesignDialogBase)
        self.mTransectSurveyRadioButton.setObjectName(_fromUtf8("mTransectSurveyRadioButton"))
        self.horizontalLayout.addWidget(self.mTransectSurveyRadioButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mShareBaselineCheckBox = QtGui.QCheckBox(SurveyDesignDialogBase)
        self.mShareBaselineCheckBox.setChecked(False)
        self.mShareBaselineCheckBox.setObjectName(_fromUtf8("mShareBaselineCheckBox"))
        self.horizontalLayout_2.addWidget(self.mShareBaselineCheckBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(196, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.mCreateSampleButton = QtGui.QPushButton(SurveyDesignDialogBase)
        self.mCreateSampleButton.setObjectName(_fromUtf8("mCreateSampleButton"))
        self.gridLayout_2.addWidget(self.mCreateSampleButton, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SurveyDesignDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.retranslateUi(SurveyDesignDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SurveyDesignDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SurveyDesignDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SurveyDesignDialogBase)

    def retranslateUi(self, SurveyDesignDialogBase):
        SurveyDesignDialogBase.setWindowTitle(QtGui.QApplication.translate("SurveyDesignDialogBase", "Survey design", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddBaselineLabel.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Add baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddBaselineToolButton.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddStratumLabel.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Add stratum", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddStratumToolButton.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddSurveyAreaLabel.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Add survey area", None, QtGui.QApplication.UnicodeUTF8))
        self.mAddSurveyAreaToolButton.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mPointSurveyRadioButton.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Point survey", None, QtGui.QApplication.UnicodeUTF8))
        self.mTransectSurveyRadioButton.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Transect survey", None, QtGui.QApplication.UnicodeUTF8))
        self.mShareBaselineCheckBox.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Share baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.mCreateSampleButton.setText(QtGui.QApplication.translate("SurveyDesignDialogBase", "Create sample", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
