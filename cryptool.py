import sys
from PyQt6.QtWidgets import *
from functools import partial
import ui.mainWindow as cryptoolWindow
from cryptoolFunctions import convertMain, encryptMain
#from encryptors import *

def goButton(view):
    action = view.action
    
    if action == "Convert":
        output = convertMain(view)

        # This part is needed because conversion returns a list
        toDisplay = ''
        for item in output:
            toDisplay += item + ' '

        view.displayOutput(str(toDisplay))
    elif action == "Encrypt":
        toDisplay = encryptMain(view)
        view.displayOutput(str(toDisplay))

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