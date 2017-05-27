# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surveypropertiesbase.ui'
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

class Ui_SurveyPropertiesBase(object):
    def setupUi(self, SurveyPropertiesBase):
        SurveyPropertiesBase.setObjectName(_fromUtf8("SurveyPropertiesBase"))
        SurveyPropertiesBase.resize(400, 380)
        self.gridLayout = QtGui.QGridLayout(SurveyPropertiesBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mSurveyLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mSurveyLabel.setObjectName(_fromUtf8("mSurveyLabel"))
        self.gridLayout.addWidget(self.mSurveyLabel, 0, 0, 1, 1)
        self.mSurveyLineEdit = QtGui.QLineEdit(SurveyPropertiesBase)
        self.mSurveyLineEdit.setObjectName(_fromUtf8("mSurveyLineEdit"))
        self.gridLayout.addWidget(self.mSurveyLineEdit, 0, 1, 1, 1)
        self.mProjectCodeLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mProjectCodeLabel.setObjectName(_fromUtf8("mProjectCodeLabel"))
        self.gridLayout.addWidget(self.mProjectCodeLabel, 1, 0, 1, 1)
        self.mProjectCodeLineEdit = QtGui.QLineEdit(SurveyPropertiesBase)
        self.mProjectCodeLineEdit.setObjectName(_fromUtf8("mProjectCodeLineEdit"))
        self.gridLayout.addWidget(self.mProjectCodeLineEdit, 1, 1, 1, 1)
        self.mDateSLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mDateSLabel.setObjectName(_fromUtf8("mDateSLabel"))
        self.gridLayout.addWidget(self.mDateSLabel, 2, 0, 1, 1)
        self.mDateSEdit = QtGui.QDateEdit(SurveyPropertiesBase)
        self.mDateSEdit.setObjectName(_fromUtf8("mDateSEdit"))
        self.gridLayout.addWidget(self.mDateSEdit, 2, 1, 1, 1)
        self.mDateFLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mDateFLabel.setObjectName(_fromUtf8("mDateFLabel"))
        self.gridLayout.addWidget(self.mDateFLabel, 3, 0, 1, 1)
        self.mDateFEdit = QtGui.QDateEdit(SurveyPropertiesBase)
        self.mDateFEdit.setObjectName(_fromUtf8("mDateFEdit"))
        self.gridLayout.addWidget(self.mDateFEdit, 3, 1, 1, 1)
        self.mContactNameLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mContactNameLabel.setObjectName(_fromUtf8("mContactNameLabel"))
        self.gridLayout.addWidget(self.mContactNameLabel, 4, 0, 1, 1)
        self.mContactNameLineEdit = QtGui.QLineEdit(SurveyPropertiesBase)
        self.mContactNameLineEdit.setObjectName(_fromUtf8("mContactNameLineEdit"))
        self.gridLayout.addWidget(self.mContactNameLineEdit, 4, 1, 1, 1)
        self.mAreasLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mAreasLabel.setObjectName(_fromUtf8("mAreasLabel"))
        self.gridLayout.addWidget(self.mAreasLabel, 5, 0, 1, 1)
        self.mAreasLineEdit = QtGui.QLineEdit(SurveyPropertiesBase)
        self.mAreasLineEdit.setObjectName(_fromUtf8("mAreasLineEdit"))
        self.gridLayout.addWidget(self.mAreasLineEdit, 5, 1, 1, 1)
        self.mMainSppLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mMainSppLabel.setObjectName(_fromUtf8("mMainSppLabel"))
        self.gridLayout.addWidget(self.mMainSppLabel, 6, 0, 1, 1)
        self.mMainSppLineEdit = QtGui.QLineEdit(SurveyPropertiesBase)
        self.mMainSppLineEdit.setObjectName(_fromUtf8("mMainSppLineEdit"))
        self.gridLayout.addWidget(self.mMainSppLineEdit, 6, 1, 1, 1)
        self.mCommentsLabel = QtGui.QLabel(SurveyPropertiesBase)
        self.mCommentsLabel.setObjectName(_fromUtf8("mCommentsLabel"))
        self.gridLayout.addWidget(self.mCommentsLabel, 7, 0, 1, 1)
        self.mCommentsLIneEdit = QtGui.QLineEdit(SurveyPropertiesBase)
        self.mCommentsLIneEdit.setObjectName(_fromUtf8("mCommentsLIneEdit"))
        self.gridLayout.addWidget(self.mCommentsLIneEdit, 7, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SurveyPropertiesBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 8, 0, 1, 2)

        self.retranslateUi(SurveyPropertiesBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SurveyPropertiesBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SurveyPropertiesBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SurveyPropertiesBase)

    def retranslateUi(self, SurveyPropertiesBase):
        SurveyPropertiesBase.setWindowTitle(_translate("SurveyPropertiesBase", "Survey properties", None))
        self.mSurveyLabel.setText(_translate("SurveyPropertiesBase", "Survey", None))
        self.mProjectCodeLabel.setText(_translate("SurveyPropertiesBase", "Project code", None))
        self.mDateSLabel.setText(_translate("SurveyPropertiesBase", "date_s", None))
        self.mDateFLabel.setText(_translate("SurveyPropertiesBase", "date_f", None))
        self.mContactNameLabel.setText(_translate("SurveyPropertiesBase", "Contact name", None))
        self.mAreasLabel.setText(_translate("SurveyPropertiesBase", "Areas", None))
        self.mMainSppLabel.setText(_translate("SurveyPropertiesBase", "mainspp", None))
        self.mCommentsLabel.setText(_translate("SurveyPropertiesBase", "Comments", None))

