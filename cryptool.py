import sys
from PyQt6.QtWidgets import *
from ui import cryptoolWindow

class cryptool:
    def __init__(self, view):
        self._view = view

def main():
    cryptoolApp = QApplication([])
    cryptoolWindowView = cryptoolWindow.cryptoolWindow()
    cryptoolWindowView.show()
    cryptool(view=cryptoolWindowView)
    sys.exit(cryptoolApp.exec())

if __name__ == "__main__":
    main()