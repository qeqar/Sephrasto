# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:52:34 2017

@author: Aeolitus
"""
import Objekte
import UI.DatenbankEditWaffeneigenschaft
from PySide6 import QtWidgets, QtCore
from Wolke import Wolke

class DatenbankEditWaffeneigenschaftWrapper(object):
    def __init__(self, datenbank, waffeneigenschaft=None, readonly = False):
        super().__init__()
        self.datenbank = datenbank
        if waffeneigenschaft is None:
            waffeneigenschaft = Objekte.Waffeneigenschaft()
        self.waffeneigenschaftPicked = waffeneigenschaft
        self.nameValid = True
        self.readonly = readonly
        self.waffeneigenschaftDialog = QtWidgets.QDialog()
        self.ui = UI.DatenbankEditWaffeneigenschaft.Ui_waffeneigenschaftDialog()
        self.ui.setupUi(self.waffeneigenschaftDialog)
        
        if not waffeneigenschaft.isUserAdded:
            if readonly:
                self.ui.warning.setText("Gelöschte Elemente können nicht verändert werden.")
            self.ui.warning.setVisible(True)

        self.waffeneigenschaftDialog.setWindowFlags(
                QtCore.Qt.Window |
                QtCore.Qt.CustomizeWindowHint |
                QtCore.Qt.WindowTitleHint |
                QtCore.Qt.WindowCloseButtonHint |
                QtCore.Qt.WindowMaximizeButtonHint |
                QtCore.Qt.WindowMinimizeButtonHint)
        
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setText("Speichern")
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Abbrechen")

        windowSize = Wolke.Settings["WindowSize-DBWaffeneigenschaft"]
        self.waffeneigenschaftDialog.resize(windowSize[0], windowSize[1])

        self.ui.nameEdit.setText(waffeneigenschaft.name)
        self.ui.nameEdit.textChanged.connect(self.nameChanged)
        self.nameChanged()

        self.ui.textEdit.setPlainText(waffeneigenschaft.text)
        self.ui.scriptPrioEdit.setValue(waffeneigenschaft.scriptPrio)

        scriptPrioDoc = [
            "Die Skript-Priorität legt die Reihenfolge der Auswertung fest. 0 ist Standard, negative Werte werden davor,",
            "positive Werte danach ausgewertet. Dies ist relevant, falls bspw. die INI verdoppelt werden soll nachdem",
            "Kampfreflexe eingerechnet wurde. In diesem Fall sollte die Skript-Priorität höher als die von Kampfreflexe sein."
        ]

        self.ui.scriptPrioEdit.setToolTip("\n".join(scriptPrioDoc))

        self.ui.scriptEdit.setText(waffeneigenschaft.script)

        self.ui.scriptEdit.setToolTip("Siehe \"Skripte für Vorteile und Waffeneigenschaften\" in der Sephrasto-Hilfe für verfügbare Funktionen und Beispiele.")

        self.waffeneigenschaftDialog.show()
        ret = self.waffeneigenschaftDialog.exec()

        Wolke.Settings["WindowSize-DBWaffeneigenschaft"] = [self.waffeneigenschaftDialog.size().width(), self.waffeneigenschaftDialog.size().height()]

        if ret == QtWidgets.QDialog.Accepted:
            self.waffeneigenschaft = Objekte.Waffeneigenschaft()
            self.waffeneigenschaft.name = self.ui.nameEdit.text()
            self.waffeneigenschaft.text = self.ui.textEdit.toPlainText()

            self.waffeneigenschaft.scriptPrio = self.ui.scriptPrioEdit.value()
            self.waffeneigenschaft.script = str.strip(self.ui.scriptEdit.text())

            self.waffeneigenschaft.isUserAdded = False
            if self.waffeneigenschaft == self.waffeneigenschaftPicked:
                self.waffeneigenschaft = None
            else:
                self.waffeneigenschaft.isUserAdded = True
        else:
            self.waffeneigenschaft = None
           
    def nameChanged(self):
        name = self.ui.nameEdit.text()
        if name == "":
            self.ui.nameEdit.setToolTip("Name darf nicht leer sein.")
            self.ui.nameEdit.setStyleSheet("border: 1px solid red;")
            self.nameValid = False
        elif name != self.waffeneigenschaftPicked.name and name in self.datenbank.waffeneigenschaften:
            self.ui.nameEdit.setToolTip("Name existiert bereits.")
            self.ui.nameEdit.setStyleSheet("border: 1px solid red;")
            self.nameValid = False
        else:
            self.ui.nameEdit.setToolTip("")
            self.ui.nameEdit.setStyleSheet("")
            self.nameValid = True
        self.updateSaveButtonState()

    def updateSaveButtonState(self):
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setEnabled(not self.readonly and self.nameValid)