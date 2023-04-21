import sys
from PyQt6.QtWidgets import *
from functools import partial
import ui.mainWindow as cryptoolWindow
from cryptoolFunctions import *

def goButton(view):
    action = view.action
    if action == "Convert":
        convertFrom = view.convertOptionsFrom.currentText()
        convertTo = view.convertOptionsTo.currentText()
        input = view.inputBox.toPlainText()
        output = convertMain(convertFrom, convertTo, input)
        view.displayOutput(str(output))
    elif action == "Encrypt":
        #call function
        print("running encrypt")
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
        self._view.clearButton.clicked.connect(self._view.clearDisplay)
        self._view.goButton.clicked.connect(partial(goButton, self._view))

def main():
    cryptoolApp = QApplication([])
    #cryptoolWindowView = cryptoolWindow()
    cryptoolWindowView = cryptoolWindow.cryptoolWindow()
    cryptoolWindowView.show()
    cryptool(view=cryptoolWindowView)
    sys.exit(cryptoolApp.exec())

if __name__ == "__main__":
    main()