# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formMain(object):
    def setupUi(self, formMain):
        formMain.setObjectName("formMain")
        formMain.setWindowModality(QtCore.Qt.ApplicationModal)
        formMain.resize(506, 472)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formMain.sizePolicy().hasHeightForWidth())
        formMain.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(formMain)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnCancel = QtWidgets.QPushButton(formMain)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnAccept = QtWidgets.QPushButton(formMain)
        self.btnAccept.setEnabled(True)
        self.btnAccept.setMinimumSize(QtCore.QSize(100, 0))
        self.btnAccept.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout_3.addWidget(self.btnAccept)
        self.gridLayout.addLayout(self.horizontalLayout_3, 15, 0, 1, 2)
        self.cbRegeln = QtWidgets.QComboBox(formMain)
        self.cbRegeln.setMinimumSize(QtCore.QSize(300, 0))
        self.cbRegeln.setObjectName("cbRegeln")
        self.gridLayout.addWidget(self.cbRegeln, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(formMain)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 17, 0, 1, 2)
        self.cbKultur = QtWidgets.QComboBox(formMain)
        self.cbKultur.setObjectName("cbKultur")
        self.gridLayout.addWidget(self.cbKultur, 6, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(formMain)
        self.label_2.setStyleSheet("background: #e8c5a9;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.lblGeschlecht = QtWidgets.QLabel(formMain)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblGeschlecht.setFont(font)
        self.lblGeschlecht.setObjectName("lblGeschlecht")
        self.gridLayout.addWidget(self.lblGeschlecht, 4, 0, 1, 1)
        self.lblRegeln = QtWidgets.QLabel(formMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRegeln.sizePolicy().hasHeightForWidth())
        self.lblRegeln.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblRegeln.setFont(font)
        self.lblRegeln.setObjectName("lblRegeln")
        self.gridLayout.addWidget(self.lblRegeln, 3, 0, 1, 1)
        self.lblProfession = QtWidgets.QLabel(formMain)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProfession.setFont(font)
        self.lblProfession.setObjectName("lblProfession")
        self.gridLayout.addWidget(self.lblProfession, 8, 0, 1, 1)
        self.lblProfessionKategorie = QtWidgets.QLabel(formMain)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProfessionKategorie.setFont(font)
        self.lblProfessionKategorie.setObjectName("lblProfessionKategorie")
        self.gridLayout.addWidget(self.lblProfessionKategorie, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnWeiblich = QtWidgets.QRadioButton(formMain)
        self.btnWeiblich.setChecked(True)
        self.btnWeiblich.setObjectName("btnWeiblich")
        self.horizontalLayout.addWidget(self.btnWeiblich)
        self.btnMaennlich = QtWidgets.QRadioButton(formMain)
        self.btnMaennlich.setObjectName("btnMaennlich")
        self.horizontalLayout.addWidget(self.btnMaennlich)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.lblSpezies = QtWidgets.QLabel(formMain)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSpezies.setFont(font)
        self.lblSpezies.setObjectName("lblSpezies")
        self.gridLayout.addWidget(self.lblSpezies, 5, 0, 1, 1)
        self.cbSpezies = QtWidgets.QComboBox(formMain)
        self.cbSpezies.setMinimumSize(QtCore.QSize(300, 0))
        self.cbSpezies.setObjectName("cbSpezies")
        self.gridLayout.addWidget(self.cbSpezies, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(formMain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 16, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 11, 0, 1, 1)
        self.lblKultur = QtWidgets.QLabel(formMain)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblKultur.setFont(font)
        self.lblKultur.setObjectName("lblKultur")
        self.gridLayout.addWidget(self.lblKultur, 6, 0, 1, 1)
        self.cbProfessionKategorie = QtWidgets.QComboBox(formMain)
        self.cbProfessionKategorie.setObjectName("cbProfessionKategorie")
        self.gridLayout.addWidget(self.cbProfessionKategorie, 7, 1, 1, 1)
        self.cbProfession = QtWidgets.QComboBox(formMain)
        self.cbProfession.setObjectName("cbProfession")
        self.gridLayout.addWidget(self.cbProfession, 8, 1, 1, 1)

        self.retranslateUi(formMain)
        QtCore.QMetaObject.connectSlotsByName(formMain)

    def retranslateUi(self, formMain):
        _translate = QtCore.QCoreApplication.translate
        formMain.setWindowTitle(_translate("formMain", "Charakterassistent"))
        self.btnCancel.setText(_translate("formMain", "Ohne Assistent fortfahren"))
        self.btnAccept.setText(_translate("formMain", "Übernehmen"))
        self.label.setText(_translate("formMain", "<html><head/><body><p>Der Charakterassistent lebt von Communitybeiträgen. Eigene Spezies/Kulturen/Professionen/Archetypen lassen sich spielend leicht erstellen. Finde hier heraus wie und teile deine Kreationen: <a href=\"https://dsaforum.de/viewtopic.php?f=180&amp;t=56703\"><span style=\" text-decoration: underline;\">Charakterassistent auf dsaforum.de</span></a></p></body></html>"))
        self.label_2.setText(_translate("formMain", "Dieser Assistent betreut dich bei der Erstellung deines Charakters. Bei den Professionen sind manchmal Namen mitangegeben - dies sind vollwertige Archetypen mit Eigenheiten. Die angegebenen benötigten Erfahrungspunkte können niedriger oder höher ausfallen."))
        self.lblGeschlecht.setText(_translate("formMain", "Geschlecht"))
        self.lblRegeln.setText(_translate("formMain", "Baukasten"))
        self.lblProfession.setText(_translate("formMain", "Profession"))
        self.lblProfessionKategorie.setText(_translate("formMain", "Professionskategorie"))
        self.btnWeiblich.setText(_translate("formMain", "Weiblich"))
        self.btnMaennlich.setText(_translate("formMain", "Männlich"))
        self.lblSpezies.setText(_translate("formMain", "Spezies"))
        self.lblKultur.setText(_translate("formMain", "Kultur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formMain = QtWidgets.QWidget()
    ui = Ui_formMain()
    ui.setupUi(formMain)
    formMain.show()
    sys.exit(app.exec_())
