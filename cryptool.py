import sys
from PyQt6.QtWidgets import *


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750

class CryptoolWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cryptool")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createInputBox()
        self._createOptions()
        self._creatOutputBox()

    def _createInputBox(self):
        self.inputBox = QPlainTextEdit()
        self.inputBox.setMaximumSize(WINDOW_WIDTH, 200)
        self.generalLayout.addWidget(self.inputBox)

    def _createOptions(self):
        
        optionsLayout = QGridLayout()
        optionsLayout.addWidget(QRadioButton("Convert"), 0, 0)
        optionsLayout.addWidget(QRadioButton("Encrypt"), 0, 2)
        optionsLayout.addWidget(QRadioButton("Crack"), 0, 4)
        
        converting = ["Binary", "Decimal", "Hexidecimal", "Base64", "Text"]
        convertOptionsFrom = QComboBox()
        convertOptionsTo = QComboBox()
        convertOptionsFrom.addItems(converting)
        convertOptionsTo.addItems(converting)
        optionsLayout.addWidget(QLabel("From:"), 1, 0)
        optionsLayout.addWidget(convertOptionsFrom, 1, 1)
        optionsLayout.addWidget(QLabel("To:"), 2, 0)
        optionsLayout.addWidget(convertOptionsTo, 2, 1)

        encrypting = ["Caesar Cipher", "XOR", "RSA"]
        encryptOptions = QComboBox()
        encryptOptions.addItems(encrypting)
        optionsLayout.addWidget(QLabel("Type:"), 1, 2)
        optionsLayout.addWidget(encryptOptions, 1, 3)

        cracking = ["Weiners"]
        crackOptions = QComboBox()
        crackOptions.addItems(cracking)
        optionsLayout.addWidget(QLabel("Type:"), 1, 4)
        optionsLayout.addWidget(crackOptions, 1, 5)
        
        clearButton = QPushButton("Clear")
        optionsLayout.addWidget(clearButton, 3, 2)
        goButton = QPushButton("Go")
        optionsLayout.addWidget(goButton, 3, 3)
        
        self.generalLayout.addLayout(optionsLayout)

    def _creatOutputBox(self):
        self.outputBox = QPlainTextEdit()
        self.outputBox.setReadOnly(True)
        self.outputBox.setMaximumSize(WINDOW_WIDTH, 200)
        self.generalLayout.addWidget(self.outputBox)

def main():
    cryptoolApp = QApplication([])
    cryptoolWindow = CryptoolWindow()
    cryptoolWindow.show()
    sys.exit(cryptoolApp.exec())

if __name__ == "__main__":
    main()