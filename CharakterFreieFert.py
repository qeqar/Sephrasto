# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterFreieFert.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 421)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.editFF8 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF8.setObjectName("editFF8")
        self.horizontalLayout_10.addWidget(self.editFF8)
        self.comboFF8 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF8.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF8.setObjectName("comboFF8")
        self.comboFF8.addItem("")
        self.comboFF8.addItem("")
        self.comboFF8.addItem("")
        self.horizontalLayout_10.addWidget(self.comboFF8)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editFF1 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF1.setReadOnly(True)
        self.editFF1.setObjectName("editFF1")
        self.horizontalLayout_2.addWidget(self.editFF1)
        self.comboFF1 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF1.setEnabled(False)
        self.comboFF1.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF1.setEditable(False)
        self.comboFF1.setObjectName("comboFF1")
        self.comboFF1.addItem("")
        self.comboFF1.addItem("")
        self.comboFF1.addItem("")
        self.horizontalLayout_2.addWidget(self.comboFF1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.editFF5 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF5.setObjectName("editFF5")
        self.horizontalLayout_5.addWidget(self.editFF5)
        self.comboFF5 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF5.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF5.setObjectName("comboFF5")
        self.comboFF5.addItem("")
        self.comboFF5.addItem("")
        self.comboFF5.addItem("")
        self.horizontalLayout_5.addWidget(self.comboFF5)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editFF2 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF2.setObjectName("editFF2")
        self.horizontalLayout_3.addWidget(self.editFF2)
        self.comboFF2 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF2.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF2.setObjectName("comboFF2")
        self.comboFF2.addItem("")
        self.comboFF2.addItem("")
        self.comboFF2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboFF2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.editFF11 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF11.setObjectName("editFF11")
        self.horizontalLayout_7.addWidget(self.editFF11)
        self.comboFF11 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF11.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF11.setObjectName("comboFF11")
        self.comboFF11.addItem("")
        self.comboFF11.addItem("")
        self.comboFF11.addItem("")
        self.horizontalLayout_7.addWidget(self.comboFF11)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 2, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.editFF12 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF12.setObjectName("editFF12")
        self.horizontalLayout_12.addWidget(self.editFF12)
        self.comboFF12 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF12.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF12.setObjectName("comboFF12")
        self.comboFF12.addItem("")
        self.comboFF12.addItem("")
        self.comboFF12.addItem("")
        self.horizontalLayout_12.addWidget(self.comboFF12)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 3, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editFF7 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF7.setObjectName("editFF7")
        self.horizontalLayout.addWidget(self.editFF7)
        self.comboFF7 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF7.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF7.setObjectName("comboFF7")
        self.comboFF7.addItem("")
        self.comboFF7.addItem("")
        self.comboFF7.addItem("")
        self.horizontalLayout.addWidget(self.comboFF7)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.editFF6 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF6.setObjectName("editFF6")
        self.horizontalLayout_8.addWidget(self.editFF6)
        self.comboFF6 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF6.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF6.setObjectName("comboFF6")
        self.comboFF6.addItem("")
        self.comboFF6.addItem("")
        self.comboFF6.addItem("")
        self.horizontalLayout_8.addWidget(self.comboFF6)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 3, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.editFF9 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF9.setObjectName("editFF9")
        self.horizontalLayout_11.addWidget(self.editFF9)
        self.comboFF9 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF9.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF9.setObjectName("comboFF9")
        self.comboFF9.addItem("")
        self.comboFF9.addItem("")
        self.comboFF9.addItem("")
        self.horizontalLayout_11.addWidget(self.comboFF9)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 2, 3, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editFF4 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF4.setObjectName("editFF4")
        self.horizontalLayout_4.addWidget(self.editFF4)
        self.comboFF4 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF4.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF4.setObjectName("comboFF4")
        self.comboFF4.addItem("")
        self.comboFF4.addItem("")
        self.comboFF4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboFF4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.editFF3 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF3.setObjectName("editFF3")
        self.horizontalLayout_6.addWidget(self.editFF3)
        self.comboFF3 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF3.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF3.setObjectName("comboFF3")
        self.comboFF3.addItem("")
        self.comboFF3.addItem("")
        self.comboFF3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboFF3)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 3, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.editFF10 = QtWidgets.QLineEdit(self.groupBox)
        self.editFF10.setObjectName("editFF10")
        self.horizontalLayout_9.addWidget(self.editFF10)
        self.comboFF10 = QtWidgets.QComboBox(self.groupBox)
        self.comboFF10.setMaximumSize(QtCore.QSize(38, 16777215))
        self.comboFF10.setObjectName("comboFF10")
        self.comboFF10.addItem("")
        self.comboFF10.addItem("")
        self.comboFF10.addItem("")
        self.horizontalLayout_9.addWidget(self.comboFF10)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 18))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.comboFF8.setCurrentIndex(0)
        self.comboFF1.setCurrentIndex(2)
        self.comboFF5.setCurrentIndex(0)
        self.comboFF2.setCurrentIndex(0)
        self.comboFF11.setCurrentIndex(0)
        self.comboFF12.setCurrentIndex(0)
        self.comboFF7.setCurrentIndex(0)
        self.comboFF6.setCurrentIndex(0)
        self.comboFF9.setCurrentIndex(0)
        self.comboFF4.setCurrentIndex(0)
        self.comboFF3.setCurrentIndex(0)
        self.comboFF10.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.editFF1, self.comboFF1)
        Form.setTabOrder(self.comboFF1, self.editFF2)
        Form.setTabOrder(self.editFF2, self.comboFF2)
        Form.setTabOrder(self.comboFF2, self.editFF3)
        Form.setTabOrder(self.editFF3, self.comboFF3)
        Form.setTabOrder(self.comboFF3, self.editFF4)
        Form.setTabOrder(self.editFF4, self.comboFF4)
        Form.setTabOrder(self.comboFF4, self.editFF5)
        Form.setTabOrder(self.editFF5, self.comboFF5)
        Form.setTabOrder(self.comboFF5, self.editFF6)
        Form.setTabOrder(self.editFF6, self.comboFF6)
        Form.setTabOrder(self.comboFF6, self.editFF7)
        Form.setTabOrder(self.editFF7, self.comboFF7)
        Form.setTabOrder(self.comboFF7, self.editFF8)
        Form.setTabOrder(self.editFF8, self.comboFF8)
        Form.setTabOrder(self.comboFF8, self.editFF9)
        Form.setTabOrder(self.editFF9, self.comboFF9)
        Form.setTabOrder(self.comboFF9, self.editFF10)
        Form.setTabOrder(self.editFF10, self.comboFF10)
        Form.setTabOrder(self.comboFF10, self.editFF11)
        Form.setTabOrder(self.editFF11, self.comboFF11)
        Form.setTabOrder(self.comboFF11, self.editFF12)
        Form.setTabOrder(self.editFF12, self.comboFF12)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboFF8.setItemText(0, _translate("Form", "I"))
        self.comboFF8.setItemText(1, _translate("Form", "II"))
        self.comboFF8.setItemText(2, _translate("Form", "III"))
        self.editFF1.setText(_translate("Form", "Muttersprache"))
        self.comboFF1.setItemText(0, _translate("Form", "I"))
        self.comboFF1.setItemText(1, _translate("Form", "II"))
        self.comboFF1.setItemText(2, _translate("Form", "III"))
        self.comboFF5.setItemText(0, _translate("Form", "I"))
        self.comboFF5.setItemText(1, _translate("Form", "II"))
        self.comboFF5.setItemText(2, _translate("Form", "III"))
        self.comboFF2.setItemText(0, _translate("Form", "I"))
        self.comboFF2.setItemText(1, _translate("Form", "II"))
        self.comboFF2.setItemText(2, _translate("Form", "III"))
        self.comboFF11.setItemText(0, _translate("Form", "I"))
        self.comboFF11.setItemText(1, _translate("Form", "II"))
        self.comboFF11.setItemText(2, _translate("Form", "III"))
        self.comboFF12.setItemText(0, _translate("Form", "I"))
        self.comboFF12.setItemText(1, _translate("Form", "II"))
        self.comboFF12.setItemText(2, _translate("Form", "III"))
        self.comboFF7.setItemText(0, _translate("Form", "I"))
        self.comboFF7.setItemText(1, _translate("Form", "II"))
        self.comboFF7.setItemText(2, _translate("Form", "III"))
        self.comboFF6.setItemText(0, _translate("Form", "I"))
        self.comboFF6.setItemText(1, _translate("Form", "II"))
        self.comboFF6.setItemText(2, _translate("Form", "III"))
        self.comboFF9.setItemText(0, _translate("Form", "I"))
        self.comboFF9.setItemText(1, _translate("Form", "II"))
        self.comboFF9.setItemText(2, _translate("Form", "III"))
        self.comboFF4.setItemText(0, _translate("Form", "I"))
        self.comboFF4.setItemText(1, _translate("Form", "II"))
        self.comboFF4.setItemText(2, _translate("Form", "III"))
        self.comboFF3.setItemText(0, _translate("Form", "I"))
        self.comboFF3.setItemText(1, _translate("Form", "II"))
        self.comboFF3.setItemText(2, _translate("Form", "III"))
        self.comboFF10.setItemText(0, _translate("Form", "I"))
        self.comboFF10.setItemText(1, _translate("Form", "II"))
        self.comboFF10.setItemText(2, _translate("Form", "III"))
        self.label.setText(_translate("Form", "Jeder Charakter beherrscht seine Muttersprache meisterlich, ohne dafür zu bezahlen."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

