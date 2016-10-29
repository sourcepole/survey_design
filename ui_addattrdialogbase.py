# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addattrdialogbase.ui'
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

class Ui_AddAttrDialogBase(object):
    def setupUi(self, AddAttrDialogBase):
        AddAttrDialogBase.setObjectName(_fromUtf8("AddAttrDialogBase"))
        AddAttrDialogBase.resize(268, 259)
        AddAttrDialogBase.setModal(True)
        self.gridLayout = QtGui.QGridLayout(AddAttrDialogBase)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mPrecLabel = QtGui.QLabel(AddAttrDialogBase)
        self.mPrecLabel.setObjectName(_fromUtf8("mPrecLabel"))
        self.gridLayout.addWidget(self.mPrecLabel, 3, 0, 1, 1)
        self.mLength = QtGui.QSpinBox(AddAttrDialogBase)
        self.mLength.setObjectName(_fromUtf8("mLength"))
        self.gridLayout.addWidget(self.mLength, 2, 1, 1, 1)
        self.textLabel1 = QtGui.QLabel(AddAttrDialogBase)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.mTypeBox = QtGui.QComboBox(AddAttrDialogBase)
        self.mTypeBox.setObjectName(_fromUtf8("mTypeBox"))
        self.gridLayout.addWidget(self.mTypeBox, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AddAttrDialogBase)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)
        self.textLabel2 = QtGui.QLabel(AddAttrDialogBase)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridLayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.mLengthLabel = QtGui.QLabel(AddAttrDialogBase)
        self.mLengthLabel.setObjectName(_fromUtf8("mLengthLabel"))
        self.gridLayout.addWidget(self.mLengthLabel, 2, 0, 1, 1)
        self.mPrec = QtGui.QSpinBox(AddAttrDialogBase)
        self.mPrec.setObjectName(_fromUtf8("mPrec"))
        self.gridLayout.addWidget(self.mPrec, 3, 1, 1, 1)
        self.mNameEdit = QtGui.QLineEdit(AddAttrDialogBase)
        self.mNameEdit.setObjectName(_fromUtf8("mNameEdit"))
        self.gridLayout.addWidget(self.mNameEdit, 0, 1, 1, 1)
        self.mPrecLabel.setBuddy(self.mPrec)
        self.textLabel1.setBuddy(self.mNameEdit)
        self.textLabel2.setBuddy(self.mTypeBox)
        self.mLengthLabel.setBuddy(self.mLength)

        self.retranslateUi(AddAttrDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddAttrDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddAttrDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AddAttrDialogBase)
        AddAttrDialogBase.setTabOrder(self.mNameEdit, self.mTypeBox)
        AddAttrDialogBase.setTabOrder(self.mTypeBox, self.mLength)
        AddAttrDialogBase.setTabOrder(self.mLength, self.mPrec)
        AddAttrDialogBase.setTabOrder(self.mPrec, self.buttonBox)

    def retranslateUi(self, AddAttrDialogBase):
        AddAttrDialogBase.setWindowTitle(_translate("AddAttrDialogBase", "Add field", None))
        self.mPrecLabel.setText(_translate("AddAttrDialogBase", "Precision", None))
        self.textLabel1.setText(_translate("AddAttrDialogBase", "N&ame", None))
        self.textLabel2.setText(_translate("AddAttrDialogBase", "Type", None))
        self.mLengthLabel.setText(_translate("AddAttrDialogBase", "Length", None))

