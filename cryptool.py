import sys
from PyQt6.QtWidgets import *
from functools import partial
import ui.mainWindow as cryptoolWindow
from cryptoolFunctions import *
from encryptors import *

def goButton(view):
    action = view.action
    
    if action == "Convert":
        convertFrom = view.convertOptionsFrom.currentText()
        convertTo = view.convertOptionsTo.currentText()
        input = view.inputBox.toPlainText()
        byBytes = view.byByteCheck.isChecked()
        output = convertMain(convertFrom, convertTo, input, byBytes)

        toDisplay = ''
        for item in output:
            toDisplay += item + ' '

        view.displayOutput(str(toDisplay))
    elif action == "Encrypt":
        if view.encryptOptions.currentText() == "Caesar Cipher":
            input = view.inputBox.toPlainText()
            alphabet = view.ccAlphabet
            shift = view.ccShift
            maintainCase = view.ccMaintainCase
            maintainForeignChar = view.ccMaintainForeignChar
            shiftNumbers = view.ccShiftNumbers

            output = caesarCipherMain(input, alphabet, int(shift), maintainCase, maintainForeignChar, shiftNumbers)
        view.displayOutput(str(output))

    elif action == "Crack":
        #call function
        print("running crack")
    else:
        print(action)


class cryptool:
    def __init__(self, view):
        self._view = view
        self._connectSlots()

    def _connectSlots(self):
        self._view.settingsButton.clicked.connect(self._view.settingsPopup)
        self._view.clearButton.clicked.connect(self._view.clearDisplay)
        self._view.goButton.clicked.connect(partial(goButton, self._view))

def main():
    cryptoolApp = QApplication([])
    cryptoolWindowView = cryptoolWindow.cryptoolWindow()
    cryptoolWindowView.show()
    cryptool(view=cryptoolWindowView)
    sys.exit(cryptoolApp.exec())

if __name__ == "__main__":
    main()